#Степан Яковле, 8-я когорта "Дипломный проект, инженер по тестированию плюс"
import request

# Проверяем создание заказа
def test_order_creation():
    creation_response = request.post_new_order()
    track_id = creation_response.json()['track']
    response = request.get_order_by_track(track_id)
    assert response.status_code == 200