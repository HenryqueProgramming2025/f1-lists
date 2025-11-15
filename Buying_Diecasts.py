def big_line():
    red = "\033[91m"
    bold = "\033[1m"
    reset = "\033[0m"
    line = "-=" * 30
    print(f"{red}{bold}{line}{reset}")

def explaining():
    bold = "\033[1m"
    reset = "\033[0m"
    print(f"""\n{bold}1. User Will Enter a Diecast He Wants
2. User Will Enter The Car's Main Driver
3. User Will Enter The Car's Year{reset}""")

def icons():
    bold = "\033[1m"
    reset = "\033[0m"
    print(f"""\n{bold}Example:
\n🏎️. Diecast - Renault
😎 Model - R25
🪪. Driver - Fernando Alonso
🎆. Year - 2005{reset}""")

BOLD = "\033[1m"
RESET = "\033[0m"

big_line()
title = "Buying Formula 1 Diecasts - Using Lists".center(60)
print(f"{BOLD}{title}{RESET}")
big_line()

title2 = "Explaing The Exercise To The User".center(60)
print(f"{BOLD}{title2}{RESET}")
explaining()
icons()
big_line()

title3 = "Asking The User To Enter Some Data".center(60)
print(f"{BOLD}{title3}{RESET}")

diecasts = []

while True:
    diecast = input(f"\n{BOLD}Please, Enter The Diecast You Want To Buy (Q/q To Quit): {RESET}")
    if diecast.lower() == "q":
        break
    else:
        model = input(f"{BOLD}Now, For The Model: {RESET}")
        driver = input(f"{BOLD}Enter a Driver That Drove That Car: {RESET}")
        year = int(input(f"{BOLD}Finally, The Year: {RESET}"))
        diecasts.append((diecast, model, driver, year))

big_line()
print(f"{BOLD}| {'Diecast':^12} | {'Model':^6} | {'Driver':^20} | {'Year':^9} |{RESET}")
big_line()

for (diecast, model, driver, year) in diecasts:
    print(f"{BOLD}| {diecast:^12} | {model:^6} | {driver:^20} | {year:^9} |{RESET}")
big_line()