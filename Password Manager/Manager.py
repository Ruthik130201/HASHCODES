def main():

     try:
        PasswordList = []
        infile = open("ThePasswordList.txt", "r")
        line = infile.readline()
        while line:
          PasswordList.append(line.strip("\n").split(","))
          line = infile.readline()
          infile.close

     except FileNotFoundError:
         print("the <ThePasswordList.txt> file is not found")
         print("starting a new password list!")
         PasswordList = []
      
     choice = 0
     while choice !=4:
      print("* Password Manager * ")
      print("1) Add a Password")
      print("2) Lookup a Password")
      print("3) Display a Password")
      print("4) Quit")
      choice = int(input())

      if choice == 1:
        print("Addig a book...")
        nWebsite = input("Name of Website>")
        nEmail = input("Email>")
        nPassword = input("Password>")
        PasswordList.append([nWebsite, nEmail, nPassword])

      elif choice == 2:
          print("Looking up for a Password...")
          keyword = input("Enter Search Term: ")
          for book in PasswordList:
            if keyword in book:
                print(book)

      elif choice == 3:
          print("All Password...")
          for i in range(len(PasswordList)):
              print(PasswordList[i])

      elif choice == 4:
          print("Quitting Program")
     print("Program Terminated!")

     outfile = open("ThePasswordList.txt", "w")
     for book in PasswordList:
         outfile.write(",".join(book) + "\n")
     outfile.close()

if __name__ == "__main__":
    main()   
