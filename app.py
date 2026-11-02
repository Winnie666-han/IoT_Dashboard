"""课程示例：模拟温湿度监控与目标温度设置。"""
import math
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
target_temperature = None


def get_latest_data():
    # 与教程一致，使用模拟数据，尚未连接真实传感器。
    return 25.0, 60.0


def render_dashboard(error=None, status=200):
    temperature, humidity = get_latest_data()
    return render_template(
        'index.html', temperature=temperature, humidity=humidity,
        target_temperature=target_temperature, error=error,
        saved=request.args.get('saved') == '1',
    ), status


@app.route('/')
def index():
    return render_dashboard()


@app.route('/set-temperature', methods=['POST'])
def set_temperature():
    global target_temperature
    try:
        value = float(request.form.get('target_temperature', ''))
        if not math.isfinite(value):
            raise ValueError
    except (ValueError, TypeError):
        return render_dashboard('请输入有效的目标温度。', 400)
    target_temperature = value
    return redirect(url_for('index', saved=1))


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=os.environ.get('FLASK_DEBUG') == '1')
