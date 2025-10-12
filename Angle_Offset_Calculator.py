#Sirka otvoru pri danom uhle a hlbke

# Geometrický model:
#skript kde zadam dlzku prvej priamky, uhol 5 stupnov a vyrata mi dlzku tretej priamky (otvoru), 
# ktora je voci prvej priamke(ktora lezi na 0° (kt zadavame dlzku) ) v 90° uhle.

from tkinter import *
import math


#Function - terminal version
# def distance(length_cm, angle_degree):       
#     # Prevod stupňov na radiány
#     angle_rad = math.radians(angle_degree)
#     # Vzdialenosť = dĺžka * tan(uhol)
#     return length_cm * math.tan(angle_rad)

def distance():
    try:
        length_cm = float(length_input.get().replace(',', '.'))
        angle_degree = float(angle_input.get().replace(',', '.'))
        # Prevod stupňov na radiány
        angle_rad = math.radians(angle_degree)
        # Vzdialenosť = dĺžka * tan(uhol)
        opening_result = length_cm * math.tan(angle_rad)   
        result_label.config(text=f'Pri uhle {angle_degree}° vznikne otvor:\n{round(opening_result,2)} cm')
    except ValueError:
        result_label.config(text="\nNezadal si číselné hodnoty!")


#Colors
maincolor = 'grey'
textcolor = "white"
inputtextcolor = 'black'

#GUI - basic
window = Tk()
window.title('Uhlový kalkulátor otvoru')
window.minsize(280,120)
window.resizable(False,False)
window.config(bg= maincolor)




#GUI - Labels & Frame(cover result_label)
line_text_label = Label(window, text='Priamka 0°\n[cm]', bg=maincolor, font=('Calibri', 11, 'bold'), fg=textcolor)   #relief='sunken' - fajn na check hranic
line_text_label.grid(row=0, column=0,  padx=0 , pady=0, sticky='s')                                             #sticky='s' -taha smerom dole south

angle_text_label = Label(window, text='Uhol -fix 5°\n[°]', bg=maincolor, font=('Calibri', 11, 'bold'), fg=textcolor)
angle_text_label.grid(row=0, column=3, padx=0, pady=0, sticky='s')

result_frame = Frame(window,bg=maincolor, width=150, height=40)             #Do tohoto Framu som umiestnil label a klucove je pouzit columnspan=4 - koľko stĺpcov má widget zaberať.
result_frame.grid(row=2,column=0, columnspan=4, padx=0, pady=0)             #Do tohoto Framu som umiestnil label a klucove je pouzit !!!columnspan=4!!!- koľko stĺpcov má widget zaberať
# result_frame.grid_propagate(False)                                #candidate to remove
result_label = Label(result_frame, text='Zadaj vstupné údaje', font=('Calibri', 12, 'bold'), bg=maincolor, fg=textcolor)        #INFO after start
# result_label.pack(expand=True, fill=BOTH)                         #candidate to remove
result_label.grid(row=2, column=1, padx=0, pady=0)

#GUI - User inputs
length_input = Entry(window, width=10, font=("Calibri", 12), fg=inputtextcolor, justify=CENTER)
length_input.insert(0,'0')                                                                                      #(0-pozicia v texte,'default hodnota zobraz sa pri spusteni')
length_input.grid(row=1, column=0, padx=10,pady=0, sticky='n')                                                  #sticky='n' taha smerom hore k line_text_label n-north


angle_input = Entry(window, width=10, font=("Calibri", 12), fg=inputtextcolor, justify=CENTER)
angle_input.insert(0,'5')                                                                                       #(0-pozicia v texte,'default hodnota zobraz sa pri spusteni')
angle_input.grid(row=1, column=3, padx=10,pady=0, sticky='n')

#GUI - Button
button_count = Button(window, text='Vypočítaj', font=('Calibri', 10), command=distance)
button_count.grid(row=1,column=1, padx=0,pady=0, sticky='n')




#Menu

#Menu funkcie

def quit_app():
    window.quit()

def show_about():
    about_window = Tk()
    about_window.title('About')
    about_window.minsize(280,120)
    about_window.resizable(False,False)
    about_window.config(bg= maincolor)
    about_window_label = Label(about_window, text=
    "Aplikácia: Uhlový kalkulátor otvoru\n" \
    "Verzia: 1.1\n" \
    "\n\nAutor:     Igor Vitovský\n" \
    "Email:     igvisk.pro@gmail.com\n" \
    "GitHub: github.com/igvisk\n" \
    "Copyright © 2025 Igor Vitovský", 
    bg=maincolor, font=('Calibri', 11, 'bold'), fg=textcolor, justify=LEFT)
    about_window_label.grid()


# Vytvorenie hlavného menu
menu_bar = Menu(window)
window.config(menu=menu_bar)

# --- 1 Súbor ---
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nový výpočet  Ctrl+N", command=distance)          #Stlacenie vypoctu -funkcia distance
file_menu.add_separator()
file_menu.add_command(label="Ukončiť             Ctrl+Q", command=window.quit)
menu_bar.add_cascade(label="Súbor", menu=file_menu)

# --- 2 Nastavenia --- TBD
# settings_menu = Menu(menu_bar, tearoff=0)
# settings_menu.add_command(label="Farba pozadia", command=lambda: print("Zmena farby"))
# settings_menu.add_command(label="Resetovať vstupy", command=lambda: print("Reset"))
# menu_bar.add_cascade(label="Nastavenia", menu=settings_menu)

# --- 3 Help/Pomocník ---
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="O programe  F1", command=show_about)          
menu_bar.add_cascade(label="Help", menu=help_menu)

# --- Klávesové skratky (bind) ---
window.bind("<Control-n>", lambda event: distance())                # .bind("<Key-combination>", lambda event: run_function())
window.bind("<Control-q>", lambda event: quit_app())
window.bind("<F1>", lambda event: show_about())


#Tkinter Mainloop
window.mainloop()



#terminal version /obsolete
# Príklady
# print("8,8 cm pri 5°:", round(vzdialenost(8.8, 5), 2), "cm")      # → 0,77 cm

# print("17 cm pri 5°:", round(vzdialenost(17, 5), 2), "cm")        # → 1.49 cm

#Zadaj vlastnu dlzku
# length_cm = float(input("Zadaj dlzku priamky leziacej na 0°: "))
# print(f"{length_cm} cm pri 5°, vychýlenie:", round(distance(length_cm, 5), 2), "cm")
