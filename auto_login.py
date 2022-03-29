import requests

def is_connect():
    try:
        res = requests.get('http://10.255.0.19/', timeout=2).headers['Content-Length']
        return True if res == '3205' else False
    except:
        return True

# 2:电信  4:移动
# '2_学号' : '密码'    为电信号
# '4_学号' : '密码'    为移动号
accounts = {
    '2_**********' : "*******",
    '4_**********' : "*******"
}


for ac, ps in accounts.items():
    mode = 'aust' if ac.split('_')[0] == "2" else 'cmcc'  # 2：电信 4：移动
    url = f"http://10.255.0.19/drcom/login?callback=dr1003&DDDDD={ ac.split('_')[1] }%40{mode}&upass={ ps }&0MKKey=123456&R1=0&R3=0&R6=0&para=00"
    if not is_connect():
        requests.get(url)
    else:
        print("Successed")
        break
    print("Failed")