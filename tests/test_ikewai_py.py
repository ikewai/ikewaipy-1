from ikewaipy import __version__
from ikewaipy.ikewai import Ikewai
import pytest

def test_version():
    assert __version__ == '0.1.0'

@pytest.fixture
def client():
    endpoint = 'https://ikeauth.its.hawaii.edu'
    token_url = 'https://ikewai.its.hawaii.edu:8888/login'
    token = ''
    username = 'guest'
    password = 'guest'
    ike = Ikewai(endpoint=endpoint,
              token_url=token_url,
              token=token,
              username=username
              )
    ike.login();
    return ike



def testSearchMetadata(client):
    print(client.searchMetadata("{'name':'Variable','value.variable_name':'Temperature'}", 1))
