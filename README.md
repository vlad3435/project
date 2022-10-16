# Юлинский Влад, ББИ226
## Техническое задание № 2: 
*Добавляем тесты и разворачиваем простейший CI/CD*

Представляю вашему вниманию код, обрабатывающий массив и находящий некоторые его характеристики: **минимум**, **максимум**, **сумму** и **произведение** его элементов. 

Помимо самого кода реализованы следующие тесты:

>Минимум и максимум

_- проверка восприимчивости к знаку (работа с отрицательными числами)_

_-проверка корректности работы при добавлении элемента_

_-проверка того, что порядок элементов последовательности для работы функции значения не имеет_

> Сумма и произведение

_-проверка коммутативности_

_-проверка свойств умножения (наличие 0 "зануляет" все произведение, (-1) * (-1) = 1, но (-1) * 1 = -1)_

>Корректность входных данных

_-проверка на то, что данные соотвествуют ограничениям (всегда есть хотя бы одно число, не может быть больше миллиона чисел)_

_-проверка того, что все получаемые данные - числа_

>Тесты времени работы программы при увеличении количества входных данных

_-реализация с помощью модуля time и контроля времени работы всей программы (учитывается не только конкретная функция, но и время на считывание данных)_

На основе тестов времени установлен линейный характер роста времени работы и составлен график зависимости времени работы от количества входных данных.