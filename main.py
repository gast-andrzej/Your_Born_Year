def your_born_year(z = int(input('How Years You Old? '))): return print(f"You Born in {int(__import__('datetime').date.today().year)-z}")
your_born_year()