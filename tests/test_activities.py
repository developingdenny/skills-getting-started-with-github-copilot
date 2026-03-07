def test_given_default_data_when_get_activities_then_returns_activity_dictionary(client):
    # Given

    # When
    response = client.get("/activities")
    body = response.json()

    # Then
    assert response.status_code == 200
    assert isinstance(body, dict)
    assert "Chess Club" in body
    assert "participants" in body["Chess Club"]
    assert isinstance(body["Chess Club"]["participants"], list)
