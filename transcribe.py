import tkinter as tk
from tkinter import filedialog, messagebox
import whisper
import os
from googletrans import Translator  # 导入翻译库

# 加载 Whisper 模型，base 模型较小，适合一般使用
model = whisper.load_model("base")

# 初始化翻译器
translator = Translator()


# 定义转录并翻译音频文件的函数
def transcribe_file(file_path):
    # 检查文件是否存在
    if not os.path.isfile(file_path):
        messagebox.showerror("错误", f"文件 {file_path} 不存在")
        return

    # 自动识别语言并转录音频
    result = model.transcribe(file_path)  # 不指定语言，Whisper 会自动检测语言

    # 获取原始的转录文本
    original_text = result["text"]

    # 翻译文本到中文
    translated_text = translator.translate(original_text, dest="zh-cn").text  # 将转录的文本翻译成中文

    # 为了改善阅读体验，自动在句号后换行
    formatted_text = original_text.replace(". ", ".\n")

    # 获取文件所在目录和文件名
    directory = os.path.dirname(file_path)
    filename = os.path.basename(file_path).split('.')[0]

    # 保存原文和翻译文本到同目录下的文本文件
    output_file_original = os.path.join(directory, f"{filename}_transcription.txt")
    output_file_translated = os.path.join(directory, f"{filename}_transcription_translated.txt")

    # 保存提取的原文
    with open(output_file_original, 'w', encoding='utf-8') as f:
        f.write(formatted_text)

    # 保存翻译的文本
    with open(output_file_translated, 'w', encoding='utf-8') as f:
        f.write(translated_text)

    # 弹出提示，告知用户转录和翻译完成
    messagebox.showinfo("完成", f"转录和翻译完成，结果保存在 {output_file_original} 和 {output_file_translated}")


# 定义文件选择函数
def open_file():
    # 打开文件选择对话框，允许用户选择音频文件
    file_path = filedialog.askopenfilename(
        title="选择音频文件",
        filetypes=[("音频文件", "*.wav *.mp3 *.m4a *.mp4")]  # 只允许选择常见音频格式
    )
    # 如果用户选择了文件，开始转录和翻译
    if file_path:
        transcribe_file(file_path)


# 创建主窗口
root = tk.Tk()  # 初始化 Tkinter 主窗口
root.title("音频转录和翻译工具")  # 设置窗口标题
root.geometry("400x200")  # 设置窗口大小

# 标签，用于提示用户操作
label = tk.Label(root, text="请选择音频文件进行转录和翻译", font=("Arial", 14))
label.pack(pady=20)  # 使用 pack 布局，设置上下内边距

# 按钮，用于打开文件选择对话框
open_button = tk.Button(root, text="选择文件", command=open_file, font=("Arial", 12))
open_button.pack(pady=10)  # 设置按钮下方的内边距

# 启动 Tkinter 主循环，等待用户操作
root.mainloop()
