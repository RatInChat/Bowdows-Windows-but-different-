import time
import sys
print("Loading Bodows:")
# important vars
guest = ""
loadingSignin = ""
appsChoice = ""
searchQuery = ""
talks = ""
# important functions
def load():
  print("Loading:")
  #animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
  animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

  for i in range(len(animation)):
     time.sleep(0.2)
     sys.stdout.write("\r" + animation[i % len(animation)])
     sys.stdout.flush()

  print("\n")

def load2():
  print("Loading:")


  #animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
  animation = ["|", "/", "-", "\\","|", "/", "-", "\\"]

  for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

  print("\n")
def apps():
  time.sleep(0.5)
  print("1. BoExploer")
  time.sleep(0.5)
  print("2. BoCord")
  time.sleep(0.5)
  print("3. DarkBo")
  time.sleep(0.5)
  print("4. BoTube")
  time.sleep(0.5)
  print("5. Visual Bo")
  time.sleep(0.5)
  print("6. exit")
  appsChoice = input("What app do you want to open? Choose: " + " ")
  if appsChoice == "1":
    load2()
    print("Welcome to BoExploer!")
    searchQuery = input("What do you want to search up? Choose: ")
    load2()
    print("No.")
    apps()
  elif appsChoice == "2":
    load2()
    print("Welcome to BoCord!")
    time.sleep(0.5)
    print("Succesfully Logged In!")
    time.sleep(0.5)
    bocord()
  elif appsChoice == "3":
    load2()
    print("Welcome to DarkBo!")
    time.sleep(0.5)
    print("Turning on Virus Protection...")
    load2()
    print("Virus Protection Failed continue at your own risk!")
    time.sleep(0.5)
    searchQuery = input("What do you want to search up? Choose: ")
    load2()
    print("That will cost you... ")
    time.sleep(0.2)
    print("VIRUS DETECTED! KILLING TASK!")
    time.sleep(0.2)
    print("CLOSING DARKBO")
    apps()
  elif appsChoice == "4":
    load2()
    print("Welcome to BoTube!")
    time.sleep(0.3)
    print("videos")
    load2()
    print("Videos failed to load! Unfortuantly this app is coming soon!")
    apps()
  elif appsChoice == "5":
    load2()
    print("Code what you want!")
    code = input("Your code: ")
    load2()
    print("code failed to load.")
    time.sleep(0.5)
    print("Reporting to Bodows...")
    load()
    print("Successfully Reported. Wating for an answer...")
    load2()
    print("Answer recived! This app is coming soon....")
    apps()
  elif appsChoice == "6":
    print("exiting...")
    load2()
    print("Closing Bowdows...")
    load()
    print("Succesfully closed Bowdows! Come back soon!")
def bocord():

    print("Here are your freinds!")
    time.sleep(0.2)
    print("1. Bob")
    time.sleep(0.3)
    print("2. Ken")
    time.sleep(0.3)
    print("3. Amantha")
    time.sleep(0.3)
    print("4. Emily")
    time.sleep(0.3)
    print("5. Exit")
    time.sleep(0.4)
    talks = input("Choose who to talk to: ")
    if talks == "1":
      time.sleep(0.5)
      print("You: Hey Bob whats up?")
      time.sleep(1)
      print("Bob: Too busy right now/Can't talk.")
      time.sleep(1)
      print("Bob: sorry.")
      time.sleep(0.9)
      bocord()
    elif talks == "2":
      time.sleep(0.5)
      print("You: Hi Ken whats up?")
      time.sleep(1)
      print("You: Ken?")
      time.sleep(2)
      print("You: KEN?!?")
      time.sleep(2)
      print("You: KE-")
      time.sleep(0.1)
      print("Ken's Parents: Ken is dead. :(")
      time.sleep(1)
      print("You: Oh sorry...")
      time.sleep(0.9)
      bocord()
    elif talks == "3":
      time.sleep(0.5)
      print("You: Hey Amantha whats up?")
      time.sleep(1)
      print("Amantha: Hey..")
      time.sleep(1)
      print("You: Man finnally a freind who wants to talk to me!")
      time.sleep(0.5)
      print("Amantha: About that...")
      time.sleep(1)
      print("Amantha: I can't really talk to you anymore...")
      time.sleep(1)
      print("Amantha: My religion or somthing...")
      time.sleep(0.9)
      print("Amantha: Sorry.")
      time.sleep(0.9)
      bocord()
    elif talks == "4":
      time.sleep(0.5)
      print("You: Hey Emily whats up?")
      time.sleep(0.1)
      print("Emily: Don't even talk to me.")
      time.sleep(0.3)
      print("Emily: You know what you did.")
      time.sleep(0.3)
      print("Guilt floods you...")
      bocord()
    else:
      print("Exiting...")
      load()
      print("Exited!")
      apps()
# start of code!
load()
print("Welcome to Bodows!")
time.sleep(1)
account = input("do you have a Bopez account? Y/N: ")
if account.lower() == "y":
  username = input("username: " + " ")
  password = input("password: " + " ")
  print("Signing in...")
  load2()
  print("Sign In Successfull!")
  print("\n")
  print("Welcome to Bowdows " + username + "!")
  time.sleep(0.5)
  print("You have 5 apps!")
  apps()
else:
  guest = input("Enter guest mode? Y/N: ")
if guest.lower() == "y": 
  print("Signing in as Guest...")
  load2()
  print("Sign In Successfull!")
  print("\n")
  print("Welcome to Bowdows" + "!")
  time.sleep(0.5)
  print("You have 5 apps!")
  apps()
if guest.lower() == "n":
  time.sleep(0.5)
  print("Can not log in as guest or user.")
  time.sleep(0.5)
  print("Reporting to Bodows...")
  load()
  print("\n")
  print("loading no work")
  time.sleep(1)
  print("destroying computer")
  load()
  print("loading no work")
  time.sleep(1)
  print("killing task...")
  load()
  print("task kill succsessfull")
  