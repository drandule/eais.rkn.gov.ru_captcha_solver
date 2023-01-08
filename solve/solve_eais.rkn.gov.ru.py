import requests
import base64


##Get captcha and save

url_captcha="https://eais.rkn.gov.ru/services/securimage/show/";

headers = {'Accept-Language':'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6,zh;q=0.5','Connection':'keep-alive','Referer':'https://eais.rkn.gov.ru/','Sec-Fetch-Dest':'script','Sec-Fetch-Mode':'no-cors','Sec-Fetch-Site':'same-site','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36','sec-ch-ua':'"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"'};

r = requests.get(url_captcha, headers=headers)

if r.status_code == 200:
    with open("eais.rkn.gov.ru_captcha.png", 'wb') as f:
        f.write(r.content)
        print("Download and save captcha from eais.rkn.gov.ru")

        #solve captcha
        base64_encoded_data = base64.b64encode(r.content)
        base64_message = base64_encoded_data.decode('utf-8')
        #print(base64_message)
        
        json = {"clientKey":"DEMO","task": {
		"type": "ImageToTextTask",
        "subType":"eais",
		"body": base64_message
	    }}
        #print(json)
        url_solve_captcha="http://iamnotbot.com:5000/createTask";         
        r = requests.post(url_solve_captcha, json=json)
        print("Capthca = "+r.text)

else:
    print("Cannot download and save captcha from eais.rkn.gov.ru")         