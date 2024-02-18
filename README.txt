--------------------------------- ENG ---------------------------------

This program is a text processor. Written in the Python programming language.
It reads the contents of the curly braces in the text of the file and replaces it with a predetermined value.
All replaced and replacement values ​​are in the "format_list" dictionary, in the "format_data" file.
The value to be replaced in the dictionary is called a 'key',
and the replacing 'meaning'.

Files for processing must be located in the INPUT folder (hereinafter referred to as "INPUT files").
The files after processing will be located in the OUTPUT folder (hereinafter referred to as "OUTPUT files").
OUTPUT files will appear on their own after processing and will have the same name and extension.
Example: INPUT/test.txt and OUTPUT/test.txt

Example of dictionary design:

###
format_list = {

    "name": "Roman",

    "age": "17",

    "job": "Student"

    }
###

Example text before and after processing:
Before: "Hi, my name is {name}, I'm {age} years old, and I have {job}."
After: “Hi, my name is Roman, I’m 17 years old and I’m a Student.”

If there is no value for a key, a KeyError will be thrown.
If there is no key for the value in the text,
there will be no error.

For example, here's the misspelled text: "Hi, my name is {name}, I'm {age} years old, and I'm {job}. I'm in a {group} group."
Because {group} has no intended value, the program will throw an error.

And here is the text without an error: “Hello, my name is {name}, I am {age} years old.”
The {job} key is not used here, but the program will not generate an error.
You can pre-write a set of keys and values ​​in a dictionary for later use.

Any key can be used an infinite number of times.
For example: "{name}{name} {name}" after processing will turn into "RomanRoman Roman".

You can write several lines for any key. To move down a line, use "\n".
Example: format_list = {"welcome": "Welcome to our store!\nWe have the lowest prices!"}

Example text before and after processing:
Before:
    """
    {welcome}

    Milk: 1000$
    Cheese: 550$
    """

After:
    """
    Welcome to our store!
    We have the lowest prices!

    Milk: 1000$
    Cheese: 550$
    """
It is impossible to insert the key into the key. It will output strictly the value.
Example: format_list = {
        "test_message": "This is a test message!",
        "call_test_message": "{test_message}"
        }

Example text before and after processing:
Before: {call_test_message}
After: {test_message}

You can, of course, process the text again.
Then it will be like this:
Before: {test_message}
After: This is a test message!

Don't just use curly braces in text; the program will try to format everything inside the curly braces.
If the program does not find a matching key to the value, a KeyError will be raised.
You can add a key with a value in curly braces to a dictionary,
so that the program behaves as in the example above.

You can also do this:

format_list = {
    "{test_key}": "{test_value}"
    }

Then the processing will look like this:
Before: {{test_key}}
After: {test_value}

Files with KeyError or ValueError errors are skipped by the program automatically and added to the "problem" list.
If there is an impossible key in the INPUT file (for example {}), the program will throw a ValueError.

The program is launched by running the main.py file using the Python interpreter (Python must be installed on the computer).

In general, experiment and test.



--------------------------------- RUS ---------------------------------

Данная программа - обработчик текста. Написана на языке программирования Python.
Она считывает содержимое фигурных скобок в тексте файла и заменяет его на заданное заранее значение.
Все заменяемые и заменяющие значения находятся в словаре "format_list", в файле "format_data".
Заменяемое значение в словаре называется 'ключом', а заменяющее 'значением'.

Файлы для обработки должны находиться в папке INPUT (далее "INPUT файлы").
Файлы после обработки будут находиться в папке OUTPUT (далее "OUTPUT файлы").
OUTPUT файлы появятся сами после обработки и будут иметь такое же название и расширение.
Пример: INPUT/test.txt и OUTPUT/test.txt

Пример оформления словаря:

###
format_list = {

    "name": "Роман",

    "age": "17",

    "job": "Студент"

    }
###

Пример текста до и после обработки:
До: "Привет, меня зовут {name}, мне {age} лет и я {job}."
После: "Привет, меня зовут Роман, мне 17 лет и я Студент."

Если для ключа не найдется значение, появится ошибка KeyError.
Если для значения в тексте не будет ключа, ошибки не будет.

К примеру, вот текст с ошибкой: "Привет, меня зовут {name}, мне {age} лет и я {job}. Я в {group} группе."
Т.к. для {group} не предназначено значение, программа выдаст ошибку.

А вот текст без ошибки: "Привет, меня зовут {name}, мне {age} лет."
Тут не используется ключ {job}, но ошибку программа не выдаст.
Можно заранее написать набор ключей и значений в словаре для дальнейшего использования.

Любой ключ можно использовать бесконечное количество раз.
К примеру: "{name}{name} {name}" после обработки превратится в "РоманРоман Роман".

Под любой ключ можно записать несколько строк. Для того, чтобы сместиться на строку ниже, используйте "\n".
Пример: format_list = {"welcome": "Добро пожаловать в наш магазин!\nУ нас самые низкие цены!"}

Пример текста до и после обработки:
До: 
    """
    {welcome}

    Молоко: 1000 рублей
    Сыр: 550 рублей
    """

После:
    """
    Добро пожаловать в наш магазин!
    У нас самые низкие цены!

    Молоко: 1000 рублей
    Сыр: 550 рублей
    """

Засунуть ключ в ключ невозможно. Он будет выводить строго значение.
Пример: format_list = {
        "test_message": "Это тестовое сообщение!",
        "call_test_message": "{test_message}"
        }

Пример текста до и после обработки:
До: {call_test_message}
После: {test_message}

Можно конечно еще раз обработать текст.
Тогда будет так:
До: {test_message}
После: Это тестовое сообщение!

Не используйте фигурные скобки в тексте просто так, программа будет пытаться форматировать все, что в фигурных скобках.
Если программа не найдет подходящий ключ к значению, будет ошибка KeyError.
Вы можете добавить ключ со значением в фигурных скобках в словарь, чтобы программа поступила как в примере выше.

Также вы можете поступить так:

format_list = {
    "{test_key}": "{test_value}"
    }

Тогда обработка будет выглядеть так:
До: {{test_key}}
После: {test_value}

Файлы с ошибкой KeyError или ValueError пропускаются программой автоматически и добавляются в список "проблемных".
Если в INPUT файле будет невозможный ключ (к примеру {}), то программа выдаст ошибку ValueError.

Запуск программы производится с помощью запуска файла main.py с помощью интерпретатора Python (на компьютере должен быть установлен Python).

В общем - экспериментируйте и тестируйте.