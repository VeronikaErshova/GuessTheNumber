# Игра "Угадай число"

Это простая игра "Угадай число", написанная на Python с использованием библиотеки PyQt для графического интерфейса. Игроку предлагается угадать загаданное число в заданном диапазоне за ограниченное количество попыток.

## Описание

В этой игре компьютер загадывает случайное число в диапазоне от 1 до 100. Игрок вводит свои предположения, и программа сообщает, было ли число слишком высоким, слишком низким или угадано. После выигрыша игроку предлагается продолжить игру или выйти.

## Установка

### Требования

- Docker
- Docker Compose (опционально)

### Клонирование репозитория

Сначала клонируйте репозиторий:

```bash
git clone https://github.com/VeronikaErshova/GuessTheNumber.git
cd guessing_game
```

### Сборка Docker-образа
Соберите Docker-образ с помощью следующей команды:

```bash
docker build -t guessing_game .
```
### Запуск приложения
Запустите контейнер с графическим интерфейсом. Если вы используете Linux с X11 или на WSL для Windows, выполните:

```bash
docker run -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix guessing_game
```
Если вы используете Windows или macOS, вам может понадобиться настроить X11 или использовать VNC для отображения графического интерфейса.

### Использование
Запустите приложение, как указано выше.
Введите число в текстовое поле и нажмите кнопку "Угадать".
Игра сообщит, угадали ли вы число, и предложит продолжить или выйти после выигрыша.
Лицензия

`Этот проект лицензирован под MIT License - смотрите файл LICENSE для подробностей.`

### Контрибьюция
Если вы хотите внести свой вклад в проект, пожалуйста, создайте форк репозитория, внесите изменения и создайте pull request.

### Автор

Вероника Ершов



