import urllib
import json


# Geoinformation service base URL
GIS_BASE = "https://www.gis.nrw.de/"
GIS_REST_BASE = "https://www.gis-rest.nrw.de/bkg/gdz_ortssuche/"


def suggest_address(address_string):
    req_param = {'outputformat': 'json',
                 'count': '5',
                 'filter': 'bundesland:Nordrhein-Westfalen',
                 'query': str(address_string)}
    req_url = GIS_REST_BASE + "suggest?" + urllib.urlencode(req_param)
    json_response = urllib.urlopen(req_url)
    data = json.loads(json_response.read())
    return data


def address_info(address_string):
    req_param = {'outputformat': 'json',
                 'count': '1',
                 'filter': 'bundesland:Nordrhein-Westfalen',
                 'srsName': 'EPSG:25832',
                 'query': address_string}
    req_url = GIS_REST_BASE + "geosearch?" + urllib.urlencode(req_param)
    json_response = urllib.urlopen(req_url)
    data = json.loads(json_response.read())
    info = data['features'][0]
    return info


def bodenrichtwert(x, y, year):
    bbox_margin = 1000
    req_param = {'f': 'json',
                 'tolerance': '0',
                 'returnGeometry': 'false',
                 'imageDisplay': '96',
                 'geometryType': 'esriGeometryPoint',
                 'geometry': '{"x":' + str(x) + ',"y":' + str(y) + '}',
                 'mapExtent': str(x - bbox_margin) + ',' + str(y - bbox_margin) + ',' + str(
                     x + bbox_margin) + ',' + str(y + bbox_margin)
                 }
    req_url = GIS_BASE + 'arcgis/rest/services/mik_borisplus/BORISplus_Bodenrichtwerte_' + str(
        year) + '_zonal/MapServer/identify?' + urllib.urlencode(req_param)
    json_response = urllib.urlopen(req_url)
    data = json.loads(json_response.read())
    brw = data['results'][0]['attributes']['BRW']
    return brw


def immobilienrichtwert():
    return


def bodenrichtwert_by_address(address, year):
    address_suggestion = suggest_address(address)[0]['suggestion']
    address_inf = address_info(address_suggestion)
    adress_x = address_inf['properties']['bbox']['coordinates'][0]
    adress_y = address_inf['properties']['bbox']['coordinates'][1]
    return bodenrichtwert(adress_x, adress_y, year)
