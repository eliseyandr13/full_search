import requests
import pygame
import sys
import os
import spn


def get_response_from_given(toponym_to_find):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"
    }
    return requests.get(geocoder_api_server, params=geocoder_params)


def check_if_not_response(response):
    if not response:
        print("Ошибка выполнения запроса:")
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)


def request_on_image(spn, geocode):
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    map_params = {
        "ll": geocode,
        "spn": spn,
        "l": "map",
        "pt": f"{geocode.split(",")[0]},{geocode.split(",")[-1]},pm2dgl"
    }
    return requests.get(map_api_server, params=map_params)


def pygame_image_show(map_file):
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()

    os.remove(map_file)


coords = "37.617698,55.755864"

response = get_response_from_given(coords)
check_if_not_response(response)

data = response.json()
spn = spn.get_spn(data)
response = request_on_image(spn, coords)
check_if_not_response(response)

map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

pygame_image_show(map_file) 
