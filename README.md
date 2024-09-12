## 项目名称：音频转录工具

### 项目简介
这是一个简单的音频转录和翻译工具，使用了 OpenAI 的 Whisper 模型来自动识别音频中的语言并将其转录为文本。转录的文本随后会被翻译为中文并保存到同一目录下。该工具通过一个图形用户界面（GUI）实现，用户可以轻松选择音频文件进行处理。

### 功能：
1. 自动识别音频中的语言并转录为文本。
2. 将转录的文本翻译为中文。
3. 支持常见的音频格式（如 `.wav`, `.mp3`, `.m4a`, `.mp4`）。
4. 生成的文本文件与音频文件保存在同一目录下。
5. 提供图形用户界面，用户操作简便。

---

### 使用指南

#### 1. 配置环境
在使用该工具前，请确保系统已正确安装并配置了以下内容：

- **FFmpeg**：
  - Whisper 需要依赖 FFmpeg 来处理音频文件。请确保你已经下载并配置了 FFmpeg。
  - 下载地址：[FFmpeg 官方网站](https://ffmpeg.org/download.html)
  - 将 FFmpeg 的 `bin` 目录添加到系统的 `PATH` 环境变量中。

  **配置环境变量**：
  - Windows 下，右键 "此电脑" -> "属性" -> "高级系统设置" -> "环境变量"，找到系统变量中的 `Path`，点击编辑，添加 FFmpeg 的 `bin` 路径，例如：`C:\ffmpeg\bin`。

  **验证 FFmpeg 安装**：
  打开命令提示符 (cmd)，输入以下命令，检查 FFmpeg 是否已正确安装：
  ```bash
  ffmpeg -version
  ```
  
### Python 环境：

1.   推荐使用 Python 3.10 或更高版本。 如果使用源码，请创建虚拟环境并安装必要的依赖：

     ```bash
     pip install -r requirements.txt
     ```

2. 使用打包的可执行文件
在 dist 目录下，你可以找到一个打包好的可执行文件（.exe）。双击运行该文件，无需安装 Python 环境或手动配置依赖。
3. 运行项目
如果你选择使用源码运行：

    克隆项目或下载源码后，在项目根目录下运行以下命令来启动：
    ```bash
    python transcribe.py
    ```
    运行后，系统将弹出一个 GUI 窗口，提示你选择一个音频文件。选择文件后，程序会自动转录并翻译音频文件，并将生成的文本文件保存到音频文件的同一目录中。

## 注意事项:

1. FFmpeg 配置： 请确保 FFmpeg 已正确安装并添加到系统 PATH 环境变量中，程序才能正常处理音频文件。
2. 虚拟环境： 如果使用源码运行，请确保你已在虚拟环境中安装了所有依赖。建议运行以下命令来创建虚拟环境并安装依赖：
    ```bash
    python -m venv .venv
    .venv\Scripts\activate
    pip install -r requirements.txt
    ```
3. 打包成可执行文件： 如果你需要重新打包该项目为可执行文件，请运行以下命令：
    ```bash
    pyinstaller --onefile --windowed transcribe.py
    ```
### 依赖列表
* Whisper (OpenAI)
* FFmpeg
* googletrans==4.0.0-rc1
* tkinter (Python 标准库)