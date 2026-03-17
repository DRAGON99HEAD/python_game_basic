import os
import random
import readchar

counter = False
slime_kills = 0
skeleton_kills = 0
dragon_kills = 0
goblin_kills = 0
ini_run = True
bow_d = 10
broken = 0
dp = 0
xp_earned = 0
parrying = False
parry_percent = 0

def clear():
    os.system("cls" if os.name == "nt" else "clear")

class jogador:

    def __init__(self, nome):
        self.nome = nome
        self.max_life = 100
        self.atual_life = 100
        self.speed = 10
        self.mana = 100
        self.defesa_base = 5
        self.defesa = 5
        self.duo_def = []
        self.defesa_parry = 0
        self.parry_ini = []
        self.inteligencia = 10
        self.dano_base = 5
        self.l_pocao = 2
        self.m_pocao = 2
        self.level = 1
        self.xp = 0
        self.max_xp = 100
        self.points = 0
        self.m_regen = random.randint(10, 1000)
        self.l_regen = random.randint(20, 100)

    def status(self):

        clear()

        print("\n==================== STATUS DO JOGADOR ====================")
        print(f"Nome: {self.nome}\t\tVida: {self.atual_life}/{self.max_life}")
        print(f"Mana: {self.mana}\t\t\tInteligência: {self.inteligencia}")
        print(f"Speed: {self.speed}\t\t\tDefesa: {self.defesa + self.defesa_parry}")
        print(f"Nível Atual: {self.level}\t\t\tXP: {self.xp}/{self.max_xp}")
        print(f"Dano Base {self.dano_base}\t\t\tPontos de Habilidade: {self.points}")
        print("===========================================================\n")

        if self.points > 0:

            print(f"Você possui {self.points} {'ponto' if self.points == 1 else 'pontos'} de habilidade para usar\n1 - Sim\n2 - Não")
            print("Deseja usar esses pontos?\n: ", end="", flush=True)
            use = readchar.readkey()

            match use:
                case "1":
                    status_upd()

        else:
            input("Pressione ENTER para continuar ...")

def status_upd():

    while player.points > 0:
        clear()

        print("===========================================================")
        print(f"1 - Vida máxima\t\t{player.max_life}\n2 - Velocidade\t\t{player.speed}\n3 - Defesa Base\t\t{player.defesa_base}\n4 - Inteligência\t{player.inteligencia}\n5 - Dano Base\t\t{player.dano_base}\n\t\t\t\t\t0 - Voltar")
        print("===========================================================")
        print(f"Você possui {player.points} {'ponto' if player.points == 1 else 'pontos'} de habilidade para usar\nEscolha um atributo para ser melhorado\n: ", end="", flush=True)
        
        upd = readchar.readkey()

        match upd:
            case "0":
                break
            case "1":
                player.max_life += 50
                player.points -= 1
            case "2":
                player.speed += 2
                player.points -= 1
            case "3":
                player.defesa_base += 3
                player.points -= 1
            case "4":
                player.inteligencia += 2
                player.points -= 1
            case "5":
                player.dano_base += 3
                player.points -= 1

def bolsa():

    clear()

    print("====================== BOLSA ======================")
    print(f"1 - Poção de vida: {player.l_pocao}\n2 - Poção de mana: {player.m_pocao}\n\t\t\t\t\t0 - VOLTAR")
    print("===================================================")
    print(": ", end="", flush=True)

    use_item = readchar.readkey()

    match use_item:
        case "1":
            clear()
            print("============================== POÇÃO DE VIDA ==============================")
            print("Está poção recupera 500 pontos de vida até alcançar a vida máxima")
            print("============================================================================")
            print(f"voçê possui {player.l_pocao} {'poções' if player.l_pocao > 1 else 'poção'} de vida gostaria de usar 1?\n1 - sim\n2 - não\n: ", end="", flush=True)
            
            use = readchar.readkey()

            match use:
                case "1":
                    clear()
                    if player.l_pocao > 0:
                        if player.atual_life == player.max_life:
                            print("Sua vida já está no máximo")
                            input("Pressione ENTER para continuar ...")
                        elif player.atual_life < player.max_life:
                            player.l_pocao -= 1
                            cura = (player.max_life - player.atual_life) - 500

                            if cura >= 0:
                                player.atual_life += 500
                                print("Sua vida foi cura em 500 pontos de vida")
                                input("Pressione ENTER para continuar ...")
                            elif cura < 0:
                                player.atual_life = player.atual_life + (500 + cura)
                                print(f"Sua vida foi curada em {500 + cura} {'pontos' if 500 + cura > 1 else 'ponto'}")
                                input("Pressione ENTER para continuar ...")
                    elif player.l_pocao <= 0:
                        print("Você não possui poções de vida")
                        input("Pressione ENTER para continuar ...")

        case "2":
            clear()
            print("============================== POÇÃO DE MANA ==============================")
            print("Está poção recupera 100 pontos de mana sem limite máximo")
            print("============================================================================")
            print(f"voçê possui {player.m_pocao} {'poções' if player.m_pocao > 1 else 'poção'} de mana gostaria de usar 1?\n1 - sim\n2 - não\n: ", end="", flush=True)
            
            use = readchar.readkey()

            match use:
                case "1":
                    if player.m_pocao > 0:
                        player.mana += 100
                        player.m_pocao -= 1
                        input(f"Sua mana foi aumentada em 100 pontos\nPressione ENTER para continuar ...")
                    elif player.m_pocao <= 0:
                        input("Você não possui poção de mana\nPressione ENTER para continuar ...")

def attacks():

    clear()

    print("============================ ATAQUES ============================")
    print("1 - Golpe de espada\n2 - Golpe de espada embuida em mana\t\tCUSTO: 5 MANA\n3 - Bola de fogo\t\t\t\tCUSTO: 10 MANA\n4 - Lança-Chamas\t\t\t\tCUSTO: 20 MANA\n5 - Tsunami\t\t\t\t\tCUSTO: 40 MANA\n6 - Jato de água\t\t\t\tCUSTO: 15 MANA\n\n\t\t\t\t\t\t0 - Voltar\n=================================================================")
    print(": ", end="", flush=True)
    
    move = readchar.readkey()
    clear()
    crit = 0
    go_to = 0
    r_crit = random.randint(0,100)
    
    if r_crit <= 10 or r_crit >= 90:
           crit = 1

    match move:
        
        case "1":
            if crit == 1:
                damage = max(10 * player.level,int(2 * (player.dano_base * player.speed) - (enemy.defense / 2)))
                enemy.life -= damage
                print(f"Dano crítico!!!\nVocê deu {damage} de dano no inimigo")
                input("Pressione ENTER para continuar ...")
                go_to = 1
            else:
                damage = max(5 * player.level,int((player.dano_base * player.speed) - (enemy.defense / 2)))
                enemy.life -= damage
                print(f"Você deu {damage} de dano no inimigo")
                input("Pressione ENTER para continuar ...")
                go_to = 1

        case "2":
            if crit == 1 and player.mana >= 5:
                damage = max(30 * player.level, int(2 * (player.dano_base * player.speed) * player.inteligencia - (enemy.defense / 2)))
                enemy.life -= damage
                player.mana -= 5
                print(f"Dano crítico!!!\nVocê deu {damage} de dano no inimigo")
                input("Pressione ENTER para continuar ...")
                go_to = 1
            elif player.mana >= 5:
                damage = max(15 * player.level, int((player.dano_base * player.speed) * player.inteligencia - (enemy.defense / 2)))
                enemy.life = enemy.life - damage
                player.mana -= 5
                print(f"Você deu {damage} de dano no inimigo")
                input("Pressione ENTER para continuar ...")
                go_to = 1
            else:
                print("Você não tem mana suficiente para usar este ataque")
                input("Pressione ENTER para continuar ...")

        case "3":
            if crit == 1 and player.mana >= 10:
                damage = max(50 * player.level, int(2 * (player.level * ((player.inteligencia * player.mana) * player.dano_base))))
                player.mana -= 10
                enemy.life = enemy.life - damage
                print(f"Dano crítico!!!\nVocê deu {damage} de dano no inimigo")
                input("Pressione ENTER para continuar ...")
                go_to = 1
            elif player.mana >= 10:
                damage = max(25 * player.level, int(player.level * ((player.inteligencia * player.mana) * player.dano_base)))
                player.mana -= 10
                enemy.life = enemy.life - damage
                print(f"Você deu {damage} de dano no inimigo")
                input("Pressione ENTER para continuar ...")
                go_to = 1
            else:
                print("Você não possui mana suficiente para este ataque")
                input("Pressione ENTER para continuar ...")

        case "4":
            if crit == 1 and player.mana >= 20:
                damage = max(100 * player.level, int(3.5 * (player.level * ( ((2 * player.inteligencia) * (4 * player.mana) * (player.dano_base * 1.5))) - (enemy.defense / 1.5))))
                player.mana -= 20
                enemy.life = enemy.life - damage
                print(f"Dano crítico!!!\nVocê deu {damage} de dano no inimigo")
                input("Pressione ENTER para continuar ...")
                go_to = 1
            elif player.mana >= 20:
                damage = max(50 * player.level, int(player.level * ( ((2 * player.inteligencia) * (4 * player.mana) * (player.dano_base * 1.5))) - (enemy.defense / 1.5)))
                player.mana -= 20
                enemy.life = enemy.life - damage
                print(f"Você deu {damage} de dano no inimigo")
                input("Pressione ENTER para continuar ...")
                go_to = 1
            else:
                print("Você não possui mana suficiente para este ataque")
                input("Pressione ENTER para continuar ...")

        case "5":
            wave_meters = player.mana / 40
            if wave_meters >= 50:
                wave_meters = 50
            if player.mana >= 40:
                damage = max(250 * player.level, int(player.level * ( (10 * player.inteligencia) * (wave_meters * player.mana)) - (enemy.defense / 10)))
                enemy.life -= damage
                player.mana -= 40
                print(f"Você deu {damage} de dano no inimigo")
                input("Pressione ENTER para continuar ...")
                go_to = 1
            else:
                print("Você não possui mana o suficiente para usar este ataque")
                input("Pressione ENTER para continuar ...")

        case "6":
            PSI = random.randint(0,16)
            if PSI >= 13:
                r_crit +=  40
            elif PSI >= 10:
                r_crit += 20
            elif PSI >= 5:
                r_crit += 5

            if r_crit <= 10 or r_crit >= 90:
                crit = 1

            damage = max(75 * player.level, int(player.level * ( ( (player.inteligencia * (player.mana / 4.5)) * PSI)) - enemy.defense))

            if crit == 1 and player.mana >= 15:
                damage = damage * 2
                enemy.life = enemy.life - damage
                player.mana -= 15
                print(f"Dano crítico!!!\nVocê deu {damage} de dano no inimigo")
                input("Pressione ENTER para continuar ...")
                go_to = 1
            elif player.mana >= 15:
                enemy.life = enemy.life - damage
                player.mana -= 15
                print(f"Você deu {damage} de dano no inimigo")
                input("Pressione ENTER para continuar ...")
                go_to = 1
            else:
                print("Você não possui mana suficiente para usar este ataque")
                input("Pressione ENTER para continuar ...")

    if enemy.life > 0 and go_to == 1:
        enemy_attacks()

def defense():
    global parrying, parry_percent

    clear()

    print("========================== DEFESA ==========================")
    print("1 - Defesa dupla\n2 - Cura\n3 - Parry\n4 - Contra-ataque\n\n\t\t\t\t\t\t0 - Voltar\n============================================================")
    print(": ", end="", flush=True)

    defe = readchar.readkey()
    clear()

    match defe:
        case "1":
            print("========================== DEFESA DUPLA ==========================")
            print("A defesa do jogador é dobrada sem nenhuma restrição\nporém dura por 5 rounds")
            print("CUSTO: 15 Pontos de mana por uso")
            print("==================================================================")
            print("1 - Sim\n2 - Não\nDeseja usar?\n: ", end="", flush=True)
            
            use = readchar.readkey()
            clear()

            match use:
                case "1":
                    if player.mana >= 15:
                        player.mana -= 15
                        player.defesa = int(player.defesa * 2)
                        player.duo_def.append(5)
                        print(f"A sua defesa foi dobra de {int(player.defesa/2)} para {player.defesa}")
                        input("Pressione ENTER para continuar ...")

                        enemy_attacks()
                    elif player.mana < 15:
                        print("Você não possui mana suficiente para usar o defesa dupla")
                        input("Pressione ENTER para continuar ...")

        case "2":
            cure_points = int(20 * (0.25 * player.inteligencia))
            print("========================== CURA ==========================")
            print(f"Cura o jogador em {cure_points} pontos de vida")
            print("CUSTO: 20 Pontos de mana por uso")
            print("==========================================================")
            print("1 - Sim\n2 - Não\nDeseja usar?\n: ", end="", flush=True)
            
            use = readchar.readkey()
            clear()

            match use:
                 case "1":
                      
                      if player.mana < 20:
                         print("Você não possui mana o suficiente para usar CURA")
                         input("Pressione ENTER para continuar ...")
                      elif player.mana >= 20:

                        if player.atual_life == player.max_life:
                             print("Sua vida já está no máximo")
                             input("Pressione ENTER para continuar ...")
                        elif player.atual_life < player.max_life:
                            player.mana -= 20
                            cura = (player.max_life - player.atual_life) - cure_points
                            if cura >= 0:
                                player.atual_life += cure_points
                                print(f"Sua vida foi cura em {cure_points} pontos de vida")
                                input("Pressione ENTER para continuar ...")
                            elif cura < 0:
                                player.atual_life = player.atual_life + (cure_points + cura)
                                print(f"Sua vida foi curada em {cure_points + cura} {'pontos' if cure_points + cura > 1 else 'ponto'}")
                                input("Pressione ENTER para continuar ...")

        case "3":

            print("========================== PARRY ==========================")
            print(f"Dependendo da sua velocidade você reduzira até 100% do")
            print("ataque do inimigo e aumenta a sua defesa em 5 pontos")
            print("por 5 rounds")
            print("CUSTO: 30 Pontos de mana por uso")
            print("==========================================================")
            print("1 - Sim\n2 - Não\nDeseja usar?\n: ", end="", flush=True)

            use = readchar.readkey()

            clear()
            match use:

                case "1":

                    if player.mana >= 30:

                        parry_percent = player.speed * 0.1
                        if parry_percent >= 100:

                            parry_percent = 100
                        parrying = True
                        player.defesa_parry += 5
                        player.parry_ini.append(5)
                        player.mana -= 30

                        print(f"Você irá bloquear o ataque inimigo em {int(parry_percent)}%\nSua defesa foi aumentada em 5 pontos")
                        input("Pressione ENTER para continuar ...")
                        
                        enemy_attacks()
                    else:
                        print("Você não tem mana suficiente para usar o parry")
                        input("Pressione ENTER para continuar ...")

class inimigo():

    def __init__(self):

        global xp_earned
        
        r_type = random.randint(0,100)

        if r_type > 75:
            self.name = "DRAGÃO"
            D_intel = random.randint(5,255)
            D_mana = random.randint(50,2550)
            D_forca = random.randint(10,510)
            D_couraca = random.randint(10,510)
            self.life = int(100 * (D_couraca * D_intel))
            self.defense = int(D_couraca * D_forca)
            self.force = int((D_forca * D_intel) + D_mana)
            self.intel =  int(D_intel + D_mana)

        elif r_type > 50:
            self.name = "GOBLIN"
            G_speed = random.randint(5,255)
            G_force = random.randint(5,255)
            G_deter = random.randint(5,255)
            G_agility = random.randint(5,255)
            G_sharp = random.randint(5,255)
            self.life = int(G_agility * G_force + (2 * G_deter))
            self.defense = int(G_speed * G_agility)
            self.force = int(G_agility * G_sharp)
            self.intel = int((G_sharp * G_deter) / 45)

        elif r_type > 25:
            self.name = "ESQUELETO"
            calcio = random.randint(50,255)
            fosforo = random.randint(50,255)
            fosfato = random.randint(25,255)
            self.life = int(fosforo * fosfato)
            self.defense = int(fosfato / 2)
            self.force = int((calcio + fosforo) / 15 + fosfato)
            self.intel = 0

        elif r_type >= 0:
            self.name = "SLIME"
            S_acid = random.randint(1,21)
            S_density = random.randint(1,100)
            S_size = random.randint(1,10)
            self.life = int(S_size * S_density)
            self.defense = int((S_acid * S_density) / S_size)
            self.force = int(S_acid * S_density)
            self.intel = 0

        if self.intel > 0:
            xp_earned = int((self.defense / 4) + (self.force / 4) + (self.life / 4) + (self.intel / 4))
        elif self.intel == 0:
            xp_earned = int((self.defense / 4) + (self.force / 4) + (self.life / 4))

def enemy_attacks():

    global bow_d, broken, dp, parrying, parry_percent, counter
    block = 0

    clear()

    if bow_d <= 0 and dp == 0:
        broken = 1

    ea = random.randint(1,3)

    if enemy.name == "DRAGÃO":
        match ea:
            case 1:
                damage = max(0, int((enemy.force + enemy.intel) - (player.defesa + player.defesa_parry)))
                if parrying == True:
                    block = int(damage * (parry_percent / 100))
                player.atual_life -= damage - block
                counter = True
                print(f"O dragão usou LIGHTNING STRIKE causando {damage - block} de dano ao jogador {player.nome}")
                input("Pressione ENTER para continuar ...")
            case 2:
                damage = max(0, int((enemy.life / 10) + (enemy.defense / 25) - (player.defesa + player.defesa_parry)))
                if parrying == True:
                    block = int(damage * (parry_percent / 100))
                player.atual_life -= damage - block
                counter = True
                print(f"O dragão usou INVESTIDA causando {damage - block} de dano ao jogador {player.nome}")
                input("Pressione ENTER para continuar ...")
            case 3:
                damage = max(0, int((enemy.force / 4.5) - (player.defesa + player.defesa_parry)))
                if parrying == True:
                    block = int(damage * (parry_percent / 100))
                player.atual_life -= damage - block
                counter = True
                print(f"O dragão usou ARRANHÃO causando {damage - block} de dano ao jogador {player.nome}")
                input("Pressione ENTER para continuar ...")

    elif enemy.name == "SLIME":
        match ea:
            case 1:
                damage = max(0, int(enemy.force * (enemy.life / 2.5) - (player.defesa + player.defesa_parry)))
                if parrying == True:
                    block = int(damage * (parry_percent / 100))
                player.atual_life -= damage - block
                counter = True
                print(f"O slime usou TIRO ÁCIDO causando {damage - block} de dano ao jogador {player.nome}")
                input("Pressione ENTER para continuar ...")
            case 2:
                damage = max(0, int((enemy.life * enemy.defense + enemy.force) - (player.defesa + player.defesa_parry)))
                if parrying == True:
                    block = int(damage * (parry_percent / 100))
                player.atual_life -= damage - block
                counter = True
                print(f"O slime usou INVESTIDA causando {damage - block} de dano ao jogador {player.nome}")
                input("Pressione ENTER para continuar ...")
            case 3:
                pre = enemy.life
                enemy.life += enemy.life * 0.25
                counter = True
                print(f"O slime usou regrowth aumentando a sua vida em {pre * 0.25}")
                input("Pressione ENTER para continuar ...")

    elif enemy.name == "GOBLIN":
        match ea:
            case 1:
                damage = max(0, enemy.intel)
                if parrying == True:
                    block = int(damage * (parry_percent / 100))
                player.atual_life -= damage - block
                enemy.life += damage - block
                counter = True
                print(f"O goblin usou THIEF para recuperar a propria vida em {enemy.intel} e causando ao jogador {player.nome} um dano de {enemy.intel}")
                input("Pressione ENTER para continuar ...")
            case 2:
                damage = max(0, int((enemy.force * 2.5) - (player.defesa + player.defesa_parry)))
                if parrying == True:
                    block = int(damage * (parry_percent / 100))
                player.atual_life -= damage - block
                counter = True
                print(f"O goblin usou APUNHALADA causando {damage - block} de dano ao jogador {player.nome}")
                input("Pressione ENTER para continuar ...")
            case 3:
                damage = max(0, int((enemy.force + enemy.intel) - (player.defesa + player.defesa_parry)))
                if parrying == True:
                    block = int(damage * (parry_percent / 100))
                player.atual_life -= damage - block
                counter = True
                print(f"O goblin usou CHUTE causando {damage - block} de dano ao jogador {player.nome}")
                input("Pressione ENTER para continuar ...")

    elif enemy.name == "ESQUELETO":
        if ea == 2 and bow_d <= 0:
            ea = 1
        elif ea == 1 and broken >= 1:
            ea = 2

        match ea:
            case 1:
                damage = max(0, int(enemy.force - (player.defesa + player.defesa_parry)))
                if parrying == True:
                    block = int(damage * (parry_percent / 100))
                player.atual_life -= damage - block
                bow_d -= 1
                counter = True
                print(f"O esqueleto usou FLECHADA causando {damage - block} de dano ao jogador {player.nome}")
                input("Pressione ENTER para continuar ...")
            case 2:
                damage = max(0, int((enemy.force + enemy.intel) - (player.defesa + player.defesa_parry)))
                if parrying == True:
                    block = int(damage * (parry_percent / 100))
                player.atual_life -= damage - block
                if broken == 1:
                    counter = True
                    print(f"O esqueleto usou tanto o arco que ele quebrou então está usando SOCO e causou {damage - block} de ao jogador {player.nome}")
                    input("Pressione ENTER para continuar ...")
                    broken = 0
                else:
                    counter = True
                    print(f"O esqueleto usou SOCO causando {damage - block} de dano ao jogador {player.nome}")
                    input("Pressione ENTER para continuar ...")
            case 3:
                damage = max(0, int((enemy.defense + enemy.force) - (player.defesa + player.defesa_parry)))
                if parrying == True:
                    block = int(damage * (parry_percent / 100))
                player.atual_life -= damage - block
                counter = True
                print(f"O esqueleto usou SCRATCH causando {damage - block} de dano ao jogador {player.nome}")
                input("Pressione ENTER para continuar ...")
    
while ini_run == True:

    clear()
    print("===========================================\n\tJOGO BÁSICO DE RPG EM PYTHON\n===========================================\n")

    nome_personagem = input(f"Insira o nome do seu personagem: ")
    player = jogador(nome_personagem)

    playing = True

    while player.atual_life > 0 and playing == True:
        round = 1
        enemy = inimigo()

        while player.atual_life > 0 and enemy.life > 0 and playing == True:

            if player.defesa < player.defesa_base:
                player.defesa = player.defesa_base

            clear()
            if parrying == True:
                parrying = False
        
            print(f"==================================================================\n\n\tJOGADOR: {player.nome}\tVIDA: {player.atual_life}/{player.max_life}\tMANA: {player.mana}")
            print(f"\n\tROUND: {round}\n\n\tINIMIGO: {enemy.name}\t\tVIDA: {enemy.life}\n\n======================== ESCOLHA UMA AÇÃO ========================")
            print("\t1 - Ataques\t\t\t2 - Defesa\n\t3 - Bolsa\t\t\t4 - Status\n\n\t\t\t\t\t0 - Sair\n\n: ", end="", flush=True)
            
            option = readchar.readkey()

            match option:
                case "1":
                    attacks()
                case "2":
                    defense()
                case "3":
                    bolsa()
                case "4":
                    player.status()
                case "0":
                    playing = False

            if counter == True:
                round += 1
                player.mana += player.m_regen
                            
                if player.atual_life < player.max_life:
                            
                    cura = (player.max_life - player.atual_life) - player.l_regen
                    if cura >= 0:
                            
                        player.atual_life += player.l_regen

                    elif cura < 0:
                        
                        player.atual_life = player.atual_life + (player.l_regen + cura)

                for i in range(len(player.duo_def) - 1, -1, -1):
                    player.duo_def[i] -= 1

                    if player.duo_def[i] <= 0:
                        player.defesa = int(player.defesa / 2)
                        player.duo_def.pop(i)

                for i in range(len(player.parry_ini) - 1, -1, -1):
                    player.parry_ini[i] -= 1

                    if player.parry_ini[i] <= 0:
                        player.defesa_parry -= 5
                        player.parry_ini.pop(i)
                        
                counter = False

        if enemy.life <= 0:
            player.xp += xp_earned
            clear()
            print(f"Você recebeu {xp_earned} de xp ao matar o inimigo")
            input("Pressione ENTER para continuar ...")
            clear()

            level_before = player.level

            while player.xp >= player.max_xp:
                player.level += 1
                player.xp -= player.max_xp
                player.max_xp += 20
                player.points += 3
                player.max_life += 10
                player.mana += 20

            if player.level > level_before:
                print(f"Você upou {player.level - level_before} {'nível' if player.level - level_before == 1 else 'níveis'}!")
                input("Pressione ENTER para continuar ...")

            if enemy.name == "SLIME":
                slime_kills += 1
                clear()
                print("=================================================")
                print(f"Você matou o inimigo {enemy.name} totalizando um total de {slime_kills} {'assassinato' if slime_kills == 1 else 'assassinatos'}")
                print("=================================================")
                input("Pressione ENTER para continuar ...")

            elif enemy.name == "GOBLIN":
                goblin_kills += 1
                clear()
                print("=================================================")
                print(f"Você matou o inimigo {enemy.name} totalizando um total de {goblin_kills} {'assassinato' if goblin_kills == 1 else 'assassinatos'}")
                print("=================================================")
                input("Pressione ENTER para continuar")

            elif enemy.name == "DRAGÃO":
                dragon_kills += 1
                clear()
                print("=================================================")
                print(f"Você matou o inimigo {enemy.name} totalizando um total de {dragon_kills} {'assassinato' if dragon_kills == 1 else 'assassinatos'}")
                print("=================================================")
                input("Pressione ENTER para continuar ...")

            elif enemy.name == "ESQUELETO":
                skeleton_kills += 1
                dp = 0
                bow_d = 10
                clear()
                print("=================================================")
                print(f"Você matou o inimigo {enemy.name} totalizando um total de {skeleton_kills} {'assassinato' if skeleton_kills == 1 else 'assassinatos'}")
                print("=================================================")
                input("Pressione ENTER para continuar ...")

            rest = 0
            clear()
            print("Você gostaria de descansar para recuperar vida e mana?")
            print("1 - Sim\n2 - Não\n: ", end="", flush=True)
            
            rest = readchar.readkey()

            match rest:
                case "1":
                    mana_regen = random.randint(20,250)
                    player.mana += mana_regen
                    player.atual_life = player.max_life
                    print(f"\nVocê descansou e recuperou sua vida por completo e sua mana foi recuperada em {mana_regen} pontos")
                    input("Pressione ENTER pata continuar ...")
    
    if player.atual_life <= 0:
        clear()
        print("Você morreu!!!\n1 - Sim\n2 - Não\nDeseja jogar novamente?\n: ", end="", flush=True)
        A = readchar.readkey()

        match A:
            case "2":
                ini_run = False
