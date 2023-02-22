import tkinter as tk
from tkinter import ttk
import webbrowser

# Funktionen zum Öffnen von URLs in einem Webbrowser
def open_aliexpress():
    webbrowser.open_new_tab("https://www.aliexpress.com/")
def open_alibaba():
    webbrowser.open_new_tab("https://www.alibaba.com/")
def open_amazon():
    webbrowser.open_new_tab("https://www.amazon.com/")
def open_zalando():
    webbrowser.open_new_tab("https://www.zalando.com/")
def open_ebay():
    webbrowser.open_new_tab("https://www.ebay.com/")
def open_youtube():
    webbrowser.open_new_tab("https://www.youtube.com/")
def open_netflix():
    webbrowser.open_new_tab("https://www.netflix.com/")

# Erstellen des Hauptfensters
root = tk.Tk()
root.title("Webseiten Dashboard")
root.geometry("600x400")
root.configure(bg='#202020')

# Erstellen von Labeln und Schaltflächen
title_label = tk.Label(root, text="Willkommen zu meinem Dashboard", font=("Arial", 20), fg="white", bg='#202020')
title_label.pack(pady=20)

aliexpress_button = ttk.Button(root, text="AliExpress", style='Golden.TButton', command=open_aliexpress)
aliexpress_button.pack(pady=10)

alibaba_button = ttk.Button(root, text="Alibaba", style='Golden.TButton', command=open_alibaba)
alibaba_button.pack(pady=10)

amazon_button = ttk.Button(root, text="Amazon", style='Golden.TButton', command=open_amazon)
amazon_button.pack(pady=10)

zalando_button = ttk.Button(root, text="Zalando", style='Golden.TButton', command=open_zalando)
zalando_button.pack(pady=10)

ebay_button = ttk.Button(root, text="eBay", style='Golden.TButton', command=open_ebay)
ebay_button.pack(pady=10)

youtube_button = ttk.Button(root, text="YouTube", style='Golden.TButton', command=open_youtube)
youtube_button.pack(pady=10)

netflix_button = ttk.Button(root, text="Netflix", style='Golden.TButton', command=open_netflix)
netflix_button.pack(pady=10)

# Erstellen des Stils für die Schaltflächen
style = ttk.Style()
style.configure('Golden.TButton', background='#FFD700', foreground='#FFD700', font=('Arial', 14, 'bold'))

# Anzeigen des Fensters
root.mainloop()
