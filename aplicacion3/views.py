from django.shortcuts import render
from django.http import JsonResponse
from plotly.io import to_json
import plotly.graph_objs as go
import json


def dashboard_data_api(request):
    data1 = go.Scatter(x=[1, 2, 3], y=[4, 1, 2], mode='lines', name='Lineas')
    data2= go.Bar(x=[1, 2, 3], y=[2, 3, 1], name='Barras')
    data3= go.Scatter(x=[1, 2, 3], y=[3, 2, 4], mode='markers', name='Dispersion')
    data4 = go.Pie(labels=['A', 'B', 'C'], values=[4, 3, 2], name='TORTA')
    data5 = go.Histogram(x=[1, 2, 2, 3, 3, 3, 4, 4, 4, 4], name='Histograma')
    data6 = go.Box(y=[1, 2, 3, 4, 5, 6, 7, 8, 9], name='Box')
    
    data = [data1,data2, data3,data4,data5,data6]

    layout = go.Layout(title='My Dashboard', xaxis={'title': 'X'}, yaxis={'title': 'Y'})
    figure = go.Figure(data=data, layout=layout)

    #  a JSON (string)
    graph_jsonstr = to_json(figure)
    # Convertir JSON string a JSON object
    graph_obj = json.loads(graph_jsonstr)


    # JSON a HTTP
    return JsonResponse(graph_obj, safe=False)
