def test_given_root_route_when_requested_then_redirects_to_static_index(client):
    # Given

    # When
    response = client.get("/", follow_redirects=False)

    # Then
    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"
