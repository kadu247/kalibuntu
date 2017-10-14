#!/usr/bin/python3

import os
import sys
import traceback
import time


def inicio():
    try:
        if not os.geteuid() == 0:
            os.system('clear')
            print('''\033[33m_  _ ____ _    _ ___  _  _ _  _ ___ _  _
|_/  |__| |    | |__] |  | |\ |  |  |  |
| \_ |  | |___ | |__] |__| | \|  |  |__|\033[mv1.0
---------- https://\033[37mnux\033[34mware\033[m.gq ----------
             
      \033[31mTens que ter privilégio root\033[m
       
        → ex: \033[32msudo ./kalibuntu\033[m ←
            ''')

        else:

            def menu():
                while True:
                    os.system('clear')
                    print('''\033[33m_  _ ____ _    _ ___  _  _ _  _ ___ _  _
|_/  |__| |    | |__] |  | |\ |  |  |  |
| \_ |  | |___ | |__] |__| | \|  |  |__|\033[mv1.0
---------- https://\033[37mnux\033[34mware\033[m.gq ----------                    
                    
(1) Adicionar/Remover repositório do kali linux 
(2) Ver categorias
(3) Instruções
(0) Saír
                    ''')
                    opcao = input('↳ ')
                    while opcao == '1':
                        os.system('clear')
                        print('''\033[33m_  _ ____ _    _ ___  _  _ _  _ ___ _  _
|_/  |__| |    | |__] |  | |\ |  |  |  |
| \_ |  | |___ | |__] |__| | \|  |  |__|\033[mv1.0
---------- https://\033[37mnux\033[34mware\033[m.gq ----------                    
                    
(1) ADICIONAR repositório kali linux
(2) REMOVER repositório kali linux
(0) Voltar
                        ''')
                        repo = input('↳ ')
                        if repo == '1':
                            os.system('clear')
                            print('A adicionar chave GPG\n')
                            time.sleep(3)
                            os.system('wget https://www.kali.org/archive-key.asc')
                            os.system('mv archive-key.asc /etc/apt/trusted.gpg.d')
                            print('\nOK')
                            time.sleep(3)
                            os.system('clear')
                            print('A adicionar repositório\n')
                            time.sleep(3)
                            os.system('echo "# Kali linux repositories | kalibuntu | http://nuxware.gq\ndeb '
                                      'http://http.kali.org/kali kali-rolling main contrib non-free" >> '
                                      '/etc/apt/sources.list.d/kali-repo.list')
                            print('\nOK')
                            time.sleep(3)
                            os.system('clear')
                            print('A actualizar repositórios\n')
                            time.sleep(3)
                            os.system('apt update')
                            print('\nOk')
                            time.sleep(3)
                        elif repo == '2':
                            os.system('clear')
                            print('A remover chave GPG\n')
                            time.sleep(3)
                            os.system('sudo rm /etc/apt/trusted.gpg.d/archive-key.asc')
                            print('\nOK')
                            time.sleep(3)
                            os.system('clear')
                            print('A remover repositório\n')
                            time.sleep(3)
                            os.system('sudo rm /etc/apt/sources.list.d/kali-repo.list')
                            print('\nOK')
                            time.sleep(3)
                            os.system('clear')
                            print('A actualizar repositórios\n')
                            time.sleep(3)
                            os.system('sudo apt update')
                            print('\nOk')
                            time.sleep(3)
                        elif repo == '0':
                            menu()
                        else:
                            print('\nOpção inválida\n')
                            time.sleep(2)
                    
                    while opcao == '2':
                        def catmenu():
                            os.system('clear')
                            print('''\033[33m_  _ ____ _    _ ___  _  _ _  _ ___ _  _
|_/  |__| |    | |__] |  | |\ |  |  |  |
| \_ |  | |___ | |__] |__| | \|  |  |__|\033[mv1.0
---------- https://\033[37mnux\033[34mware\033[m.gq ----------

(1) Obtenção de Informação       (8) Ferramentas de esploração
(2) Análise de Vulnerabilidade   (9) Ferramentas Forenses
(3) Ataque a Redes Wireless     (10) Testes de Stress
(4) Aplicações Web              (11) Ataques a Passwords
(5) Sniffing e Spoofing         (12) Engenharia Reversa
(6) Manutenção de Acessos       (13) Modificações a Hardware
(7) Ferramentas de ralatórios   (14) Extra

(0) Voltar
                        ''')
                            cat = input('↳ ')
                            while cat == '1':
                                os.system('clear')
                                print('''\033[33m_  _ ____ _    _ ___  _  _ _  _ ___ _  _
|_/  |__| |    | |__] |  | |\ |  |  |  |
| \_ |  | |___ | |__] |__| | \|  |  |__|\033[mv1.0
---------- https://\033[37mnux\033[34mware\033[m.gq ----------

 (1) acccheck             (30) lbd
 (2) ace-voip             (31) Maltego Teeth
 (3) Amap                 (32) masscan
 (4) Automater            (33) Metagoofil
 (5) bing-ip2hosts        (34) Miranda
 (6) braa                 (35) Nmap
 (7) CaseFile             (36) ntop
 (8) CDPSnarf             (37) p0f
 (9) cisco-torch          (38) Parsero
(10) Cookie Cadger        (39) Recon-ng
(11) copy-router-config   (40) SET
(12) DMitry               (41) smtp-user-enum
(13) dnmap                (42) snmpcheck
(14) dnsenum              (43) sslcaudit
(15) dnsmap               (44) SSLsplit
(16) DNSRecon             (45) sslstrip
(17) dnstracer            (46) SSLyze
(18) dnswalk              (47) THC-IPV6
(19) DotDotPwn            (48) theHarvester
(20) enum4linux           (49) TLSSLed
(21) enumIAX              (50) twofi
(22) exploitdb            (51) URLCrazy
(23) Fierce               (52) Wireshark
(24) Firewalk             (53) WOL-E
(25) fragroute            (54) Xplico
(26) fragrouter           (55) iSMTP
(27) Ghost Phisher        (56) InTrace
(28) GoLismero            (57) hping3
(29) goofile

(0) Voltar
                                ''')
                                opcao01 = input('↳ ')
                                if opcao01 == '1':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '2':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '3':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '4':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '5':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '6':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '7':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '8':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '9':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '10':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '11':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '12':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '13':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '14':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '15':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '16':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '17':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '18':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '19':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '20':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '21':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '22':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '23':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '24':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '25':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '26':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '27':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '28':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '29':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '30':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '31':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '32':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '33':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '34':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '35':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '36':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '37':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '38':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '39':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '40':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '41':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '42':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '43':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '44':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '45':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '46':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '47':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '48':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '49':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '50':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '51':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '52':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '53':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '54':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '55':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '56':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao01 == '57':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)                                                    
                                elif opcao01 == '0':
                                    catmenu()
                                else:
                                    print('\nOpção inválida\n')
                                    time.sleep(2)
                            
                            while cat == '2':
                                os.system('clear')
                                print('''\033[33m_  _ ____ _    _ ___  _  _ _  _ ___ _  _
|_/  |__| |    | |__] |  | |\ |  |  |  |
| \_ |  | |___ | |__] |__| | \|  |  |__|\033[mv1.0
---------- https://\033[37mnux\033[34mware\033[m.gq ----------

 (1) BBQSQL                         (18) Nmap
 (2) BED                            (19) ohrwurm
 (3) cisco-auditing-tool            (20) openvas-administrator
 (4) cisco-global-exploiter         (21) openvas-cli
 (5) cisco-ocs                      (22) openvas-manager
 (6) cisco-torch                    (23) openvas-scanner
 (7) copy-router-config             (24) Oscanner
 (8) commix                         (25) Powerfuzzer
 (9) DBPwAudit                      (26) sfuzz
(10) DoonaDot                       (27) SidGuesser
(11) DotPwn                         (28) SIPArmyKnife
(12) Greenbone Security Assistant   (29) sqlmap
(13) GSD                            (30) Sqlninja
(14) HexorBase                      (31) sqlsus
(15) Inguma                         (32) THC-IPV6
(16) jSQL                           (33) tnscmd10g
(17) Lynis                          (34) unix-privesc-check
					                (35) Yersinia

(0) Voltar
                                ''')
                                opcao02 = input('↳ ')
                                if opcao02 == '1':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao02 == '2':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao02 == '3':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao02 == '4':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao02 == '5':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao02 == '6':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao02 == '7':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao02 == '8':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao02 == '9':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao02 == '10':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao02 == '11':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao02 == '12':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao02 == '13':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao02 == '14':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao02 == '15':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao02 == '16':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao02 == '17':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao02 == '18':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao02 == '19':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao02 == '20':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao02 == '21':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao02 == '22':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao02 == '23':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao02 == '24':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao02 == '25':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao02 == '26':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao02 == '27':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao02 == '28':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao02 == '29':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao02 == '30':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao02 == '31':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao02 == '32':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao02 == '33':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao02 == '34':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao02 == '35':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)                                
                                elif opcao02 == '0':
                                    catmenu()
                                else:
                                    print('\nOpção inválida\n')
                                    time.sleep(2)
                            while cat == '3':
                                os.system('clear')
                                print('''\033[33m_  _ ____ _    _ ___  _  _ _  _ ___ _  _
|_/  |__| |    | |__] |  | |\ |  |  |  |
| \_ |  | |___ | |__] |__| | \|  |  |__|\033[mv1.0
---------- https://\033[37mnux\033[34mware\033[m.gq ----------

 (1) Aircrack-ng         (16) kalibrate-rtl
 (2) Asleap              (17) KillerBee
 (3) Bluelog             (18) Kismet
 (4) BlueMaho            (19) mdk3
 (5) Bluepot             (20) mfcuk
 (6) BlueRanger          (21) mfoc
 (7) Bluesnarfer         (22) mfterm
 (8) Bully               (23) Multimon-NG
 (9) coWPAtty            (24) PixieWPS
(10) crackle             (25) Reaver
(11) eapmd5pass          (26) redfang
(12) Fern Wifi Cracker   (27) RTLSDR Scanner
(13) Ghost Phisher       (28) Spooftooph
(14) GISKismet           (39) Wifi Honey
(15) gr-scan             (30) Wifitap 
                         (31) Wifite 
				
(0) Voltar
                                ''')
                                opcao03 = input('↳ ')
                                if opcao03 == '1':
                                    os.system('clear')
                                    print('A instalar Aircrack-ng\n')          
                                    os.system('apt install aircrack-ng')
                                    print('\nOK')
                                    time.sleep(2)
                                elif opcao03 == '2':
                                    os.system('clear')
                                    print('A instalar Asleap\n')             
                                    os.system('apt install asleap')        
                                    print('\nOK')                   
                                    time.sleep(2)
                                elif opcao03 == '3':
                                    os.system('clear')
                                    print('A instalar Bluelog\n')             
                                    os.system('apt install bluelog')        
                                    print('\nOK')                   
                                    time.sleep(2)
                                elif opcao03 == '4':
                                    os.system('clear')
                                    print('A colonar BlueMaho\n')             
                                    os.system('apt install git && git clone git://git.kali.org/packages/bluemaho.git')        
                                    print('\nOK')                   
                                    time.sleep(2)
                                elif opcao03 == '5':
                                    os.system('clear')
                                    print('A colonar Bluepot\n')             
                                    os.system('apt install git && git clone git://git.kali.org/packages/bluepot.git')        
                                    print('\nOK')                   
                                    time.sleep(2)
                                elif opcao03 == '3':
                                    os.system('clear')
                                    print('A instalar Blueranger\n')             
                                    os.system('apt install blueranger')        
                                    print('\nOK')   
                                elif opcao03 == '7':
                                    os.system('clear')
                                    print('A instalar Bluesnarfer\n')             
                                    os.system('apt install bluesnarfer')        
                                    print('\nOK')   
                                elif opcao03 == '8':
                                    os.system('clear')
                                    print('A instalar Bully\n')             
                                    os.system('apt install bully')        
                                    print('\nOK')
                                elif opcao03 == '9':
                                    os.system('clear')
                                    print('A instalar coWPAtty\n')             
                                    os.system('apt install cowpatty')        
                                    print('\nOK')
                                elif opcao03 == '10':
                                    os.system('clear')
                                    print('A instalar crackle\n')             
                                    os.system('apt install crackle')        
                                    print('\nOK')
                                elif opcao03 == '11':
                                    os.system('clear')
                                    print('A instalar eapmd5pass\n')             
                                    os.system('apt install eapmd5pass')        
                                    print('\nOK')
                                elif opcao03 == '12':
                                    os.system('clear')
                                    print('A instalar Fern Wifi Cracker\n')             
                                    os.system('apt install fern-wifi-cracker')        
                                    print('\nOK')
                                elif opcao03 == '13':
                                    os.system('clear')
                                    print('A instalar Ghost Phisher\n')             
                                    os.system('apt install ghost-phisher')        
                                    print('\nOK')
                                elif opcao03 == '14':
                                    os.system('clear')
                                    print('A instalar GISKismet\n')             
                                    os.system('apt install giskismet')        
                                    print('\nOK')
                                elif opcao03 == '15':
                                    os.system('clear')
                                    print('A colonar gr-scan\n')             
                                    os.system('apt install git && git clone git://git.kali.org/packages/gr-scan.git')        
                                    print('\nOK')
                                elif opcao03 == '16':
                                    os.system('clear')
                                    print('A instalar kalibrate-rtl\n')             
                                    os.system('apt install kalibrate-rtl')        
                                    print('\nOK')
                                elif opcao03 == '17':
                                    os.system('clear')
                                    print('A instalar KillerBee\n')             
                                    os.system('apt install killerbee')        
                                    print('\nOK')
                                elif opcao03 == '18':
                                    os.system('clear')
                                    print('A instalar Kismet\n')             
                                    os.system('apt install kismet')        
                                    print('\nOK')
                                elif opcao03 == '19':
                                    os.system('clear')
                                    print('A instalar mdk3\n')             
                                    os.system('apt install mdk3')        
                                    print('\nOK')
                                elif opcao03 == '20':
                                    os.system('clear')
                                    print('A instalar mfcuk\n')             
                                    os.system('apt install mfcuk')        
                                    print('\nOK')
                                elif opcao03 == '21':
                                    os.system('clear')
                                    print('A instalar mfoc\n')             
                                    os.system('apt install mfoc')        
                                    print('\nOK')
                                elif opcao03 == '22':
                                    os.system('clear')
                                    print('A instalar mfterm\n')             
                                    os.system('apt install mfterm')        
                                    print('\nOK')
                                elif opcao03 == '23':
                                    os.system('clear')
                                    print('A instalar Multimon-NG\n')             
                                    os.system('apt install multimon-ng')        
                                    print('\nOK')
                                elif opcao03 == '24':
                                    os.system('clear')
                                    print('A instalar PixieWPS\n')             
                                    os.system('apt install pixiewps')        
                                    print('\nOK')
                                elif opcao03 == '25':
                                    os.system('clear')
                                    print('A instalar Reaver\n')             
                                    os.system('apt install reaver')        
                                    print('\nOK')
                                elif opcao03 == '26':
                                    os.system('clear')
                                    print('A instalar redfang\n')             
                                    os.system('apt install redfang')        
                                    print('\nOK')
                                elif opcao03 == '27':
                                    os.system('clear')
                                    print('A instalar RTLSDR Scanner\n')             
                                    os.system('apt install rtlsdr-scanner')        
                                    print('\nOK')
                                elif opcao03 == '28':
                                    os.system('clear')
                                    print('A instalar Spooftooph\n')             
                                    os.system('apt install spooftooph')        
                                    print('\nOK')
                                elif opcao03 == '29':
                                    os.system('clear')
                                    print('A instalar Wifi Honey\n')             
                                    os.system('apt install wifi-honey')        
                                    print('\nOK')
                                elif opcao03 == '30':
                                    os.system('clear')
                                    print('A instalar Wifitap\n')             
                                    os.system('apt install wifitap')        
                                    print('\nOK')
                                elif opcao03 == '31':
                                    os.system('clear')
                                    print('A instalar Wifite\n')             
                                    os.system('apt install wifite')        
                                    print('\nOK')
                                elif opcao03 == '0':
                                    catmenu()
                                else:
                                    print('\nOpção inválida\n')
                                    time.sleep(2)

                            while cat == '4':
                                os.system('clear')
                                print('''\033[33m_  _ ____ _    _ ___  _  _ _  _ ___ _  _
|_/  |__| |    | |__] |  | |\ |  |  |  |
| \_ |  | |___ | |__] |__| | \|  |  |__|\033[mv1.0
---------- https://\033[37mnux\033[34mware\033[m.gq ----------

 (1) apache-users    (21) Parsero
 (2) Arachni         (22) plecost
 (3) BBQSQL          (23) Powerfuzzer
 (4) BlindElephant   (24) ProxyStrike
 (5) Burp Suite      (25) Recon-ng
 (6) commix          (26) Skipfish
 (7) CutyCapt        (27) sqlmap
 (8) DAVTest         (28) Sqlninja
 (9) deblaze         (29) sqlsus
(10) DIRB            (30) ua-tester
(11) DirBuster       (31) Uniscan
(12) fimap           (32) Vega
(13) FunkLoad        (33) w3af
(14) Grabber         (34) WebScarab
(15) jboss-autopwn   (35) Webshag
(16) joomscan        (36) WebSlayer
(17) jSQL            (37) WebSploit
(18) Maltego Teeth   (38) Wfuzz
(19) PadBuster       (39) WPScan
(20) Paros           (40) XSSer
					 (41) zaproxy                                

(0) Voltar
                                ''')
                                opcao04 = input('↳ ')
                                if opcao04 == '1':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '2':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '3':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '4':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '5':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '6':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '7':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '8':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '9':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '10':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '11':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '12':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '13':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '14':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '15':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '16':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '17':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '18':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '19':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '20':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '21':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '22':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '23':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '24':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '25':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '26':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '27':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '28':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '29':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '30':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '31':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '32':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '33':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '34':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '35':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '36':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '37':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '38':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '39':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '40':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao04 == '41':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)                      
                                elif opcao04 == '0':
                                    catmenu()
                                else:
                                    print('\nOpção inválida\n')
                                    time.sleep(2)
                            
                            while cat == '5':
                                os.system('clear')
                                print('''\033[33m_  _ ____ _    _ ___  _  _ _  _ ___ _  _
|_/  |__| |    | |__] |  | |\ |  |  |  |
| \_ |  | |___ | |__] |__| | \|  |  |__|\033[mv1.0
---------- https://\033[37mnux\033[34mware\033[m.gq ----------

(1) Burp Suite         (17) rtpmixsound
(2) DNSChef            (18) sctpscan
(3) fiked              (19) SIPArmyKnife
(4) hamster-sidejack   (20) SIPp
(5) HexInject          (21) SIPVicious
(6) iaxflood           (22) SniffJoke
(7) inviteflood        (23) SSLsplit
(8) iSMTP              (24) sslstrip
(9) isr-evilgrade      (25) THC-IPV6
(10) mitmproxy         (26) VoIPHopper
(11) ohrwurm           (27) WebScarab
(12) protos-sip        (28) Wifi Honey
(13) rebind            (29) Wireshark
(14) responder         (30) xspy
(15) rtpbreak          (31) Yersinia
(16) rtpinsertsound    (32) zaproxy                                 
                                
(0) Voltar                   
                                ''')
                                opcao05 = input('↳ ')
                                if opcao05 == '1':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao05 == '2':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao05 == '3':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao05 == '4':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao05 == '5':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao05 == '6':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao05 == '7':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao05 == '8':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao05 == '9':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao05 == '10':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao05 == '11':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao05 == '12':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao05 == '13':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao05 == '14':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao05 == '15':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao05 == '16':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao05 == '17':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao05 == '18':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao05 == '19':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao05 == '20':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao05 == '21':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao05 == '22':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao05 == '23':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao05 == '24':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao05 == '25':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao05 == '26':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao05 == '27':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao05 == '28':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao05 == '29':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao05 == '30':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao05 == '31':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao05 == '32':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)       
                                elif opcao05 == '0':
                                    catmenu()
                                else:
                                    print('\nOpção inválida\n')
                                    time.sleep(2)

                            while cat == '6':
                                os.system('clear')
                                print('''\033[33m_  _ ____ _    _ ___  _  _ _  _ ___ _  _
|_/  |__| |    | |__] |  | |\ |  |  |  |
| \_ |  | |___ | |__] |__| | \|  |  |__|\033[mv1.0
---------- https://\033[37mnux\033[34mware\033[m.gq ----------

(1) CryptCat       (9) polenum
(2) Cymothoa      (10) PowerSploit
(3) dbd           (11) pwnat
(4) dns2tcp       (12) RidEnum
(5) http-tunnel   (13) sbd
(6) HTTPTunnel    (14) U3-Pwn
(7) Intersect     (15) Webshells
(8) Nishang       (16) Weevely

(0) Voltar
                                ''')
                                opcao06 = input('↳ ')
                                if opcao06 == '1':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao06 == '2':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao06 == '3':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao06 == '4':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao06 == '5':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao06 == '6':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao06 == '7':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao06 == '8':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao06 == '9':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao06 == '10':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao06 == '11':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao06 == '12':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao06 == '13':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao06 == '14':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao06 == '15':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao06 == '16':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao06 == '0':
                                    catmenu()
                                else:
                                    print('\nOpção inválida\n')
                                    time.sleep(2)

                            while cat == '7':
                                os.system('clear')
                                print('''\033[33m_  _ ____ _    _ ___  _  _ _  _ ___ _  _
|_/  |__| |    | |__] |  | |\ |  |  |  |
| \_ |  | |___ | |__] |__| | \|  |  |__|\033[mv1.0
---------- https://\033[37mnux\033[34mware\033[m.gq ----------

(1) CaseFile
(2) CutyCapt
(3) dos2unix
(4) Dradis
(5) KeepNote	
(6) MagicTree
(7) Metagoofil
(8) Nipper-ng
(9) pipal                                

(0) Voltar          
                                ''')
                                opcao07 = input('↳ ')
                                if opcao07 == '1':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao07 == '2':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao07 == '3':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao07 == '4':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao07 == '5':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao07 == '6':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao07 == '7':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao07 == '8':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao07 == '9':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao07 == '0':
                                    catmenu()
                                else:
                                    print('\nOpção inválida\n')
                                    time.sleep(2)

                            while cat == '8':
                                os.system('clear')
                                print('''\033[33m_  _ ____ _    _ ___  _  _ _  _ ___ _  _
|_/  |__| |    | |__] |  | |\ |  |  |  |
| \_ |  | |___ | |__] |__| | \|  |  |__|\033[mv1.0
---------- https://\033[37mnux\033[34mware\033[m.gq ----------

(1) Armitage                 (10) jboss-autopwn
(2) Backdoor Factory         (11) Linux Exploit Suggester
(3) BeEF(12) Maltego Teeth   (13) SET
(4) cisco-auditing-tool      (14) ShellNoob
(5) cisco-global-exploiter   (15) sqlmap
(6) cisco-ocs                (16) THC-IPV6
(7) cisco-torch              (17) Yersinia   
(8) commix
(9) crackle

(0) Voltar
                                ''')
                                opcao08 = input('↳ ')
                                if opcao08 == '1':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao08 == '2':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao08 == '3':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao08 == '4':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao08 == '5':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao08 == '6':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao08 == '7':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao08 == '8':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao08 == '9':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao08 == '10':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao08 == '11':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao08 == '12':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao08 == '13':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao08 == '14':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao08 == '15':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao08 == '16':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao08 == '17':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao08 == '0':
                                    catmenu()
                                else:
                                    print('\nOpção inválida\n')
                                    time.sleep(2)

                            while cat == '9':
                                os.system('clear')
                                print('''\033[33m_  _ ____ _    _ ___  _  _ _  _ ___ _  _
|_/  |__| |    | |__] |  | |\ |  |  |  |
| \_ |  | |___ | |__] |__| | \|  |  |__|\033[mv1.0
---------- https://\033[37mnux\033[34mware\033[m.gq ----------

 (1) Binwalk          (11) extundelete
 (2) bulk-extractor   (12) Foremost
 (3) Capstone         (13) Galleta
 (4) chntpw           (14) Guymager
 (5) Cuckoo           (15) iPhone Backup Analyzer
 (6) dc3dd            (16) p0f
 (7) ddrescue         (17) pdf-parser
 (8) DFF              (18) pdfid
 (9) diStorm3         (19) pdgmail
(10) Dumpzilla        (20) peepdf
				   	  (21) RegRipper
					  (22) Volatility
					  (23) Xplico

(0) Voltar
                                ''')
                                opcao09 = input('↳ ')
                                if opcao09 == '1':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao09 == '2':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao09 == '3':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao09 == '4':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao09 == '5':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao09 == '6':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao09 == '7':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao09 == '8':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao09 == '9':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao09 == '10':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao09 == '11':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao09 == '12':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao09 == '13':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao09 == '14':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao09 == '15':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao09 == '16':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao09 == '17':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao09 == '18':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao09 == '19':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao09 == '20':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao09 == '21':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao09 == '22':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao09 == '23':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao09 == '0':
                                    catmenu()
                                else:
                                    print('\nOpção inválida\n')
                                    time.sleep(2)

                            while cat == '10':
                                os.system('clear')
                                print('''\033[33m_  _ ____ _    _ ___  _  _ _  _ ___ _  _
|_/  |__| |    | |__] |  | |\ |  |  |  |
| \_ |  | |___ | |__] |__| | \|  |  |__|\033[mv1.0
---------- https://\033[37mnux\033[34mware\033[m.gq ----------

(1) DHCPig          (8) Reaver
(2) FunkLoad        (9) rtpflood
(3) iaxflood       (10) SlowHTTPTest
(4) Inundator      (11) t50
(5) inviteflood    (12) Termineter
(6) ipv6-toolkit   (13) THC-IPV6
(7) mdk3           (14) THC-SSL-DOS 	

(0) Voltar
                                ''')
                                opcao10 = input('↳ ')
                                if opcao10 == '1':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao10 == '2':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao10 == '3':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao10 == '4':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao10 == '5':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao10 == '6':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao10 == '7':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao10 == '8':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao10 == '9':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao10 == '10':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao10 == '11':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao10 == '12':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao10 == '13':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao10 == '14':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao10 == '0':
                                    catmenu()
                                else:
                                    print('\nOpção inválida\n')
                                    time.sleep(2)

                            while cat == '11':
                                os.system('clear')
                                print('''\033[33m_  _ ____ _    _ ___  _  _ _  _ ___ _  _
|_/  |__| |    | |__] |  | |\ |  |  |  |
| \_ |  | |___ | |__] |__| | \|  |  |__|\033[mv1.0
---------- https://\033[37mnux\033[34mware\033[m.gq ----------

 (1) acccheck              (19) Maskprocessor
 (2) Burp Suite            (20) multiforcer
 (3) CeWL                  (21) Ncrack
 (4) chntpw                (22) oclgausscrack
 (5) cisco-auditing-tool   (23) PACK
 (6) CmosPwd               (24) patator
 (7) creddump              (25) phrasendrescher
 (8) crunch                (26) polenum
 (9) DBPwAudit             (27) RainbowCrack
(10) findmyhash            (28) rcracki-mt
(11) gpp-decrypt           (29) RSMangler
(12) hash-identifier       (30) SQLdict
(13) HexorBase             (31) Statsprocessor
(14) THC-Hydra             (32) THC-pptp-bruter
(15) John the Ripper       (33) TrueCrack
(16) Johnny                (34) WebScarab 
(17) keimpx                (35) wordlists 
(18) Maltego Teeth         (36) zaproxy

(0) Voltar
                                ''')
                                opcao11 = input('↳ ')
                                if opcao11 == '1':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao11 == '2':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao11 == '3':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao11 == '4':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao11 == '5':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao11 == '6':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao11 == '7':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao11 == '8':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao11 == '9':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao11 == '10':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao11 == '11':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao11 == '12':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao11 == '13':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao11 == '14':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao11 == '15':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao11 == '16':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao11 == '17':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao11 == '18':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao11 == '19':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao11 == '20':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao11 == '21':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao11 == '22':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao11 == '23':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao11 == '24':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao11 == '25':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao11 == '26':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao11 == '27':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao11 == '28':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao11 == '29':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao11 == '30':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao11 == '31':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao11 == '32':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao11 == '33':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao11 == '34':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao11 == '35':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao11 == '36':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao11 == '0':
                                    catmenu()
                                else:
                                    print('\nOpção inválida\n')
                                    time.sleep(2)

                            while cat == '12':
                                os.system('clear')
                                print('''\033[33m_  _ ____ _    _ ___  _  _ _  _ ___ _  _
|_/  |__| |    | |__] |  | |\ |  |  |  |
| \_ |  | |___ | |__] |__| | \|  |  |__|\033[mv1.0
---------- https://\033[37mnux\033[34mware\033[m.gq ----------

 (1) apktool
 (2) dex2jar
 (3) diStorm3
 (4) edb-debugger
 (5) jad	
 (6) javasnoop
 (7) JD-GUI
 (8) OllyDbg
 (9) smali
(10) Valgrind
(11) YARA

(0) Voltar                 
                                ''')
                                opcao12 = input('↳ ')
                                if opcao12 == '1':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao12 == '2':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao12 == '3':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao12 == '4':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao12 == '5':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao12 == '6':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao12 == '7':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao12 == '8':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao12 == '9':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao12 == '10':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao12 == '11':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao12 == '0':
                                    catmenu()
                                else:
                                    print('\nOpção inválida\n')
                                    time.sleep(2)

                            while cat == '13':
                                os.system('clear')
                                print('''\033[33m_  _ ____ _    _ ___  _  _ _  _ ___ _  _
|_/  |__| |    | |__] |  | |\ |  |  |  |
| \_ |  | |___ | |__] |__| | \|  |  |__|\033[mv1.0
---------- https://\033[37mnux\033[34mware\033[m.gq ----------

(1) android-sdk
(2) apktool
(3) Arduino
(4) dex2jar
(5) Sakis3G	
(6) smali

(0) Voltar
                                ''')
                                opcao13 = input('↳ ')
                                if opcao13 == '1':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao13 == '2':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao13 == '3':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao13 == '4':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao13 == '5':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao13 == '6':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao13 == '0':
                                    catmenu()
                                else:
                                    print('\nOpção inválida\n')
                                    time.sleep(2)

                            while cat == '14':
                                os.system('clear')
                                print('''\033[33m_  _ ____ _    _ ___  _  _ _  _ ___ _  _
|_/  |__| |    | |__] |  | |\ |  |  |  |
| \_ |  | |___ | |__] |__| | \|  |  |__|\033[mv1.0
---------- https://\033[37mnux\033[34mware\033[m.gq ----------

(1) Wifresti
(2) Squid3

(0) Voltar
                                ''')
                                opcao14 = input('↳ ')
                                if opcao14 == '1':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao14 =='2':
                                    os.system('clear')
                                    print('Indisponível de momento...\n' # - Apagar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ') ----------------- Descomentar e completar nome da ferramenta
                                    # os.system('apt install ') ------------ Descomentar e completar comando
                                    # print('\nOK') ------------------------ Descomentar
                                    time.sleep(3) # ------------------------ Mudar para time.sleep(2)
                                elif opcao14 == '0':
                                    catmenu()
                                else:
                                    print('\nOpção inválida\n')
                                    time.sleep(2)

                                opcao14 = input('↳ ')
                                if opcao14 == '1':
                                    os.system('clear')
                                    print('Instalar Wifresti\n')
                                    os.system('git clone https://github.com/LionSec/wifresti.git '
                                              '&& cp wifresti/wifresti.py /usr/bin/wifresti '
                                              '&& chmod +x /usr/bin/wifresti && wifresti')
                                elif opcao14 == '2':
                                    os.system('clear')
                                    print('Instalar Squid3\n')
                                    os.system('apt install squid3')
                                elif opcao14 == '0':
                                    catmenu()
                                else:
                                    print('\nOpção inválida\n')
                                    time.sleep(2)

                            if cat == '0':
                                menu()
                            else:
                                print('\nOpção inválida\n')
                                time.sleep(2)
                        
                        catmenu()
                    
                    while opcao == '3':
                        os.system('clear')
                        print('''\033[33m_  _ ____ _    _ ___  _  _ _  _ ___ _  _
|_/  |__| |    | |__] |  | |\ |  |  |  |
| \_ |  | |___ | |__] |__| | \|  |  |__|\033[mv1.0
---------- https://\033[37mnux\033[34mware\033[m.gq ----------                          
############################################
#                                          #
# 1 - Adiciona o repositório kali.         #
#                                          #
# 2 - No menu categorias escolhe a         #
#     categoria e a ferramenta que queres  #
#     instalar do repositório kali.        #
#                                          #
# 3 - Remove o repositírio kali.           #
#                                          #
# ##########################################
#                                          #
# \033[31mImportante\033[m - Remover sempre o            #
# repositório kali depois de instalar      #
# todas as ferramentas pretendidas.        #
# Se quiseres ficar com ele activo tens    #
# que ter noção do que são e como          #
# funcionam os repositórios.               #
# Um "dist-upgrade" pode e vai, danificar  #
# o sistema!                               #
#                                          #
############################################
                        ''')
                        input('Prime "enter" para voltar')
                        menu()

                    if opcao == '0':
                        exit()
                    
                    else:
                        print('\nOpção inválida\n')
                        time.sleep(2)
            menu()

    except KeyboardInterrupt:
        print('\nInterrompido...')
        time.sleep(1)
        print('Adeus')
        time.sleep(1)
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)


if __name__ == "__main__":
    inicio()
