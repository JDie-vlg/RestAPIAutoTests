import pytest

class TestPosts:

    def test_get_all_posts(self, session, base_url):
        """GET /posts - получение всех постов"""
        response = session.get(f'{base_url}/posts')
        assert response.status_code == 200, "должно быть 200"
        data = response.json()

        assert isinstance(data, list)

        assert len(data) > 0

        for post in data:
            assert "userId" in post, "Отсутствует userId"
            assert "id" in post, "Отсутствует id"
            assert "title" in post, "Отсутствует title"
            assert "body" in post, "Отсутствует body"


    @pytest.mark.parametrize("post_id", [1,2,3])
    def test_get_post_by_id(self, session, base_url, post_id):
        """Параметризированный тест GET /posts/{id} для получение нескольких постов по ID"""
        response = session.get(f'{base_url}/posts/{post_id}')
        assert response.status_code == 200, "должно быть 200"

        data = response.json()

        assert data['id'] == post_id, f"ID ({data['id']}) не соответствует запрошенному ({post_id})"
        assert "userId" in data
        assert "title" in data
        assert "body" in data

    def test_create_post(self, session, base_url):
        """GET /posts - создание нового поста"""
        new_post = {
            "userId": 1,
            "title": "foo",
            "body": "bar"
        }

        response = session.post(f'{base_url}/posts', json=new_post, timeout=15)
        assert response.status_code == 201, "должно быть 201"
        data = response.json()

        assert data["userId"] == new_post["userId"], "userId не совпадает"
        assert data['title'] == new_post['title'], 'title не совпадает'
        assert data['body'] == new_post['body'], 'body не совпадает'

        assert data['id'] == 101, "ID должно быть 101"

        assert set(data.keys()) == {'userId', 'id', 'title', 'body'}

    def test_update_post(self, session, base_url):
        """PUT /posts - обновление существующего поста"""
        updated_post = {
            'id': 1,
            'userId': 1,
            'title': 'updated title',
            'body': 'updated body',
        }

        response = session.put(f'{base_url}/posts/1', json=updated_post)
        assert response.status_code == 200, "должно быть 200"

        data = response.json()

        assert data['id'] == updated_post['id'], "ID не совпадает"
        assert data['title'] == updated_post['title'], "title не обновился"
        assert data['body'] == updated_post['body'], "body не обновился"

        assert 'userId' in data

    def test_delete_post(self, session, base_url):
        """PUT /posts/{id} - удаление поста"""
        response = session.delete(f'{base_url}/posts/1')
        assert response.status_code == 200, "должно быть 200"

        assert response.text == "{}"

    def test_get_nonexistent_post(self, session, base_url):
        """Негативный тест: GET /posts/{id} с несуществующим ID"""
        response = session.get(f'{base_url}/posts/999')
        assert response.status_code == 404, "должно быть 404"