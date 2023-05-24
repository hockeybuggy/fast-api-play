from unittest.mock import patch

from fastapi import Response
from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_root_redirects():
    response = client.get("/")

    assert len(response.history) == 1
    assert response.history[0].status_code == 307


@patch("fast_api_playground.main.get_current_timestamp")
def test_ping_returns_time(get_current_timestamp_mock):
    expected_fake_time = 1684936317
    get_current_timestamp_mock.return_value = expected_fake_time

    response = client.get("/ping")

    assert response.status_code == 200
    assert response.json() == {"pong": expected_fake_time}
