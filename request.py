import configuration
import data
import requests

#Создаем заказ
def post_new_order():
    return requests.post(configuration.URL_SERVISE + configuration.CREATE_NEW_ORDER,  # url
                         json=data.order_body, #тело
                         headers=data.headers)

# Получаем заказ по трек номеру
def get_order_by_track(track_id):
    return requests.get(configuration.URL_SERVISE + configuration.FIND_ORDER_BY_ID + str(track_id),
                        headers = data.headers)