from django.shortcuts import render
# Create your views here.
def main(request):
    return render(request, 'Dota2Predictor/main.html')

# Usually the methods and logic should be separated, but for this project I won't be that detailed.

def predictTheGame(hero, skill, role, lane, type, mode, kda, length):
    import pickle

    model = pickle.load(open("C:/Users/krist/Desktop/University 2021/djangoProject/Dota2Predictor/knn.sav", "rb"))
    encoder = pickle.load(open("C:/Users/krist/Desktop/University 2021/djangoProject/Dota2Predictor/hotencoder.sav", "rb"))
    labels = encoder.transform([[hero, skill, role, lane, type, mode, kda, length]])
    print(encoder.get_params())
    prediction = model.predict(labels)

    if prediction[0] == "Win":
        return "Victory"
    elif prediction[0] == "Loss":
        return "Defeat"


def result(request):
    try:
        skill = request.POST['skill']
        role = request.POST['role']
        lane = request.POST['lane']
        type = request.POST['type']
        mode = request.POST['mode']
        hero = request.POST['hero']
        kda = int(request.POST['kda'])
        length = int(request.POST['length'])

        result = predictTheGame(hero, skill, role, lane, type, mode, kda, length)

        return render(request, 'Dota2Predictor/result.html', {'result': result})
    except:
        return render(request, 'Dota2Predictor/result.html', {'result': 'None'})
