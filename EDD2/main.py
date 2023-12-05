from prog01 import evaluation

def main():
    print("Digite as expressoes: ")

    while True:
        user_input = input(">>> ")

        if user_input == "exit":
            break

        evaluation(user_input) 

if __name__ == "__main__":
    main()
