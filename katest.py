import os, sys
from traceback import print_exc	# TO OUTPUT A STACK TRACE WHEN AN EXCPTN (ERR) OCCURS IN PYTHON \\
								# Для вывода трассировки стека в случае возникновения исключения (ошибки) в Python.


#COLORS \\ Цвета
def Green(text):
	return "\033[1;32m{}\033[1;m".format(text)
def Blue(text):
	return "\033[1;36m{}\033[1;m".format(text)
def Red(text):
	return "\033[1;31m{}\033[1;m".format(text)


InputText = Green("Process ?> ")


# FUNC FOR OPENING A FILE FOR READING \\ Функция открытия файла для чтения
def OpenFileForRead(file_path):
	with open(file_path, 'r', encoding='utf-8') as file:
		lines = file.readlines()
		return lines


# DISPLAY THE TOOL LIST \\ Вывод списка инструментов
def output_result_bd(lines): # LINES FROM FUNC. OpenFileForRead() \\ Lines из функции OpenFileForRead()
	for line_number, line in enumerate(lines, start=1): # GO THROUGH EACH LINE \\ Проходим по каждой строке
		columns = line.split('|') # SPLIT THE ROW INTO COL BY SPACES \\ Разделяем строку на столбцы по пробелам
		if columns:
			print(f"{line_number}) {columns[0]}") # columns[0] -> LIST COL. WITH INSTRUMENT NAMES \\ columns[0] -> Колонна списка с названиями

# FUNC. FOR PROCESSING USER INPUT \\ Функция для обработки ввода пользователя
def process_input(opcion2, lines):
	if 1 <= int(opcion2) <= len(lines):
		# SPLIT THE ROW INTO COL-S AND OUTPUT THE 2ND COL. \\ Разделяем строку на столбцы и выводим второй столбец
		columns = lines[int(opcion2) - 1].split('|')
		if len(columns) >= 2:
			cmd = os.system(columns[1]) # columns[1] -> LIST COL. WITH TOOLS INSTALLATION \\ columns[1] -> Колонна списка с установкой тулов
		else:
			print(Red("[Error]: No installation method!"))
	else:
		print(Red("[Error]: No installation method!"))


# INSTALLING PACKAGES BY THEME \\ Установка пакетов по темам
def DownloadPacket(lines, thems):
    print ('''
\033[1;36m=+[ {}\033[1;m

0) Install all {} tools'''.format(thems, thems))
    output_result_bd(lines) # TOOL OUTPUT \\ Вывод тулов

    print (Blue("Insert the number of the tool to install it .\n"))

    entry = input(InputText)

    Back(entry)

    if entry == "0": # OR INSTALLING ALL COMPONENTS FROM THE LIST \\ Или установка всех компонентов из списка
        for line_number, line in enumerate(lines, start=1):  # GO THROUGH EACH LINE \\ Проходим по каждой строке
            columns = line.split('|')  # SPLIT THE ROW INTO COL BY SPACES \\ Разделяем строку на столбцы по пробелам
            if columns:
                cmd = os.system(columns[1]) # DOWNLOAD ALL PACKAGES FROM THE LIST \\ Скачиваем все пакеты с категории

    elif 1 <= int(entry) <= len(lines): 	# IF THERE IS SOMETHING UNDER THAT NUMBER IN THE LIST, IT WILL INSTALL ITSELF \\
        process_input(entry, lines) 		# Если в списке есть что-то под этим номером, оно установится

    else:
        print (Red("[Error]: Wrong command!"))


def Back(input_var):
	if input_var.lower() in ["back", "quit", "exit", "gohome"]:
		Start_menu()


# ASCII-ART OUTPUT FUNC. \\ Функция вывода ASCII-арта
def ASCII_art():
    print ('''

 $$\   $$\             $$\                         $$\ $$\           
 $$ | $$  |            $$ |                        $$ |\__|          
 $$ |$$  /  $$$$$$\  $$$$$$\    $$$$$$\   $$$$$$\  $$ |$$\ $$$$$$$\  
 $$$$$  /   \____$$\ \_$$  _|  $$  __$$\ $$  __$$\ $$ |$$ |$$  __$$\ 
 $$  $$<    $$$$$$$ |  \033[1;36mKali linux tools installer\033[1;m |$$ |$$ |$$ |  $$ |
 \033[1;36m$$ |\$$\  $$  __$$ |  $$ |$$\ $$ |  $$ |$$ |  $$ |$$ |$$ |$$ |  $$ |
 $$ | \$$\ \$$$$$$$ |  \$$$$  |\$$$$$$  |\$$$$$$  |$$ |$$ |$$ |  $$ |
 \__|  \__| \_______|   \____/  \______/  \______/ \__|\__|\__|  \__| V2.2 \033[1;m


 \033[1;32m+ -- -- +=[ Author: LionSec | Homepage: www.neodrix.com\033[1;m
 \033[32m+ -- -- +=[ Co-Author: Ego-Dystonia | Homepage: https://github.com/Ego-Dystonia\033[1;m
 \033[1;32m+ -- -- +=[ 331 Tools \033[1;m


\033[1;31m[W] Before updating your system , please remove all Kali-linux repositories to avoid any kind of problem .\033[1;m
''')

# MAIN MENU FUNC., WHICH IND. 5 OUTPUT RESULTS \\ Функция главного меню, включающая 5 результатов вывода
def Start_menu():
	while True:
		print ('''
1) Add Kali repositories & Update 
2) View Categories
3) Install classicmenu indicator
4) Install Kali menu
5) Help
''')
		selection = input(InputText) # INPUT \\ Ввод

		while selection == '1':
			Result1()	# Add Kali repositories & Update

		while selection == '2':
			Result2()	# View Categories

		while selection == '3':
			Result3()	# Install classicmenu indicator

		while selection == '4':
			Result4()	# Install Kali menu

		while selection == '5':
			Result5()	# Help
		

# Start_menu() OUTPUT RESULTS (1-5) \\ Результаты вывода Start_menu() (1-5) ---------------\

# Add Kali repositories & Update
def Result1():
	print ('''
1) Add kali linux repositories
2) Update
3) Remove all kali linux repositories
4) View the contents of sources.list file
''')
	repo = input(InputText)

	Back(repo) # RETURN TO THE MAIN MENU WHEN PREV. SPECIF. INPUT RECVD \\ Возврат в главное меню при наличии ранее указанного ввода

	# Add kali linux repositories
	if repo == '1':
		cmd1 = os.system("apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ED444FF07D8D0BF6")
		cmd2 = os.system("echo '# Kali linux repositories | Added by Katoolin\ndeb http://http.kali.org/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list") # deb тут какой-то
	
	# Update
	elif repo == '2':
		cmd3 = os.system("apt-get update -m")

	# Remove all kali linux repositories
	elif repo == '3':
		infile = "/etc/apt/sources.list"
		outfile = "/etc/apt/sources.list"

		delete_list = ["# Kali linux repositories | Added by Katoolin\n", "deb http://http.kali.org/kali kali-rolling main contrib non-free\n"] # тут тоже
		fin = open(infile)
		os.remove("/etc/apt/sources.list")
		fout = open(outfile, "w+")

		for line in fin:
			for word in delete_list:
				line = line.replace(word, "")
			fout.write(line)

		fin.close()
		fout.close()
		print (Red("\nAll kali linux repositories have been deleted !\n"))

	# View the contents of sources.list file
	elif repo == '4':
		file = open('/etc/apt/sources.list', 'r')
		print (file.read())
		repo = input(Green("To exit, press [Enter]"))
	else:
		print (Red("Sorry, that was an invalid command!"))

# View Categories 
def Result2():
	print ('''
\033[1;36m**************************** All Categories *****************************\033[1;m

1) Informamtion Gathering			8) Exploitation Tools
2) Vulnerability Analysis			9) Forensics Tools
3) Wireless Attacks				10) Stress Testing
4) Web Applications				11) Password Attacks
5) Sniffing & Spoofing				12) Reverse Engineering
6) Maintaining Access				13) Hardware Hacking
7) Reporting Tools 				14) Extra
									
0) All

''')
	
	print (Blue("Select a category or press (0) to install all Kali linux tools .\n"))

	option = input(InputText)

	Back(option)
	
	if option == "0":
		#cmd = os.system("apt-get -f install acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega w3af webscarab websploit wfuzz wpscan xsser zaproxy burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy apktool dex2jar python-distorm3 edb-debugger jad javasnoop jd ollydbg smali valgrind yara android-sdk apktool arduino dex2jar sakis3g smali && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")	
  
		PatchPackages = [
			lambda: OpenFileForRead('Packages/WirelessAttacks.txt'),
			lambda: OpenFileForRead('Packages/ExploitationTools.txt'),
			lambda: OpenFileForRead('Packages/Extra.txt'),
			lambda: OpenFileForRead('Packages/ForensicsTools.txt'),
			lambda: OpenFileForRead('Packages/HardwareHacking.txt'),
			lambda: OpenFileForRead('Packages/InformationGathering.txt'),
			lambda: OpenFileForRead('Packages/MaintainingAccess.txt'),
			lambda: OpenFileForRead('Packages/PasswordAttacks.txt'),
			lambda: OpenFileForRead('Packages/ReportingTools.txt'),
			lambda: OpenFileForRead('Packages/ReverseEngineering.txt'),
			lambda: OpenFileForRead('Packages/SniffingSpoofing.txt'),
			lambda: OpenFileForRead('Packages/StressTesting.txt'),
			lambda: OpenFileForRead('Packages/VulnerabilityAnalysis.txt'),
			lambda: OpenFileForRead('Packages/WebApplications.txt')
		]
		vatient = input(Green("Do you want to Install or Review? [i/R]> "))
		x = 0
		while x <= len(PatchPackages):  # CHECK THAT THE INPUT IS VALID \\ Проверяем, что ввод является допустимым
			for line_number, line in enumerate(PatchPackages[int(x)-1](), start=1):  # GO THROUGH EACH LINE \\ Проходим по каждой строке
				columns = line.split('|')  # SPLIT THE ROW INTO COL BY SPACES \\ Разделяем строку на столбцы по пробелам
				if columns:
					if vatient.lower() == 'i':
						cmd = os.system(columns[1].strip())
					else:
						cmd = os.system(f"echo '{columns[1].strip()}'")
			x+=1
 
 
	def InformationGathering():
		lines_InformationGathering = OpenFileForRead('Packages/InformationGathering.txt')
		DownloadPacket(lines_InformationGathering, "Information Gathering")

	def VulnerabilityAnalysis():
		lines_VulnerabilityAnalysis = OpenFileForRead('Packages/VulnerabilityAnalysis.txt')
		DownloadPacket(lines_VulnerabilityAnalysis, "Vulnerability Analysis")

	def WirelessAttacks():
		lines_WirelessAttacks = OpenFileForRead('Packages/WirelessAttacks.txt')
		DownloadPacket(lines_WirelessAttacks, "Wireless Attacks")

	def WebApplications():
		lines_WebApplications = OpenFileForRead('Packages/WebApplications.txt')
		DownloadPacket(lines_WebApplications, "Web Applications")

	def SniffingSpoofing():
		lines_SniffingSpoofing = OpenFileForRead('Packages/SniffingSpoofing.txt')
		DownloadPacket(lines_SniffingSpoofing, "Sniffing && Spoofing")

	def MaintainingAccess():
		lines_MaintainingAccess = OpenFileForRead('Packages/MaintainingAccess.txt')
		DownloadPacket(lines_MaintainingAccess, "Maintaining Access")

	def ReportingTools():
		lines_ReportingTools = OpenFileForRead('Packages/ReportingTools.txt')
		all_commands = "apt-get install -y casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal"
		DownloadPacket(lines_ReportingTools, "Reporting Tools")

	def ExploitationTools():
		lines_ExploitationTools = OpenFileForRead('Packages/ExploitationTools.txt')
		DownloadPacket(lines_ExploitationTools, "Exploitation Tools")

	def ForensicsTools():
		lines_ForensicsTools = OpenFileForRead('Packages/ForensicsTools.txt')
		DownloadPacket(lines_ForensicsTools, "Forensics Tools")

	def StressTesting():
		lines_StressTesting = OpenFileForRead('Packages/StressTesting.txt')
		DownloadPacket(lines_StressTesting, "Stress Testing")

	def PasswordAttacks():
		lines_PasswordAttacks = OpenFileForRead('Packages/PasswordAttacks.txt')
		DownloadPacket(lines_PasswordAttacks, "Password Attacks")

	def ReverseEngineering():
		lines_ReverseEngineering = OpenFileForRead('Packages/ReverseEngineering.txt')
		DownloadPacket(lines_ReverseEngineering, "Reverse Engineering")

	def HardwareHacking():
		lines_HardwareHacking = OpenFileForRead('Packages/HardwareHacking.txt')
		DownloadPacket(lines_HardwareHacking, "Hardware Hacking")

	def Extra():
		lines_Extra = OpenFileForRead('Packages/Extra.txt')
		DownloadPacket(lines_Extra, "Extra")

# ANONYMOUS LIST OF FUNC. \\ Анонимный список функций
	categories = [
		lambda: InformationGathering(),
		lambda: VulnerabilityAnalysis(),
		lambda: WirelessAttacks(),
		lambda: WebApplications(),
		lambda: SniffingSpoofing(),
		lambda: MaintainingAccess(),
		lambda: ReportingTools(),
		lambda: ExploitationTools(),
		lambda: ForensicsTools(),
		lambda: StressTesting(),
		lambda: PasswordAttacks(),
		lambda: ReverseEngineering(),
		lambda: HardwareHacking(),
		lambda: Extra()
	]

	Back(option)

	if option.isdigit(): # Проверка, если ввод состоит только из чисел
		while 1 <= int(option) <= len(categories):  # CHECK THAT THE INPUT IS VALID \\ Проверяем, что ввод является допустимым
			categories[int(option)-1]()  # CALL A FUNC. FROM THE LIST \\ Вызываем функцию из списка
		while int(option) > len(categories):
			print(Red("[Error]: Invalid number!"))
			Result2()
	

# Install classicmenu indicator
def Result3():
	print (''' 
ClassicMenu Indicator is a notification area applet (application indicator) for the top panel of Ubuntu's Unity desktop environment.

It provides a simple way to get a classic GNOME-style application menu for those who prefer this over the Unity dash menu.

Like the classic GNOME menu, it includes Wine games and applications if you have those installed.

For more information , please visit : http://www.florian-diesch.de/software/classicmenu-indicator/

''')
	repo = input(Green("Do you want to install classicmenu indicator ? [y/N]>"))
	if repo == "y":
		cmd1 = os.system("add-apt-repository ppa:diesch/testing && apt-get update")
		cmd = os.system("sudo apt-get install classicmenu-indicator")
	else:
		Start_menu()

# Install Kali menu
def Result4():
	repo = input(Green("Do you want to install Kali menu ? [y/N]>"))
	if repo == "y":
		cmd1 = os.system("apt-get install kali-menu")
	else:
		Start_menu()

# Help
def Result5():
	print (''' 
****************** +Commands+ ******************
{} \033[1;33m-- Go to the main menu\033[1;m
''').format(Green("back \ quit \ exit \ gohome"), )
	Start_menu()

# END OF Start_menu() OUTPUT RESULTS \\  Конец результатов вывода Start_menu() (1-5) ------/


# CHECKING FOR SUDO PRIVILEGES \\ Проверка наличия привилегий sudo
if os.getuid() != 0:
	print ("Sorry. This script requires sudo privledges")
	sys.exit()


# THE SCRIPT ITSELF \\ Сам скрипт
def main():
	try:
		ASCII_art()
		
		Start_menu()

    # ERROR HANDLING \\ Обработка ошибок
	except KeyboardInterrupt:
		print (": Shutdown requested...Goodbye...")
	except Exception:
		print_exc(file=sys.stdout)
	sys.exit(0)
	


# CHECKING FOR DIRECK SCRIPT LAUNCH \\ Проверка прямого запуска сценария
if __name__ == "__main__":
    main()
