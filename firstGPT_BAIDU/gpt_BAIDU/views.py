# -*- coding: utf8 -*-

from django.http import JsonResponse
from django.shortcuts import render
import qianfan


# 百度千帆大模型API,替换为 API和对应的KEY
API_KEY = 'xxxxxxxxxxxxxxxx'
SECRET_KEY = 'xxxxxxxxxxxxxxxx'
MODEL_NAME = "ERNIE-4.0-8K"
chatbot = qianfan.ChatCompletion(ak=API_KEY, sk=SECRET_KEY)

modelList = ["ERNIE-4.0-8K","ERNIE-3.5-8K","ERNIE-Speed-128K","ERNIE Speed-AppBuilder","ERNIE-Character-8K","ERNIE-Functions-8K","ERNIE-Lite-8K","Qianfan-Chinese-Llama-2-7B"]
# 用来存储历史问答信息
messages = [{"role":'user','content':'记住你现在的中文和英文名字都叫BOT'},{"role":'assistant','content':'好的，在后面的对话中我会称呼自己为BOT'}]
def gpt(request):
    print(messages)
    # 用户和助手对话信息
    singleUserMesg = {"role": 'user', "content":0}
    singleAssistantMesg  = {"role": 'assistant', "content":0}
    if request.method == 'GET':
        return render(request, 'gpt.html')
    if request.method == 'POST':
        userMeg = request.POST.get('userMesg','')
        modelName = request.POST.get('modelName','')
        if modelName != "":
            MODEL_NAME = modelName

        singleUserMesg['content'] = userMeg

        messages.append(singleUserMesg)

        resp = chatbot.do(model=MODEL_NAME, messages = messages)
        result = resp["body"]["result"]

        singleAssistantMesg['content'] = result
        messages.append(singleAssistantMesg)

        responseData = {
            'result': result,
        }
        print("MODEL_NAME: ",MODEL_NAME)
        print("userMeg: ",userMeg)
        print("response: ",result)
        return JsonResponse(responseData)
