# Проект автоматизации тестирования REST API (JSONPlaceholder)

## Описание

Данный проект содержит набор автотестов на Python с использованием `pytest` и `requests` для проверки базовых CRUD-операций (GET, POST, PUT, DELETE) над ресурсом `/posts` публичного API [JSONPlaceholder](https://jsonplaceholder.typicode.com/).

Тесты покрывают:
- Получение списка всех постов.
- Получение поста по ID (параметризовано 3 значениями).
- Создание нового поста.
- Обновление существующего поста.
- Удаление поста.
- Негативный сценарий (запрос несуществующего поста).

Тесты идемпотентны, не зависят от порядка выполнения и стабильно проходят при запуске всех тестов вместе.

## Установка и запуск

1. Клонируйте репозиторий.
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
3. Запустите тесты:
   ```pytest tests/ -v``` \
   Для детального вывода используйте 
   ```pytest tests/ -v -s```

## Структура проекта
tests/ – директория с тестами.

conftest.py – фикстуры: session (новая сессия для каждого теста) и base_url.

test_posts.py – тесты для эндпоинта /posts.

requirements.txt – зависимости.

README.md – описание проекта.

.gitignore – игнорируемые файлы.

## Пример ожидаемого вывода

tests/test_posts.py::TestPosts::test_get_all_posts PASSED
tests/test_posts.py::TestPosts::test_get_post_by_id[1] PASSED
tests/test_posts.py::TestPosts::test_get_post_by_id[2] PASSED
tests/test_posts.py::TestPosts::test_get_post_by_id[3] PASSED
tests/test_posts.py::TestPosts::test_create_post PASSED
tests/test_posts.py::TestPosts::test_update_post PASSED
tests/test_posts.py::TestPosts::test_delete_post PASSED
tests/test_posts.py::TestPosts::test_get_nonexistent_post PASSED

### Примечания
Фикстура сессии имеет scope='function', чтобы избежать проблем с переиспользованием соединения, которые приводили к таймаутам при запуске всех тестов последовательно.