def big_line():
    print('-=' * 24)

big_line()
print('Drivers Names - Fullname and Acronym'.center(48))
big_line()

all_drivers = []

print('Asking The User To Enter The Data'.center(48))
drivers = int(input('\nEnter The Amount Of Drivers You Want To Insert: '))

for d in range(1, drivers + 1):
    fullname = input('Enter The Fullname Of The Driver: ')
    all_drivers.append(fullname)

big_line()
print(f"| {'Position':^7} | {'Fullname':^18} | {'Acronym Name':^10} |")
big_line()

for i, fullname in enumerate(all_drivers):
    surname = fullname.split()[-1]
    acronym = surname[0:3]
    print(f"| {i + 1:^8} | {fullname:^18} | {acronym[0:3]:^12} |".upper())
big_line()

