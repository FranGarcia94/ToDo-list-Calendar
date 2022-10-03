# To-Do list Calendar

[![Python_version](https://img.shields.io/badge/Python-v3.10.2-blueviolet?style=flat&logo=python&logoColor=white)](https://www.python.org/downloads/release/python-3102/)
![License](https://custom-icon-badges.herokuapp.com/github/license/FranGarcia94/ToDo-list-Calendar?logo=law)
![Size](https://badge-size.herokuapp.com/FranGarcia94/ToDo-list-Calendar/main/todo-list-calendar.py)

<p align = "center">
<a href="https://github.com/FranGarcia94/ToDo-list-Calendar"><img src="https://user-images.githubusercontent.com/107102754/193524241-2aec673c-020f-49b2-ad2f-47942d77b23a.jpg" width=500/></a>
</p>
<p align = "center">
<b>To-Do list Calendar</b>
</p>

# Introduction

![Tkinter](https://img.shields.io/badge/Tkinter-orange?style=flat)
![tkcalendar](https://img.shields.io/badge/tkcalendar-darkred?style=flat)
![datetime](https://img.shields.io/badge/datetime-blue?style=flat)

This is an application to add a To-Do List within the calendar in a simple and visual way.

It is possible to save and delete tasks by typing them in the text box below, and the calendar always remains on the screen.

| Image | GIF |
| -- | -- |
|<img src="https://user-images.githubusercontent.com/107102754/193534641-7b7aac1c-10ca-45a5-8441-9995fb7e875a.jpg" width="275"/> | <img src="https://user-images.githubusercontent.com/107102754/193534714-24841860-6cb5-4f01-bfbe-abe536225008.gif" width="600"/>|


### Calendar
In the calendar we can see the month, year, day of the week and number of the week, the days in which there is a task will be shown in red, the rest of the days in white and the day that we select will be temporarily blue.

<p align = "center">
<a href="https://github.com/FranGarcia94/ToDo-list-Calendar"><img src="https://user-images.githubusercontent.com/107102754/193526261-d3fe6d22-ae17-4abf-8c72-e83e6a5e52d3.jpg" width=500/></a>
</p>

### Text Box
To add or delete a task, we simply select the day, write or delete it from the text box and click on the Update button. At that time the action will be saved. If there was no task before, the day will turn red.

<p align = "center">
<a href="https://github.com/FranGarcia94/ToDo-list-Calendar"><img src="https://user-images.githubusercontent.com/107102754/193526793-fc264017-26c9-400b-bdb8-829cd5d5a8fc.jpg" width=500/></a>
</p>

### .txt File
Tasks are saved in an associated text file `saved_events.txt`. This is very important as we cannot change the name or the destination folder. Although it is possible to change both things from the code in the following lines:

```python
  def load_task():
    
    # Create the .txt file if it doesn't exist
    with open('saved_events.txt', 'a+') as f:

        f.close()

    with open('saved_events.txt', 'r') as f:
                .
                .
                .
    
```

```python
  # Rewrite the document with existing tasks
  with open('saved_events.txt', 'w') as f:

        for i in tag_list:

            f.write(f'{i}\n')
        
        f.write('\n')

        for i in date_list:

            f.write(f'{i}\n')
            
```
To change the path of the file and position it where it is most comfortable for us, we just have to change the inside of the `open` function and put the full path of the folder we want.

We can also change the name of the file by replacing the existing name, however, if we have already saved a task, it would have to be copied and pasted into the new file when it is generated since it will start empty. 

For example:

```python
  with open('C:\\Users\\...\\FILE_NAME.txt', 'a+') as f:
  
  with open('C:\\Users\\...\\FILE_NAME.txt', 'r') as f:
  
  with open('C:\\Users\\...\\FILE_NAME.txt', 'w') as f:
  
```

In this `.txt` file the tasks and days will be saved with the format shown below:

<p align = "center">
<a href="https://github.com/FranGarcia94/ToDo-list-Calendar"><img src="https://user-images.githubusercontent.com/107102754/193530835-2dad7028-11cb-4664-86e9-21a2cb89f554.jpg" width=500/></a>
</p>

Every time the program starts, it will read the text file to mark the tasks that we had already placed and return to the last state. This file will be created automatically the first time we run the program.

As we can see, the tasks are saved one by one in order of insertion and the dates are saved in sets of 3 numbers: year, month and day. Tasks and dates are separated by an empty line where the program will detect this separation.

### Footnote
This application has been created using the options provided by the `tkcalendar` library, although something more elaborate can be done by incorporating a database and the `treeview` display for a somewhat more complex and elegant finish.

However, this way is simple, intuitive and compact since we have everything in a single interface and all the actions are done quickly.
