# Django Practice

## Using
* [Test-Driven Development with Python][1] by Harry J. W. Percival
* Python 3.5.2
* Firefox 49.0
* [Selenium 3.0.03b][2]
* [Django 1.10.0][3]

## Common Commands
* `python3 manage.py test`
    * Runs unit tests
* `python3 manage.py runserver`
    * Runs dev server
* `python3 functional_tests.py`
    * Runs functional tests

### Problems & Solutions
* Ran into issues using Firefox 49.0
    * Solution: geckodriver

###Notes
* I am using Django 1.10 and the book uses Django 1.8
* I am using Selenium3 and the book uses Selenium2
    * `from selenium.webdriver.common import Keys` becomes from `selenium.webdriver.common.keys import Keys`


[1]: http://chimera.labs.oreilly.com/books/1234000000754/index.html
[2]: https://pypi.python.org/pypi/selenium
[3]: https://docs.djangoproject.com/en/1.10/
