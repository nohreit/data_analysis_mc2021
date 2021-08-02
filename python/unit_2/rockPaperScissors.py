# two-player Rock-Paper-Scissors game


def run():
    replay = "YES"

    print("Rock-Paper-Scissors")
    # print("Scissors > Paper > Rock and Rock > Scissors")
    while replay == "YES":
        print("[1] => Rock\n[2] => Paper\n[3] => Scissors")
        p1 = int(input("Player1: "))
        p2 = int(input("Player2: "))
        print("Result: ", check(p1, p2))
        print("\nPlay again?\n")
        replay = input("Enter YES for a new game or anything else to quit:\t").upper()
    print("\nThank you for playing")


def check(p1, p2):
    n = [1, 2, 3]
    if p1 == p2:
        return "It's a draw"
    elif p1 not in n or p2 not in n:
        return "Invalid"
    elif p1 == 3 and p2 == 2:  # Scissors > Paper
        return "Player 1 wins"
    elif p1 == 2 and p2 == 1:  # Paper > Rock
        return "Player 1 wins"
    elif p1 == 1 and p2 == 3:  # Rock < Scissor
        return "Player 1 wins"
    else:
        return "Player 2 wins"


if __name__ == "__main__":
    run()
