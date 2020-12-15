import random

# Função que chama o game
def init_game():  
  total_numbers_list = []  
  sides = choose_dice_sides()
  roll = True
  roll_the_dice(roll, sides, total_numbers_list)

# Gera números para os dados
def result(sides):
  dice = random.randint(1, sides)
  return dice

# Gera lista de todos os números sorteados
def list_results(list):
  rodada = 0
  print("Números Sorteados:")
  while(rodada < len(list)):
    print(f"{rodada+1}ª: {str(list[rodada]).strip('[]')} | Total: {sum(list[rodada])}")
    rodada += 1

# Verifica se o usuário quer jogar e escolher o número de lados do dado
def choose_dice_sides():
  roll = False
  print("==================================")
  print("Bem-vindo ao lançador de dados!")  
  play = input("Gostaria de jogar? ").lower().strip()

  while (not roll):
    if (play == "nao"):
      print("Que pena :( Até mais!")
      quit()
    elif (play == "sim"):
      print("Vamos jogar :)")      
      sides = input('Escolha o número de lados do dado: ').strip()
      while (not sides.isdigit()):
        print("Tentativa inválida!")
        sides = input('Escolha o número de lados do dado: ').strip()
      sides = int(sides)   
      roll = True      
    else:
      play = input("Não entendi, gostaria de jogar? Digite 'SIM' ou 'NAO': ").lower()
  print("==================================")
  return sides

# Roda o lançador de dados depois que usuário escolhe o número de lados
def roll_the_dice(roll, sides, total_numbers_list):
   while (roll):
    print('"ENTER" para rolar o dado!')
    print('"L" para ver os números sorteados!')
    print('"D" para trocar o dado!')
    print('"Q" para sair!')
    action = input().lower().strip()    

    if (action == "q"):
      roll = False
      print()
      print("==================================")
      print("Até a próxima!")
      print("==================================")
    elif (action == "l"):
      print()
      print("==================================")      
      list_results(total_numbers_list)
      print("==================================")
    elif (action == "d"):
      print()
      print("==================================")
      sides = input('Escolha o número de lados do dado: ').strip()
      while (not sides.isdigit()):
        print("Tentativa inválida!")
        sides = input('Escolha o número de lados do dado: ').strip()
      sides = int(sides)
      print("==================================")
    elif (action == ""):      
      dices_amount = input("Quantos dados serão jogados? ").strip()
      while (not dices_amount.isdigit()):
        print("Tentativa inválida!")
        dices_amount = input('Quantos dados serão jogados? ').strip()
      dices_amount = int(dices_amount)
      round_numbers_list = []      
      for x in range(dices_amount):        
        dice_number = result(sides)
        round_numbers_list.append(dice_number)
      print()
      print("==================================")
      print(f"E o dado rolou: {round_numbers_list}")
      print(f"Total: {sum(round_numbers_list)}")
      total_numbers_list.append(round_numbers_list)
      print("==================================")
    else:
      roll = True
      print("==================================")
      print("Comando Inválido!")
      print("==================================")


init_game()