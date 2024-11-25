from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO




def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((600, 480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f'Произошла ошибка: {e}')
        return None

def open_new_window():
    tag = tag_entry.get()
    url_tag = f"https://cataas.com/cat/{tag}" if tag else "https://cataas.com/cat"

    img = load_image(url_tag)



    if img:
        new_window = Toplevel()
        new_window.title("Картинка с котиком")
        new_window.geometry("600x480")
        label = Label(new_window, image=img)
        label.pack()
        label.image = img




def exit():
    window.destroy()




window = Tk()
window.title("Cats")
window.geometry("600x520")

tag_entry = Entry()
tag_entry.pack()


main_menu = Menu(window)
window.config(menu=main_menu)

load_button = Button(text="Загрузить по тегу", command=open_new_window)
load_button.pack()
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="Обновить картинку", command=open_new_window)
main_menu.add_cascade(label="Файл",menu=file_menu)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit)


# update_button = Button(text="Обновить", command=load_image)
# update_button.pack()

url = "https://cataas.com/cat"


window.mainloop()

