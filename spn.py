def get_spn(data):
    toponym = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['boundedBy']['Envelope']
    lowerCorner = list(map(float, toponym['lowerCorner'].split()))
    upperCorner = list(map(float, toponym['upperCorner'].split()))
    return f'{abs(lowerCorner[0] - upperCorner[0])},{abs(lowerCorner[1] - upperCorner[1])}'