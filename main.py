from whatsapp import send_whatsapp
from email_sender import send_email

def menu():
    print("\n--- AutoMessenger ---")
    print("1. Send WhatsApp Message")
    print("2. Send Email")
    print("3. Exit")

    while True:
        choice = input("Choose an option (1-3): ")
        if choice == '1':
            send_whatsapp()
        elif choice == '2':
            send_email()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

menu()
