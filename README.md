# Тестовое задание компании КБ Стрелка

Нужно написать простой консольный скрипт на Python, который бы смог сделать следующее
1. открыть раздел "Новости" на сайте StrelkaMag (https://strelkamag.com/ru?format=news)
2. забрать оттуда заголовки первых 50 новостей
3. по какому-либо признаку выбрать среди них те, где есть упоминания о Москве, Ижевсе и Барселоне
4. на основе выборки из п.3 сформировать CSV документ со следующими полями:
- ID - идентификатор статьи (может быть строкой, должен однозначно идентифицировать статью)
- title - заголовок статьи
- date - дата в формате yyyy-mm-dd
- url - ссылка на статью
