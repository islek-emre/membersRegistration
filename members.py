import tkinter as tk
from tkinter import messagebox, scrolledtext

# Üye kaydetme fonksiyonu
def save_member():
    # Girdi alanlarındaki verileri al
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    phone = phone_entry.get()
    other_info = other_entry.get()

    # Boş alan kontrolü
    if not first_name or not last_name or not phone:
        messagebox.showwarning("Input Error", "Please fill out all required fields.")
        return

    # Üye bilgilerini txt dosyasına kaydet
    with open("members.txt", "a") as file:
        file.write(f"{first_name},{last_name},{phone},{other_info}\n")
    
    # Kullanıcıya başarı mesajı göster ve alanları temizle
    messagebox.showinfo("Success", "Member saved successfully!")
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    other_entry.delete(0, tk.END)

# Üye listeleme fonksiyonu
def list_members():
    try:
        # Üyeleri gösteren alanı temizle
        result_text.delete(1.0, tk.END)
        
        # Dosyadaki üyeleri okuma
        with open("members.txt", "r") as file:
            members = file.readlines()
            
            # Her bir üyeyi listeye ekleme
            if members:
                result_text.insert(tk.END, "List of Members:\n\n")
                for member in members:
                    result_text.insert(tk.END, member)
            else:
                result_text.insert(tk.END, "No members found.\n")
    
    except FileNotFoundError:
        result_text.insert(tk.END, "No members file found.\n")

# GUI kurulum
root = tk.Tk()
root.title("Member Registration")

# İsim
tk.Label(root, text="First Name:").grid(row=0, column=0, padx=10, pady=5)
first_name_entry = tk.Entry(root, width=30)
first_name_entry.grid(row=0, column=1, padx=10, pady=5)

# Soyisim
tk.Label(root, text="Last Name:").grid(row=1, column=0, padx=10, pady=5)
last_name_entry = tk.Entry(root, width=30)
last_name_entry.grid(row=1, column=1, padx=10, pady=5)

# Telefon
tk.Label(root, text="Phone Number:").grid(row=2, column=0, padx=10, pady=5)
phone_entry = tk.Entry(root, width=30)
phone_entry.grid(row=2, column=1, padx=10, pady=5)

# Diğer Bilgiler
tk.Label(root, text="Other Info:").grid(row=3, column=0, padx=10, pady=5)
other_entry = tk.Entry(root, width=30)
other_entry.grid(row=3, column=1, padx=10, pady=5)

# Kaydet Butonu
save_button = tk.Button(root, text="Save Member", command=save_member)
save_button.grid(row=4, column=0, pady=10)

# Listeleme Butonu
list_button = tk.Button(root, text="List Members", command=list_members)
list_button.grid(row=4, column=1, pady=10)

# Üyeleri gösteren kaydırılabilir metin kutusu
result_text = scrolledtext.ScrolledText(root, width=60, height=15)
result_text.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
