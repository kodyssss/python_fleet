from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# static 文件夹与 web_demo.py 同级
STATIC_DIR = 'static'

# 读取版本号
VERSION = "v1.0.7"

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(STATIC_DIR, filename)

@app.route('/')
def hello():
    return '''
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>我们是 SUSE</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                font-family: 'Arial', sans-serif;
                background: linear-gradient(to bottom, #003087, #00695c);
                min-height: 100vh;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                color: #ffffff;
            }
            .container {
                text-align: center;
                padding: 20px;
                background-color: rgba(255, 255, 255, 0.1);
                border-radius: 15px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
                max-width: 90%;
            }
            h1 {
                font-size: 2.5em;
                margin: 10px 0;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            }
            h1:nth-child(2) {
                font-size: 1.8em;
                font-weight: normal;
            }
            .image-container {
                margin-top: 20px;
                padding: 10px;
                background-color: #ffffff;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                max-width: 100%;
            }
            img {
                max-width: 100%;
                border-radius: 5px;
                transition: transform 0.3s ease-in-out;
            }
            img:hover {
                transform: scale(1.05);
            }
            .footer {
                position: fixed;
                bottom: 10px;
                color: #ffffff;
                font-size: 0.9em;
                opacity: 0.8;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>我们是 SUSE. (版本: ''' + VERSION + ''')</h1>
            <h1>我们坚信，我们将创造一个安全、开源创新的未来。</h1>
            <div class="image-container">
                <img src="/static/suse.jpg" alt="SUSE Image">
            </div>
        </div>
        <div class="footer">
            Powered by Flask & Docker | © 2025 SUSE China Team
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(port=5001, host='0.0.0.0', debug=True)
