import send_email

def main():
    #Eingabe von Informationen
    print("Willkomen bei der Installation von Watch My Pi! \nZum Nutzen der Software benötigt Watch My Pi! ihre E-Mail Adresse und Anmelde Daten \nDiese werden nur lokal gespeichert und kommen an keiner Stellle online. \nACHTUNG: Die Anmelde Daten inbegriffen dem Passwort sind zurzeit lokal zugreifbar, wir empfehlen daher eine eigene E-Mail nur für Watch My Pi! zu verwenden.")
    emailData = input("\n E_Mail: \n ") +"|"
    emailData += input("\n SMTP Adresse (Form: smtp.domain.com): \n ") +"|"
    emailData += input("\n Passwort: \n ")

    rightKey = False;
    #TODO: Random key generation
    key = "7T23C"

    #Speichern der Daten als .txt Datei
    path = "C:\\Users\\Hartmut\\Desktop\\testDatei.txt"
    file = open(path, "w")
    file.write(emailData)
    file.close()
    
    #Senden einer Email und bestätigen des Keys
    send_email.main("Bitte übertragen sie diesen Schlüssel in die Konsole:\n\n"+key)
    print("\nIhn wurde ein Schlüssel per E-Mail gesendet. Bitte bestätigen sie die Richtigkeit der angegebenen Daten indem sie den Schlüssel in die Konsole schreiben.")
    while(rightKey):
        if(input("Schlüssel: ")==key):
            rightKey = True
        else:
            print("Der Schlüssel war leider falsch")
            
    print("Se haben Watch My Pi erfolgreich instaliert. Viel Spaß damit! :)")
    
    return True
    
if __name__ == '__main__':
  main()
