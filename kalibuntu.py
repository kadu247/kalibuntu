#!/usr/bin/python3

import os
import sys
import traceback
import time


def inicio():
    try:
        if not os.geteuid() == 0:
            os.system('clear')
            print('''
_  _ ____ _    _ ___  _  _ _  _ ___ _  _
|_/  |__| |    | |__] |  | |\ |  |  |  |
| \_ |  | |___ | |__] |__| | \|  |  |__|v1.0
---------- https://nuxware.gq ----------
             
      Tens que ter privilégio root
       
        → ex: sudo ./kalibuntu ←
            ''')

        else:

            def menu():
                while True:
                    os.system('clear')
                    print('''
_  _ ____ _    _ ___  _  _ _  _ ___ _  _
|_/  |__| |    | |__] |  | |\ |  |  |  |
| \_ |  | |___ | |__] |__| | \|  |  |__|v1.0
---------- https://nuxware.gq ----------                    
                    
(1) Adicionar/Remover repositório do kali linux 
(2) Ver categorias
(3) Instruções
(0) Saír
                    ''')
                    opcao = input('↳ ')
                    while opcao == '1':
                        os.system('clear')
                        print('''
_  _ ____ _    _ ___  _  _ _  _ ___ _  _
|_/  |__| |    | |__] |  | |\ |  |  |  |
| \_ |  | |___ | |__] |__| | \|  |  |__|v1.0
---------- https://nuxware.gq ----------                    
                    
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
                            print('''
_  _ ____ _    _ ___  _  _ _  _ ___ _  _
|_/  |__| |    | |__] |  | |\ |  |  |  |
| \_ |  | |___ | |__] |__| | \|  |  |__|v1.0
---------- https://nuxware.gq ----------

(1) Information Gathering     (8) Exploitation Tools
(2) Vulnerability Analysis    (9) Forensics Tools
(3) Wireless Attacks         (10) Stress Testing
(4) Web Applications         (11) Password Attacks
(5) Sniffing & Spoofing      (12) Reverse Engineering
(6) Maintaining Access       (13) Hardware Hacking
(7) Reporting Tools          (14) Extra

(0) Voltar
                        ''')
                            cat = input('↳ ')
                            while cat == '1':
                                os.system('clear')
                                print('''
_  _ ____ _    _ ___  _  _ _  _ ___ _  _
|_/  |__| |    | |__] |  | |\ |  |  |  |
| \_ |  | |___ | |__] |__| | \|  |  |__|v1.0
---------- https://nuxware.gq ----------

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
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '2':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '3':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '4':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '5':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '6':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '7':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '8':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '9':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '10':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '11':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '12':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '13':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '14':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '15':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '16':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '17':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '18':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '19':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '20':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '21':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '22':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '23':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '24':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '25':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '26':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '27':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '28':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '29':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '30':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '31':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '32':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '33':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '34':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '35':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '36':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '37':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '38':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '39':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '40':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '41':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '42':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '43':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '44':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '45':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '46':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '47':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '48':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '49':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '50':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '51':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '52':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '53':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '54':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '55':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '56':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '57':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao01 == '0':
                                    catmenu()
                                else:
                                    print('\nOpção inválida\n')
                                    time.sleep(2)
                            
                            while cat == '2':
                                os.system('clear')
                                print('''
_  _ ____ _    _ ___  _  _ _  _ ___ _  _
|_/  |__| |    | |__] |  | |\ |  |  |  |
| \_ |  | |___ | |__] |__| | \|  |  |__|v1.0
---------- https://nuxware.gq ----------

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
                                elif opcao02 == '0':
                                    catmenu()
                                else:
                                    print('\nOpção inválida\n')
                                    time.sleep(2)
                            while cat == '3':
                                os.system('clear')
                                print('''
_  _ ____ _    _ ___  _  _ _  _ ___ _  _
|_/  |__| |    | |__] |  | |\ |  |  |  |
| \_ |  | |___ | |__] |__| | \|  |  |__|v1.0
---------- https://nuxware.gq ----------

 (1) Aircrack-ng         (17) kalibrate-rtl
 (2) Asleap              (18) KillerBee
 (3) Bluelog             (19) Kismet
 (4) BlueMaho            (20) mdk3
 (5) Bluepot             (21) mfcuk
 (6) BlueRanger          (22) mfoc
 (7) Bluesnarfer         (23) mfterm
 (8) Bully               (24) Multimon-NG
 (9) coWPAtty            (25) PixieWPS
(10) crackle             (26) Reaver
(11) eapmd5pass          (27) redfang
(12) Fern Wifi Cracker   (28) RTLSDR Scanner
(13) Ghost Phisher       (29) Spooftooph
(14) GISKismet           (30) Wifi Honey
(16) gr-scan             (31) Wifitap 
                         (32) Wifite 
				
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
                                    print('A instalar BlueMaho\n')             
                                    os.system('apt install git && git clone git://git.kali.org/packages/bluemaho.git')        
                                    print('\nOK')                   
                                    time.sleep(2)
                                elif opcao03 == '5':
                                    os.system('clear')
                                    print('A instalar \n')             
                                    os.system('apt install ')        
                                    print('\nOK')                   
                                    time.sleep(2)
                                elif opcao03 == '0':
                                    catmenu()
                                else:
                                    print('\nOpção inválida\n')
                                    time.sleep(2)

                            while cat == '4':
                                os.system('clear')
                                print('''
_  _ ____ _    _ ___  _  _ _  _ ___ _  _
|_/  |__| |    | |__] |  | |\ |  |  |  |
| \_ |  | |___ | |__] |__| | \|  |  |__|v1.0
---------- https://nuxware.gq ----------

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
                                elif opcao04 == '0':
                                    catmenu()
                                else:
                                    print('\nOpção inválida\n')
                                    time.sleep(2)
                            
                            while cat == '5':
                                os.system('clear')
                                print('''
_  _ ____ _    _ ___  _  _ _  _ ___ _  _
|_/  |__| |    | |__] |  | |\ |  |  |  |
| \_ |  | |___ | |__] |__| | \|  |  |__|v1.0
---------- https://nuxware.gq ----------

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
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao05 == '0':
                                    catmenu()
                                else:
                                    print('\nOpção inválida\n')
                                    time.sleep(2)

                            while cat == '6':
                                os.system('clear')
                                print('''
_  _ ____ _    _ ___  _  _ _  _ ___ _  _
|_/  |__| |    | |__] |  | |\ |  |  |  |
| \_ |  | |___ | |__] |__| | \|  |  |__|v1.0
---------- https://nuxware.gq ----------

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
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao06 == '0':
                                    catmenu()
                                else:
                                    print('\nOpção inválida\n')
                                    time.sleep(2)

                            while cat == '7':
                                os.system('clear')
                                print('''
_  _ ____ _    _ ___  _  _ _  _ ___ _  _
|_/  |__| |    | |__] |  | |\ |  |  |  |
| \_ |  | |___ | |__] |__| | \|  |  |__|v1.0
---------- https://nuxware.gq ----------

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
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao07 == '0':
                                    catmenu()
                                else:
                                    print('\nOpção inválida\n')
                                    time.sleep(2)

                            while cat == '8':
                                os.system('clear')
                                print('''
_  _ ____ _    _ ___  _  _ _  _ ___ _  _
|_/  |__| |    | |__] |  | |\ |  |  |  |
| \_ |  | |___ | |__] |__| | \|  |  |__|v1.0
---------- https://nuxware.gq ----------

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
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao08 == '0':
                                    catmenu()
                                else:
                                    print('\nOpção inválida\n')
                                    time.sleep(2)

                            while cat == '9':
                                os.system('clear')
                                print('''
_  _ ____ _    _ ___  _  _ _  _ ___ _  _
|_/  |__| |    | |__] |  | |\ |  |  |  |
| \_ |  | |___ | |__] |__| | \|  |  |__|v1.0
---------- https://nuxware.gq ----------

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
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao09 == '0':
                                    catmenu()
                                else:
                                    print('\nOpção inválida\n')
                                    time.sleep(2)

                            while cat == '10':
                                os.system('clear')
                                print('''
_  _ ____ _    _ ___  _  _ _  _ ___ _  _
|_/  |__| |    | |__] |  | |\ |  |  |  |
| \_ |  | |___ | |__] |__| | \|  |  |__|v1.0
---------- https://nuxware.gq ----------

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
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao10 == '0':
                                    catmenu()
                                else:
                                    print('\nOpção inválida\n')
                                    time.sleep(2)

                            while cat == '11':
                                os.system('clear')
                                print('''
_  _ ____ _    _ ___  _  _ _  _ ___ _  _
|_/  |__| |    | |__] |  | |\ |  |  |  |
| \_ |  | |___ | |__] |__| | \|  |  |__|v1.0
---------- https://nuxware.gq ----------

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
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao11 == '0':
                                    catmenu()
                                else:
                                    print('\nOpção inválida\n')
                                    time.sleep(2)

                            while cat == '12':
                                os.system('clear')
                                print('''
_  _ ____ _    _ ___  _  _ _  _ ___ _  _
|_/  |__| |    | |__] |  | |\ |  |  |  |
| \_ |  | |___ | |__] |__| | \|  |  |__|v1.0
---------- https://nuxware.gq ----------

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
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao12 == '0':
                                    catmenu()
                                else:
                                    print('\nOpção inválida\n')
                                    time.sleep(2)

                            while cat == '13':
                                os.system('clear')
                                print('''
_  _ ____ _    _ ___  _  _ _  _ ___ _  _
|_/  |__| |    | |__] |  | |\ |  |  |  |
| \_ |  | |___ | |__] |__| | \|  |  |__|v1.0
---------- https://nuxware.gq ----------

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
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
                                elif opcao13 == '0':
                                    catmenu()
                                else:
                                    print('\nOpção inválida\n')
                                    time.sleep(2)

                            while cat == '14':
                                os.system('clear')
                                print('''
_  _ ____ _    _ ___  _  _ _  _ ___ _  _
|_/  |__| |    | |__] |  | |\ |  |  |  |
| \_ |  | |___ | |__] |__| | \|  |  |__|v1.0
---------- https://nuxware.gq ----------

(1) Wifresti
(2) Squid3

(0) Voltar
                                ''')
                                opcao14 = input('↳ ')
                                if opcao14 == '1':
                                    os.system('clear')
                                    print('Indisponível de momento...\n'  # Descomentar esta linha quando comando disponivel
                                          'Script em actualização!')
                                    # print('A instalar ...')             # Nome da ferramenta
                                    # os.system('apt install ...')        # Comando para instalar
                                    # print('OK')                         # Confirmação
                                    time.sleep(3)
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
                        print('''
_  _ ____ _    _ ___  _  _ _  _ ___ _  _
|_/  |__| |    | |__] |  | |\ |  |  |  |
| \_ |  | |___ | |__] |__| | \|  |  |__|v1.0
---------- https://nuxware.gq ----------                          
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
# Importante - Remover sempre o            #
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
