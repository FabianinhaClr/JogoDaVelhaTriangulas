def tab_triangular(A, B, C, D, E, F, G, H, I):
 out = f'({A})'.center(60) + ('\n' * 5) + f'({B})\n'.center(45)
 out += ' ' * 16 + f'({C})\n' + ' ' * 29 + f'({D})\n' + ' ' * 22 + f'({E})\n\n'
 out += f'({F})'.center(49)
 out += ('\n' * 7) + f'({G})' + ' ' * 10 + f'({H})' + ' ' * 45 + f'({I})'
 return out

def verifica_ganhador(A, B, C, D, E, F, G, H, I):
   return A == B and B == G \
     or G == A and A == B \
     or A == C and C == I \
     or B == D and D == I \
     or I == C and C == A \
     or A == E and E == H \
     or H == E and E == A \
     or B == E and E == F \
     or F == E and E == B \
     or B == D and D == I \
     or I == D and D == B \
     or D == E and E == C \
     or E == D and D == C \
     or C == F and F == G \
     or G == F and F == C \
     or D == F and F == H

def deu_velha(A, B, C, D, E, F, G, H, I):
   return A != "1" \
     and B != "2" \
     and C != "3" \
     and D != "4" \
     and E != "5" \
     and F != "6" \
     and G != "7" \
     and H != "8" \
     and I != "9"

A, B, C, D, E, F, G, H, I = "1", "2", "3", "4", "5", "6", "7", "8", "9"

while True:
    aceitar = input("Olá Jogadores! Sejam bem vindos ao Jogo da Velha Triangular, vamos começar?")
    if aceitar == "SIM" or aceitar == "sim":
     print("OK, entendi que estão ansiosos e preparados, mas vamos repassar as regras, e relembrar-los como se joga: \
           São dois participantes, o primeiro poderá escolher se quer jogar X ou O, e o objetivo é completar 3 espaços do tabuleiro que são conjuntos, sendo eles: \
           (1, 2, 7), (1, 3, 9), (1, 5, 8), (2, 5, 6), (2, 4, 9), (5, 4, 3), (3, 6, 7), (4, 6, 8) \
           e caso todas as casas estiverem ocupadas e não houve vitória de niguém, dará Velha \
           Agora que vocês entenderam como funciona o jogo, espero que se divirtam. Bom jogo e boa sorte a amba das partes.")
     print("Atenciosamente, Clara Antonelo!")

     jogador = input("Qual você escolhe: X ou O?")

     while not verifica_ganhador(A, B, C, D, E, F, G, H, I):
         print(tab_triangular(A, B, C, D, E, F, G, H, I))
         casa = input(f"Jogador {jogador} escolha uma casa para marcar:")
         if casa == "1" and A == "1":
             A = jogador
         elif casa == "2" and B == "2":
             B = jogador
         elif casa == "3" and C == "3":
             C = jogador
         elif casa == "4" and D == "4":
             D = jogador
         elif casa == "5" and E == "5":
             E = jogador
         elif casa == "6" and F == "6":
             F = jogador
         elif casa == "7" and G == "7":
             G = jogador
         elif casa == "8" and H == "8":
             H = jogador
         elif casa == "9" and I == "9":
             I = jogador
         else:
             print("OPS.. esta casa não existe ou já esta ocupada. TENTE NOVAMENTE!")
         continue

         if verifica_ganhador(A, B, C, D, E, F, G, H, I):
            print(f"QUE LEGAL!! Parabéns {jogador} você venceu o jogo!!")

         jogador = "O" if jogador == "X" else "X"

         if deu_velha(A, B, C, D, E, F, G, H, I):
             print("O jogo terminou em empate. Deu Velha!!")

             break

     A, B, C, D, E, F, G, H, I = "1", "2", "3", "4", "5", "6", "7", "8", "9"

else:
     break
