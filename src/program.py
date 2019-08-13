from colorama import Fore
import program_guests
import program_hosts
import data.mongo_setup as mongo_setup
import sys

def main():
    mongo_setup.global_init()

    print_header()

    run()


def print_header():

    cat = \
    """
  .-------.
  |  Hi   |
  '-------'
      ^      (\_/)
      '----- (O.o)
             (> <)
    """
    print(Fore.WHITE + '****************  CatCageRentApp  ****************')
    print(Fore.CYAN + cat)
    print(Fore.WHITE + '**************************************************')
    print()
    print("Welcome to CatCageRentApp!")
    print("Why are you here?")
    print()


def find_user_intent():
    print("[g] Book a cage for your cat")
    print("[h] Offer extra cage space")
    print()
    choice = input("Are you a [g]uest or [h]ost or e[x]it? ")
    if choice == 'h':
        return 'offer'

    elif choice == 'g':
        return 'book'
    elif choice == 'x':
        sys.exit(0)
    else :
        print("\n\n")
        unknown_command()
        print("Press either g or h or x to exit the app.\n\n")
        find_user_intent()

def run():
    mongo_setup.global_init()
    try:
        while True:
            if find_user_intent() == 'book':
                program_guests.run()
            else :
                program_hosts.run()
    except KeyboardInterrupt:
        return
    

def unknown_command():
    print("Sorry we didn't understand that command.")

if __name__ == '__main__':
    main()
