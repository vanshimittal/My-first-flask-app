import app

def test_hello_world():
    response=app.app.test_client().get("/hello")
    assert response.status_code==200
    assert response.data==b'Hello'

def test_age():
    response=app.app.test_client().get("/goodbye")
    assert response.status_code==200
    assert response.data==b'Rahul'

def test_name():
    response=app.app.test_client().get("/name")
    assert response.status_code==200
    assert response.data==b'Rahul'

def test_age():
    response=app.app.test_client().get("/age")
    assert response.status_code==200
    assert response.data==b'43'