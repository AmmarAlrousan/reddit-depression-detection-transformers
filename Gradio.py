# 📚 استيراد المكتبات
import gradio as gr
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# 📦 تعريف المسارات للنموذجين
model_dirs = ['Models\nreimers MiniLM Model', 'Models\saved_model_electra']
models = []
tokenizers = []
devices = []

# 📦 تحميل الموديلين والـ tokenizers
for dir in model_dirs:
    tokenizer = AutoTokenizer.from_pretrained(dir)
    model = AutoModelForSequenceClassification.from_pretrained(dir)
    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
    model.to(device)

    tokenizers.append(tokenizer)
    models.append(model)
    devices.append(device)

print("✅ تم تحميل جميع النماذج والتوكنيزر بنجاح.")

# 🔥 دالة التنبؤ
def predict(text):
    results = []
    for model, tokenizer, device in zip(models, tokenizers, devices):
        inputs = tokenizer(
            text,
            truncation=True,
            padding='max_length',
            max_length=128,
            return_tensors='pt'
        )
        inputs = {key: val.to(device) for key, val in inputs.items()}

        model.eval()
        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits
            prediction = torch.argmax(logits, dim=-1).item()

        label = "🔵 مصاب بالاكتئاب" if prediction == 1 else "🟢 غير مصاب بالاكتئاب"
        results.append(label)

    # 💬 تنسيق النتيجة بشكل جميل
    return f"👨‍🔬 نتيجة النموذج الأول:\n{results[0]}\n\n👩‍🔬 نتيجة النموذج الثاني:\n{results[1]}"

# 🎨 بناء واجهة Gradio
interface = gr.Interface(
    fn=predict,
    inputs=gr.Textbox(lines=3, placeholder="📝 اكتب جملة هنا..."),
    outputs=gr.Textbox(label="🔮 النتائج"),
    title="🧠 مقارنة توقعات نموذجين",
    description="أدخل جملة وشاهد توقع كل نموذج."
)

# 🚀 إطلاق التطبيق
interface.launch(debug=True)
