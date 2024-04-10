from wakeonlan import send_magic_packet as smp
import tkinter as tk

window = tk.Tk()
window.geometry("400x200")
window.title("WakeOnLan")
title = tk.Label(
    window, text="Wol Magic Packet Sender", font=("Microsoft JhengHei UI", 20), height=2
)
title.pack(side="top")

mac_addr_v = tk.StringVar()
mac_addr_entry = tk.Entry(window, textvariable=mac_addr_v)
mac_addr_entry.pack()
mac_addr_v.set("Enter Mac Address Here")


def send_mp():
    global mac_addr_v
    mac_addr_text = mac_addr_v.get()
    smp(mac_addr_text)
    print("Magic Packet Sent")
    info.set(f"Magic Packet Sent to {mac_addr_text}")


send_button = tk.Button(window, text="Send Magic Packet", command=send_mp)
send_button.pack()

info = tk.StringVar()
info_l = tk.Label(window, textvariable=info, font=("Microsoft JhengHei UI", 10))
info_l.pack(side="bottom")

window.mainloop()
