# IoT Dashboard 温湿度控制台

按照课程 Flask 简明教程完成的网页 Demo。

## 功能
- 显示模拟温度 25.0 ℃、湿度 60.0%。
- 通过 POST 表单设置目标温度，提交后重定向回首页并显示结果。
- 对空值、非数字和非有限数值进行校验。

## 本地运行
建议 Python 3.9 或以上版本。在项目目录执行：

```bash
python -m pip install -r requirements.txt
python app.py
```

浏览器访问 http://127.0.0.1:5001 。使用安装 Flask 的同一个 Python 运行程序；Miniforge 用户可以使用 `/Users/zhangyuhan/miniforge3/bin/python`。

默认使用 5001，避免 macOS 的 5000 端口冲突。如有需要：

```bash
PORT=5002 python app.py
```

## Render 部署（可选）
- Runtime: Python 3
- Build Command: `pip install -r requirements.txt`
- Start Command: `python app.py`
- 程序读取 Render 提供的 PORT，监听 0.0.0.0。

本项目为课程演示，使用 Flask 内置服务器。目标温度仅保存在单进程内存，重启清空；尚未连接 MQTT、传感器或真实控制设备，不用于生产环境。

## 提交材料
项目代码压缩包，以及本地运行截图（作业允许本地截图或 Render 部署截图）。截图展示初始页面和设置 26.5 ℃后的结果。

## 参考
https://www.wolai.com/a7b4MTo2WTmw5igsip3kx3
