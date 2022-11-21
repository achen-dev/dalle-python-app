import os
from PIL import Image
import openai
from flask import Flask, redirect, render_template, request, url_for
import requests

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")
img_num = 9


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        img_prompt = request.form["animal"]
        response = openai.Image.create(
            prompt=img_prompt,
            n=img_num,
            size="256x256",
        )
        image_url_list = []
        for i in range(img_num):
            image_url = response['data'][i]['url']
            image_url_list.append(image_url)
            im = Image.open(requests.get(image_url, stream=True).raw)
            im.save("genimages/" + img_prompt + str(i) +".png")
        print(image_url_list)
        return redirect(url_for("index", result0=image_url_list[0],
                                result1=image_url_list[1],
                                result2=image_url_list[2],
                                result3=image_url_list[3],
                                result4=image_url_list[4],
                                result5=image_url_list[5],
                                result6=image_url_list[6],
                                result7=image_url_list[7],
                                result8=image_url_list[8],
                                ))

    result0 = request.args.get("result0")
    result1 = request.args.get("result1")
    result2 = request.args.get("result2")
    result3 = request.args.get("result3")
    result4 = request.args.get("result4")
    result5 = request.args.get("result5")
    result6 = request.args.get("result6")
    result7 = request.args.get("result7")
    result8 = request.args.get("result8")
    return render_template("index.html",
                           result0=result0,
                           result1=result1,
                           result2=result2,
                           result3=result3,
                           result4=result4,
                           result5=result5,
                           result6=result6,
                           result7=result7,
                           result8=result8,)

