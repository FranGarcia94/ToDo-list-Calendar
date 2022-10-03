#============================= To-Do list Calendar =============================#
#                                                                               #
#                       Calendar where to add To-Do list                        #
#                                                                               #
#                                                            @FranGarcia94      #
#===============================================================================#

import datetime
from tkinter import *
from tkcalendar import *


def showEvent(event):

    y = cal.get_calevents(date = cal.selection_get())

    t.delete(1.0,'end')
    t.insert('end', f" ~ ~   {cal.selection_get().strftime('%d-%B-%Y')}   ~ ~ \n\n")
    t.tag_add("here", "1.0", "2.0")
    t.tag_config("here", background = "#FFEDC5", foreground = "black", underline = True, justify = 'center')

    for i in y:

        aux = cal.calevent_cget(i, 'tags')

        if len(aux) > 1:

            t.insert('end', f"{aux[i]}\n")
        else:

            t.insert('end', f"{aux[0]}\n")


def load_task():
    
    # Create the .txt file if it doesn't exist
    with open('saved_events.txt', 'a+') as f:

        f.close()

    with open('saved_events.txt', 'r') as f:

        txt_reader = f.readlines()
        txt_reader = [txt_reader[i].split('\n') for i in range(len(txt_reader))]
        [txt_reader[i].remove('') for i in range(len(txt_reader)) if len(txt_reader[i]) > 1]


    global tag_list
    global date_list
    global datetime_format

    for i in range(len(txt_reader)):

        if txt_reader[i][0] != '':

            tag_list.append(txt_reader[i][0])
        else:

            del txt_reader[0:i+1]
            date_list = [int(k[0]) for k in txt_reader]

            break

    datetime_format = []

    i = 0
    while i in range(len(date_list)):

        datetime_format.append(datetime.date(date_list[i], date_list[i+1], date_list[i+2]))
        i += 3

    
    for i in range(len(tag_list)):

        id = cal.calevent_create(datetime_format[i], 'Task', tags = tag_list[i])
        cal.tag_config(tag_list[i], background = 'red', foreground = 'yellow')
    

def update_fun():

    textbox_list = t.get(3.0, 'end') # Correspond to everything in textbox, less first line

    # These two lines prepare the word or sentence to be treated
    textbox_list = textbox_list.split("\n")
    textbox_list = list(filter(('').__ne__, textbox_list)) 

    dif_insert = list(set(textbox_list).difference(set(tag_list))) # If there is a new item to insert (or several)

    for i in dif_insert:

        tag_list.append(i)

        date_list.append(cal.selection_get().year)
        date_list.append(cal.selection_get().month)
        date_list.append(cal.selection_get().day)

        id = cal.calevent_create(cal.selection_get(), 'Task', tags = i)
        cal.tag_config(tag_list[-1], background = 'red', foreground = 'yellow')


    y = cal.get_calevents(date = cal.selection_get())
    aux = []

    for i in y:

        aux.append(cal.calevent_cget(i,'tags')[0])

    dif_delete = list(set(aux).difference(set(textbox_list))) # If there is a new item to delete (or several)

    for j in dif_delete:

        id2 = cal.get_calevents(date = cal.selection_get(), tag = j)

        cal.calevent_remove(tag = j)

        date_list.pop(3*tag_list.index(j))
        date_list.pop(3*tag_list.index(j))
        date_list.pop(3*tag_list.index(j))

        tag_list.remove(j)
        
    # Lines to check that everything is going well
    '''print(f'\nDiff Insert: {dif_insert}\n')
    print(f'\nDiff Delete: {dif_delete}\n')

    print(f'Update List(textbox_list): {textbox_list}\n')
    
    print(f'Tag List: {tag_list}')
    print(f'Date List: {date_list}')
    print(f'IDs: {cal.get_calevents()}')'''

    with open('saved_events.txt', 'w') as f:

        for i in tag_list:

            f.write(f'{i}\n')
        
        f.write('\n')

        for i in date_list:

            f.write(f'{i}\n')


# Hover functions
def enter_fun(e):

    update_button['background'] = '#8F8F87'
    update_button['foreground'] = '#FFEDC5'
    update_button['font'] = ('Pristina 15 bold')

def leave_fun(e):

    update_button['background'] = '#FFEDC5'
    update_button['foreground'] = 'black'
    update_button['font'] = ('Pristina 15 bold')



if __name__ == '__main__':

    tag_list = []
    date_list = []

    year = datetime.datetime.now().year
    
    root = Tk()
    root.title('Calendar')
    root.iconbitmap('ga2.ico') # https://icon-icons.com


    cal = Calendar(root, Year = year)

    cal.config(background = '#5A3E00', foreground = '#BCFFF9', font = ('Pristina 12 bold'), bordercolor = '#5A3E00', borderwidth = 0,
        headersbackground = '#FFEDC5', headersforeground = 'black', 
        normalbackground = 'white', normalforeground = 'black', weekendbackground = 'white', weekendforeground = 'black',
        othermonthforeground = '#464646', othermonthbackground = '#C5C5C5', othermonthweforeground = '#464646', othermonthwebackground = '#C5C5C5')


    cal.bind('<<CalendarSelected>>', showEvent)
    cal.pack(fill = 'both',expand = 1)


    load_task()


    t = Text(root, height = 12, width = 50)
    t.config(relief = 'solid', borderwidth = 2, font = ('Arial 13 bold'), padx = 10, pady = 10)
    t.pack(fill = 'both', expand = 1)


    update_button = Button(root, text = 'Update', command = update_fun)
    update_button.pack(fill = 'both', expand = 1)
    update_button.config(relief = 'solid', borderwidth = 1, cursor = 'hand2', background  = '#FFEDC5', font = ('Pristina 15 bold'))

    update_button.bind('<Enter>', enter_fun)
    update_button.bind('<Leave>', leave_fun)

    root.mainloop()
