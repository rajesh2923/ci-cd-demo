import pytest
from src.app import app

@pytest.fixture
def client():
    return app.test_client()

def test_hello(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, World from Rajesh CI/CD Demo!" in response.data

