from django.shortcuts import render
import plotly.graph_objs as go

def dashboard(request):
    data1 = go.Scatter(x=[1, 2, 3], y=[4, 1, 2], mode='lines', name='Lineas')
    data2 = go.Bar(x=[1, 2, 3], y=[2, 3, 1], name='Barras')
    data3 = go.Scatter(x=[1, 2, 3], y=[3, 2, 4], mode='markers', name='Dispersion')
    data4 = go.Pie(labels=['A', 'B', 'C'], values=[4, 3, 2], name='TORTA')
    data5 = go.Histogram(x=[1, 2, 2, 3, 3, 3, 4, 4, 4, 4], name='Histograma')
    data6 = go.Box(y=[1, 2, 3, 4, 5, 6, 7, 8, 9], name='Box')

    graph1 = go.Figure(data=data1, layout=go.Layout(title='Lineas', xaxis={'title': 'X'}, yaxis={'title': 'Y'}))
    graph2 = go.Figure(data=data2, layout=go.Layout(title='Barras', xaxis={'title': 'X'}, yaxis={'title': 'Y'}))
    graph3 = go.Figure(data=data3, layout=go.Layout(title='Dispersion', xaxis={'title': 'X'}, yaxis={'title': 'Y'}))
    graph4 = go.Figure(data=data4, layout=go.Layout(title='TORTA'))
    graph5 = go.Figure(data=data5, layout=go.Layout(title='Histograma', xaxis={'title': 'X'}, yaxis={'title': 'Frequency'}))
    graph6 = go.Figure(data=data6, layout=go.Layout(title='Box', yaxis={'title': 'Value'}))

    graph1_json = graph1.to_json()
    graph2_json = graph2.to_json()
    graph3_json = graph3.to_json()
    graph4_json = graph4.to_json()
    graph5_json = graph5.to_json()
    graph6_json = graph6.to_json()

    return render(request, 'dashboard.html', {'graph1_json': graph1_json, 'graph2_json': graph2_json,
                                              'graph3_json': graph3_json, 'graph4_json': graph4_json,
                                              'graph5_json': graph5_json, 'graph6_json': graph6_json})
