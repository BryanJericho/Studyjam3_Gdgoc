import random

def playgame ():
    choices = ["Batu", "Gunting", "Kertas"]
    botChoices = random.choice(choices)
    playerChoices = input("Masukkan Pilihan anda : ")
    print("Kamu memilih : ", playerChoices)
    print("Bot memilih : ", botChoices)

    if botChoices == playerChoices : {
        print("Hasilnya seri!")
    }
    elif (botChoices == "Batu" and playerChoices == "Gunting" ) or (botChoices == "Kertas" and playerChoices == "Batu") or (botChoices == "Gunting" and playerChoices == "Kertas") : {
        print("Kamu kalah!")
    } 
    else : {
        print("Kamu menang")
    }

playgame()

# nyawa player dan nyawa botnya