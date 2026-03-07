from src.app import activities


def test_given_existing_activity_when_signup_then_returns_200_and_adds_participant(client):
    # Given
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"
    assert email not in activities[activity_name]["participants"]

    # When
    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

    # Then
    assert response.status_code == 200
    assert response.json() == {"message": f"Signed up {email} for {activity_name}"}
    assert email in activities[activity_name]["participants"]


def test_given_unknown_activity_when_signup_then_returns_404(client):
    # Given
    activity_name = "Unknown Club"
    email = "student@mergington.edu"

    # When
    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

    # Then
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_given_already_registered_student_when_signup_then_returns_400(client):
    # Given
    activity_name = "Chess Club"
    email = "michael@mergington.edu"

    # When
    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

    # Then
    assert response.status_code == 400
    assert response.json() == {"detail": "Student already signed up for this activity"}


def test_given_missing_email_when_signup_then_returns_422(client):
    # Given
    activity_name = "Chess Club"

    # When
    response = client.post(f"/activities/{activity_name}/signup")

    # Then
    assert response.status_code == 422


def test_given_registered_student_when_unregister_then_returns_200_and_removes_participant(client):
    # Given
    activity_name = "Chess Club"
    email = "michael@mergington.edu"
    assert email in activities[activity_name]["participants"]

    # When
    response = client.delete(
        f"/activities/{activity_name}/participants", params={"email": email}
    )

    # Then
    assert response.status_code == 200
    assert response.json() == {"message": f"Unregistered {email} from {activity_name}"}
    assert email not in activities[activity_name]["participants"]


def test_given_unknown_activity_when_unregister_then_returns_404(client):
    # Given
    activity_name = "Unknown Club"
    email = "student@mergington.edu"

    # When
    response = client.delete(
        f"/activities/{activity_name}/participants", params={"email": email}
    )

    # Then
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_given_non_registered_student_when_unregister_then_returns_404(client):
    # Given
    activity_name = "Chess Club"
    email = "notregistered@mergington.edu"

    # When
    response = client.delete(
        f"/activities/{activity_name}/participants", params={"email": email}
    )

    # Then
    assert response.status_code == 404
    assert response.json() == {"detail": "Student not registered for this activity"}


def test_given_missing_email_when_unregister_then_returns_422(client):
    # Given
    activity_name = "Chess Club"

    # When
    response = client.delete(f"/activities/{activity_name}/participants")

    # Then
    assert response.status_code == 422
