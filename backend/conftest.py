import pytest
import requests

@pytest.fixture(scope="module")
def base_url():
    base_url = "https://discord.com/api/v10"
    return base_url

@pytest.fixture(scope="module")
def channel_id():
    channel_id = 1286673511733268552
    return channel_id

@pytest.fixture(scope="module")
def headers():
    api_key = "MTI4NjYwOTgxOTEzNzk5ODg4Mw.G0Fflc.xDvykECWDsrG8htMuEj9KYG0lUdx_XweIdzOsE"
    return {
        "Authorization": f"Bot {api_key}",
        "Content-Type": "application/json"
    }

@pytest.fixture(scope='module', autouse=True)
def message_id (base_url, channel_id, headers):
    # Создание сообщения перед каждым тестом
    url = f"{base_url}/channels/{channel_id}/messages"
    data = {
        "content": "Привет я тестовое сообщение, я скоро удалюсь "
    }
    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    message_id = response.json().get('id')

    yield message_id

    delete_url = f"{base_url}/channels/{channel_id}/messages/{message_id}"
    response = requests.delete(delete_url, headers=headers)
    assert response.status_code == 204
