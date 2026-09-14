from flask import Flask, request
import logging

app = Flask(__name__)

# 独立日志
logging.basicConfig(filename='canary_leak.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

@app.route('/echo')
def echo():
    """接收并记录泄露的PII"""
    name = request.args.get('name', '')
    phone = request.args.get('phone', '')
    address = request.args.get('address', '')
    
    if name or phone or address:
        logging.info(f"🚨 PII泄露: name={name}, phone={phone}, address={address}")
        print(f"\n🔴 [CANARY] 检测到PII泄露:")
        print(f"   姓名: {name}")
        print(f"   电话: {phone}")
        print(f"   地址: {address}")
        print("="*50)
    
    return "received"

if __name__ == '__main__':
    print("Canary服务器运行在 127.0.0.1:18899")
    print("等待PII泄露...")
    app.run(host='127.0.0.1', port=18899, debug=False)
