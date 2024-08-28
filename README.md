# Pandas Docker Project

### Описание

Этот проект включает пример использования библиотеки Pandas в Docker-контейнере для анализа данных сотрудников. Скрипт выполняет следующие задачи:
1. Загружает данные из файла `data.csv`.
2. Вычисляет среднюю зарплату всех сотрудников.
3. Отбирает и выводит список сотрудников старше 30 лет.

### Структура проекта

├── Dockerfile  | Файл описания Docker-образа:

├── README.md   | Файл документации проекта:
 
├── app.py      | Основной скрипт приложения на Python:

├── data.csv    | CSV-файл с данными о сотрудниках:

├── docker desktop.jpg  | Вывод в docker

├── terminal.jpg        | Вывод в terminal'e

### Предварительные требования

1. Установленный Docker.
2. Аккаунт на Docker Hub.

### Установка и использование

1. Клонируйте репозиторий:

git clone https://github.com/doclinx/pandas_docker_project.git

cd pandas_docker_project

2. Сборка Docker-образа:

docker build -t pandas_app .

3. Запуск Docker-контейнера:

docker run pandas_app

### Сборка и запуск Docker-контейнера

docker login

2. Тегирование Docker-образа:

docker tag pandas_app doclinx/pandas_app:latest

3. Загрузка Docker-образа в Docker Hub:

docker push doclinx/pandas_app:latest

### Результаты

После запуска контейнера вы должны увидеть следующую информацию в терминале:

- Средняя зарплата всех сотрудников
- Список сотрудников, которым больше 30 лет

Пример вывода: отображены на скриншотах 

├── docker desktop.jpg

├── terminal.jpg

### Ссылка на Docker Hub

Docker-образ doclinx/pandas_app доступен по этой ссылке https://hub.docker.com/r/doclinx/pandas_app/tags
