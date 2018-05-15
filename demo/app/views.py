from django.shortcuts import render
from keras.models import load_model
from PIL import Image
import numpy as np

import tensorflow as tf

graph = tf.get_default_graph()

model = load_model('./model.h5')


# Create your views here.

def index(request):
    result = ''
    if request.POST:
        image = request.FILES['file']
        with open('dd.png', "wb+") as destination:
            for chunk in image.chunks():
                destination.write(chunk)
        arr = np.array(Image.open('./dd.png').convert('L'))
        arr.resize([28, 28, 1])
        global graph
        with graph.as_default():
            result = '预测结果：{}'.format(np.argmax(model.predict(np.array([arr]))))

    return render(request, 'index.html', {'result': result})
