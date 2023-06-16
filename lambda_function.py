
import json
import requests

def lambda_handler(event, context):
    print(event)
    try:
        body=json.loads(event['body'])
        
        print(body)
        
        
        message_part=body['message'].get('text')
        print("Message part : {}".format(message_part))
        
        #data = {'url': message_part}
        if(message_part == "1"):
            #payload=requests.post('https://cleanuri.com/api/v1/shorten',...)
            #short_url=payload.json()['result_url']
            #print("The short url is : {}".format(short_url))
            
            #chat_id=body['message']['chat']['id']
            
            #url = f'https://api.telegram.org//sendMessage'
            #payload = {
            #            'chat_id': chat_id,
            #            'text': short_url
             #           }
           
            #r = requests.post(url,json=payload)
            bot_token = ''
            chat_id = ''
            message_text = '1 is selected. Attend'
            url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
            params = {
                'chat_id': chat_id,
                'text': message_text
            }
    
            response = requests.post(url, params=params)
            return  {
                "statusCode": 200
            }
        elif (message_part == "2"):
        #payload=requests.post('https://cleanuri.com/api/v1/shorten',...)
        #short_url=payload.json()['result_url']
        #print("The short url is : {}".format(short_url))
        
        #chat_id=body['message']['chat']['id']
            #payload=requests.post('https://cleanuri.com/api/v1/shorten',...)
            #short_url=payload.json()['result_url']
            #print("The short url is : {}".format(short_url))
            
            #chat_id=body['message']['chat']['id']
            
            #url = f'https://api.telegram.org/bot6k32oC0E/sendMessage'
            #payload = {
            #            'chat_id': chat_id,
            #            'text': short_url
             #           }
           
            #r = requests.post(url,json=payload)
            bot_token = ''
            chat_id = ''
            message_text = '2 is selected not attend'
            
            url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
            params = {
                'chat_id': chat_id,
                'text': message_text
            }
    
            response = requests.post(url, params=params)
            return  {
                "statusCode": 200
            }      

        else:
            #payload=requests.post('https://cleanuri.com/api/v1/shorten',...)
            #short_url=payload.json()['result_url']
            #print("The short url is : {}".format(short_url))
            
            #chat_id=body['message']['chat']['id']
            
            #url = f'https://api.telegram.org//sendMessage'
            #payload = {
            #            'chat_id': chat_id,
            #            'text': short_url
             #           }
           
            #r = requests.post(url,json=payload)
            bot_token = ''
            chat_id = ''
            message_text = '''
            ⠄⠄⠄⠄⠄⠄⢴⡶⣶⣶⣶⡒⣶⣶⣖⠢⡄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
            ⠄⠄⠄⠄⠄⠄⢠⣿⣋⣿⣿⣉⣿⣿⣯⣧⡰⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
            ⠄⠄⠄⠄⠄⠄⣿⣿⣹⣿⣿⣏⣿⣿⡗⣿⣿⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
            ⠄⠄⠄⠄⠄⠄⠟⡛⣉⣭⣭⣭⠌⠛⡻⢿⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
            ⠄⠄⠄⠄⠄⠄⠄⠄⣤⡌⣿⣷⣯⣭⣿⡆⣈⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
            ⠄⠄⠄⠄⠄⠄⠄⢻⣿⣿⣿⣿⣿⣿⣿⣷⢛⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
            ⠄⠄⠄⠄⠄⠄⠄⠄⢻⣷⣽⣿⣿⣿⢿⠃⣼⣧⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄
            ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣛⣻⣿⠟⣀⡜⣻⢿⣿⣿⣶⣤⡀⠄⠄⠄⠄⠄
            ⠄⠄⠄⠄⠄⠄⠄⠄⢠⣤⣀⣨⣥⣾⢟⣧⣿⠸⣿⣿⣿⣿⣿⣤⡀⠄⠄⠄
            ⠄⠄⠄⠄⠄⠄⠄⠄⢟⣫⣯⡻⣋⣵⣟⡼⣛⠴⣫⣭⣽⣿⣷⣭⡻⣦⡀⠄
            ⠄⠄⠄⠄⠄⠄⠄⢰⣿⣿⣿⢏⣽⣿⢋⣾⡟⢺⣿⣿⣿⣿⣿⣿⣷⢹⣷⠄
            ⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⢣⣿⣿⣿⢸⣿⡇⣾⣿⠏⠉⣿⣿⣿⡇⣿⣿⡆
            ⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⢸⣿⣿⣿⠸⣿⡇⣿⣿⡆⣼⣿⣿⣿⡇⣿⣿⡇
            ⠇⢀⠄⠄⠄⠄⠄⠘⣿⣿⡘⣿⣿⣷⢀⣿⣷⣿⣿⡿⠿⢿⣿⣿⡇⣩⣿⡇
            ⣿⣿⠃⠄⠄⠄⠄⠄⠄⢻⣷⠙⠛⠋⣿⣿⣿⣿⣿⣷⣶⣿⣿⣿⡇⣿⣿⡇
            '''
            
            url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
            params = {
                'chat_id': chat_id,
                'text': message_text
            }
    
            response = requests.post(url, params=params)
            return  {
                "statusCode": 200
            }
    except:
        return  {
        "statusCode": 200
    }        
