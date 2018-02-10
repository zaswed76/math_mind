resource.qrc
=============

Создание файла ресурсов

В корне проекта создайте файл с описанием тех ресурсов, которые собираетесь использовать.

Он имеет следующий вид (resource.qrc): ::

  <RCC>
  <qresource prefix="/">
    <file>resource/icons/stop_btn.png</file>
    <file>resource/icons/start_btn.png</file>
    <file>resource/icons/start_btn_hover.png</file>
    <file>resource/icons/home.png</file>
    <file>resource/icons/combo_down.png</file>
    <file>resource/icons/success.png</file>
    <file>resource/icons/xtwo.png</file>
    <file>resource/icons/xtwo_select.png</file>
  </qresource>
   </RCC>

атрибут prefix указывает относительно какого каталога находатся ресурсы

в данном случае доступ к файлу можно получить так -  :/resource/icons/stop_btn.png.

затем, находясь в корневом каталоге,  набираем команду: ::

 pyrcc5 -o resource.py resource.qrc


в модуле main импортируем модуль resource.py ::

 import resource










