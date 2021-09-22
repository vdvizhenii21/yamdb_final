# API_YamDB

REST API для сервиса YaMDb — базы отзывов о фильмах, книгах и музыке.

Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Произведению может быть присвоен жанр. Новые жанры может создавать только администратор. Читатели оставляют к произведениям текстовые отзывы и выставляют произведению рейтинг (оценку в диапазоне от одного до десяти). Из множества оценок автоматически высчитывается средняя оценка произведения.

Аутентификация по JWT-токену

Поддерживает методы GET, POST, PUT, PATCH, DELETE

Предоставляет данные в формате JSON

Cоздан в команде из трёх человек с использованим Git в рамках учебного курса Яндекс.Практикум.
# Стек технологий
- проект написан на Python с использованием Django REST Framework
- библиотека Simple JWT - работа с JWT-токеном
- библиотека django-filter - фильтрация запросов
- базы данны - SQLite3 и PostgreSQL
- автоматическое развертывание проекта - Docker, docker-compose
- система управления версиями - git


## Как запустить проект, используя Docker (база данных PostgreSQL):

1. С помощью Dockerfile и docker-compose.yaml разверните проект:
```sh 
docker-compose up --build
```
2. В новом окне терминала узнайте id контейнера yamdb_web и войдите в контейнер:
```sh
docker container ls
```
docker exec -it <CONTAINER_ID> bash
3. В контейнере выполните миграции, создайте суперпользователя и заполните базу начальными данными:
```sh 
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata fixtures.json
```

Ваш проект запустился на http://0.0.0.0:8000/

Полная документация (redoc.yaml) доступна по адресу http://0.0.0.0:8000/redoc/

Вы можете запустить тесты и проверить работу модулей:

```sh 
docker exec -ti <container_id> pytest
```

## Алгоритм регистрации пользователей:
- Пользователь отправляет запрос с параметрами email и username на /auth/email/.
- YaMDB отправляет письмо с кодом подтверждения (confirmation_code) на адрес email .
- Пользователь отправляет запрос с параметрами email и confirmation_code на /auth/token/, в ответе на запрос ему приходит token (JWT-токен).

## Ресурсы API YaMDb:
- Ресурс AUTH: аутентификация.
- Ресурс USERS: пользователи.
- Ресурс TITLES: произведения, к которым пишут отзывы (определённый фильм, книга или песня).
- Ресурс CATEGORIES: категории (типы) произведений («Фильмы», «Книги», «Музыка»).
- Ресурс GENRES: жанры произведений. Одно произведение может быть привязано к нескольким жанрам.
- Ресурс REVIEWS: отзывы на произведения. Отзыв привязан к определённому произведению.
- Ресурс COMMENTS: комментарии к отзывам. Комментарий привязан к определённому отзыву.

![example workflow](https://github.com/vdvizhenii21/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

## Авторы:
- Цьома Виталий 
- Овчинникова Тома 
- Кораблин Андрей

