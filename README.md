# okx-racer-rpa
Кликер для игры okx-racer в тг:   
[Запустить кликер](https://t.me/OKX_official_bot/OKX_Racer?startapp=linkCode_65748275)

## Инфо   
На компьютере с windows запущены несколько версий tg. Один раз в X секунд ищем на экране случайно выбранные кнопки `static/moon.png` или `static/doom.png` и кликаем на них всех по очереди.    
Это примитивная версия кликера. Хорошо бы использовать прокси: 1 прокси = 1 приложение. Например подойдёт proxifier.    
Не рекомендуется запускать с одного айпи более 5 таких учёток. Да и в целом любая автоматизация это риск быть забаненным.

## Установка проекта на Windows
0. [Установка git](https://git-scm.com/download/win/)    
1. [Установить python](https://www.python.org/downloads/).    
2. [Скачать](https://desktop.telegram.org/) portable версию тг.     
![telegram](./static/for_readme/image.png)
3. Настройка рабочей среды.
    - 1 аккаунт = 1 папка, в каждую папку нужно закинуть копию portable телеги, запустить и залогиниться в тг.     
    - Переименовать .exe файл от телеги в соответствии с именем папки. 
    - Для каждого тг для удобства надо отключить уведомления и изменить размер интерфейса тг, чтобы больше вмещалось на пк (Настройки -> масштаб по умолчанию).    
4. Открыть cmd(нажать `Win+R`, ввести `cmd`, нажать `enter`), перейти в папку куда хотим скачать проект( например `cd C:\`).    
```
git clone https://github.com/aizavod/okx-racer-rpa.git
cd okx-racer-rpa
python -m venv venv (Если на этом шаге ошибка, то нужно найти полный путь к .exe файлу питона и вставить его вместо `python`), пример: "C:\Program Files\python\python.exe" -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
python rpa.py
```
5. Запустить телеги, запустить кликер, расставить на рабочем экране. (Если не кликается, то можно заменить кнопки в папке static `doom.png` и `moon.png`).


## Создание ярлыка на рабочем столе
Для создания ярлыка на рабочем столе Windows, вам потребуется выполнить следующие шаги:

- На рабочем столе жмём правой кнопкой мыши и кликаем `создать ярлык`
- В поле объект указать комбинацию `"путь к питону в виртуальной среде.exe"` `"путь к скрипту"`
Пример: `"C:\okx-racer-rpa\venv\Scripts\python.exe" "C:\okx-racer-rpa\rpa.py"`
- Нажмите далее и сохраните ярлык
- Кликните правой кнопкой мыши по ярлыку и в поле Рабочая папка укажите папку проекта, например: `"C:\okx-racer-rpa"`

## Версии
Версия #2    
Июль, 2024