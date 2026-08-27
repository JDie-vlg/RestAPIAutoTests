import pytest
import requests

@pytest.fixture(scope="function")
def session():
    with requests.Session() as s:
        yield s


@pytest.fixture(scope="class")
def base_url():
    return 'https://jsonplaceholder.typicode.com'