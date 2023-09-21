import os
import sys

def get_valid_shutdown_time():
    while True:
        try:
            shutdown_time = int(input("Enter the shutdown time in seconds: "))
            if shutdown_time <= 0:
                print("Please enter a positive integer for shutdown time.")
            else:
                return shutdown_time
        except ValueError:
            print("Invalid input. Please enter a valid number of seconds.")

def main():
    try:
        shutdown_time = get_valid_shutdown_time()
        print(f"Scheduling shutdown in {shutdown_time} seconds...")
        os.system(f'shutdown /s /t {shutdown_time}')
    except KeyboardInterrupt:
        print("\nShutdown timer canceled.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
