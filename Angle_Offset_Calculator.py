#Angle Offset Calculator - Sirka otvoru pri danom uhle a dlzke

# Geometrický model:
# Vstupy: 
#   1. Dĺžka základnej priamky
#   2. Uhol sklonu druhej priamky (prednastavená hodnota 5°)
# Výstupy:
#   1. Vypočítaná dĺžka tretej priamky (kolmá na základnú) – dĺžka vznikajúceho otvoru
#   2. Grafické zobrazenie trojuholníka vo widgete Tkinter Canvas

from tkinter import *
import math

def distance():
    try:
        length_cm = float(length_input.get().replace(',', '.'))             #prilahla odvesna
        angle_degree = float(angle_input.get().replace(',', '.'))
        # Prevod stupňov na radiány
        angle_rad = math.radians(angle_degree)
        # Vzdialenosť = dĺžka * tan(uhol)
        opening_result = length_cm * math.tan(angle_rad)                    #!vypocet dlzky kolmice/otvoru pre zadany uhol - protilahla odvesna
        hypotenuse = math.sqrt(length_cm**2 + opening_result**2)            #vypocet prepony
        
        result_label.config(text=f'Pri uhle {angle_degree}° vznikne otvor:\n{round(opening_result,2)} cm')          #ak potrebne, dopln info o prepone " /prepona: {round(hypotenuse,2)}cm"
    except ValueError:
        result_label.config(text="\nNezadal si číselné hodnoty!")

    draw_triangle(length_cm, opening_result, angle_degree, hypotenuse)                                              # goes to function draw_triangle(1.base,2.height,3.angle,4.hypotenuse/prepona)

    #=== Funkcia na vykreslenie trojuholníka ===
def draw_triangle(base, height, angle, hypotenuse):
    canvas.delete("all")  # vyčistí predchádzajúci nákres

    # mierka - 1 cm = 5 px
    scale = 5
    base_px = base * scale
    height_px = height * scale

    # súradnice
    x0, y0 = 30, 220
    x1, y1 = x0 + base_px, y0
    x2, y2 = x1, y1 - height_px

    # trojuholník
    canvas.create_line(x0, y0, x1, y1, fill="white", width=1)   # základňa
    canvas.create_line(x1, y1, x2, y2, fill="red", width=4)     # výška (otvor)
    canvas.create_line(x0, y0, x2, y2, fill="yellow", width=1)  # šikmá priamka

    # popisy
    canvas.create_text(x0 + base_px/2, y0 + 15, text=f"{base} cm", fill="white", font=('Calibri', 9))
    canvas.create_text(x1 + 25, y1 - height_px/2, text=f"{round(height,2)} cm", fill="red", font=('Calibri', 9, 'bold'))        #otvor text
    canvas.create_text(x0 + 50, y0 - 20, text=f"{angle}°", fill="white", font=('Calibri', 9))
    canvas.create_text(x0 + 10, y1 - 10, text=f"{round(hypotenuse,2)} cm", fill='yellow', font=('Calibri', 9))                  #prepona text

version = 1.2

#Colors
maincolor = 'grey'
textcolor = "white"
inputtextcolor = 'black'

#GUI - basic
window = Tk()
window.title(f'Uhlový kalkulátor otvoru {version}')
window.minsize(315,300)
window.resizable(False,False)
window.config(bg= maincolor)

#GUI - Labels & Frame(cover result_label)
line_text_label = Label(window, text='Priamka 0°\n[cm]', bg=maincolor, font=('Calibri', 11, 'bold'), fg=textcolor)   #relief='sunken' - fajn na check hranic
line_text_label.grid(row=0, column=0,  padx=0 , pady=0, sticky='s')                                             #sticky='s' -taha smerom dole south

angle_text_label = Label(window, text='Uhol -fix 5°\n[°]', bg=maincolor, font=('Calibri', 11, 'bold'), fg=textcolor)
angle_text_label.grid(row=0, column=3, padx=0, pady=0, sticky='s')

result_frame = Frame(window,bg=maincolor, width=150, height=40)             #Do tohoto Framu som umiestnil label a klucove je pouzit columnspan=4 - koľko stĺpcov má widget zaberať.
result_frame.grid(row=2,column=0, columnspan=4, padx=0, pady=0)             #Do tohoto Framu som umiestnil label a klucove je pouzit !!!columnspan=4!!!- koľko stĺpcov má widget zaberať
        #↓→               ↓
result_label = Label(result_frame, text='\nZadaj vstupné údaje', font=('Calibri', 12, 'bold'), bg=maincolor, fg=textcolor)        #INFO after start
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

# === Frame pre grafické znázornenie + Tkinter Canvas ===
canvas_frame = Frame(window, bg='black', width=280, height=250)
canvas_frame.grid(row=3, column=0, columnspan=4, padx=10, pady=10)
canvas = Canvas(canvas_frame, bg='black', width=280, height=250)                                                #Tkinter - Canvas widget pre kreslenie
canvas.pack()


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
    f"Aplikácia: Uhlový kalkulátor otvoru\n"
    f"Verzia: {version}\n"
    f"\n\nAutor:     Igor Vitovský\n"
    f"e-mail:   igvisk.pro@gmail.com\n"
    f"GitHub: github.com/igvisk\n"
    f"Copyright © 2025 Igor Vitovský", 
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