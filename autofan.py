import os
try:
	from websocket import create_connection
except:
	os.system('pip install websocket-client')
import json
import datetime
from datetime import datetime
import time
try:
	import requests
except:
	os.system('pip install requests')
import websocket
import traceback
import _thread as thread
try:
	from fake_useragent import UserAgent
except:
	os.system('pip install fake-useragent')
import re
import threading
import random
import uuid
import platform
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

counter = 0
penghitung=0

def tele(bot_message):
    
    bot_token = '1160430048:AAHWoxOJxQ8amBHh0b3CsRTz8NeXphWVf70'
    bot_chatID = '-483298315'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)
   
 
def activation(bot_message):
    
    bot_token = '1160430048:AAHWoxOJxQ8amBHh0b3CsRTz8NeXphWVf70'
    bot_chatID = '-426516657'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

def unfantozero():
	print("[ INFO ]")
	print(" - digunakan untuk menghapus semua list block \n - login akun terlebih dahulu via no telp dan password \n - akan otomatis meng unblock semua dari daftar block")
	
	
	print("____________________________________________________________")
	
	response5 = requests.get('https://id-api.spooncast.net/users/'+userid+'/followings/',headers=headers2)
	nexts=(response5.json()['next'])
	idd2=[]
	z=0
	for i in range(0,len(response5.json()['results'])):
		idd2.append(str(response5.json()['results'][int(i)]['id']))
		thread.start_new_thread(unfolcepet, (str(response5.json()['results'][int(i)]['id']),))
		
	while nexts!="":
		print("========================")
		response6 = requests.get(nexts,headers=headers2)
		link1=(response6.json()['next'])
		print(link1)
		nexts=link1
		for i in range(0,len(response6.json()['results'])):
			idd2.append(str(response6.json()['results'][int(i)]['id']))
			unfolcepet(str(response6.json()['results'][int(i)]['id']))
			z+=1
			print(z)
	print("debug")
	print(len(idd2))
	print(idd2)

def getlistfans():
	print("____________________________________________________________")
	os.remove('listid.txt')
	os.system('touch listid.txt')
	filefans=open('listid.txt','r+')
	response5 = requests.get('https://id-api.spooncast.net/users/'+userid+'/followers/',headers=headers2)
	nexts=(response5.json()['next'])
	idd2=[]
	z=0
	for i in range(0,len(response5.json()['results'])):
		idd2.append(str(response5.json()['results'][int(i)]['id']))
		filefans.write(str(response5.json()['results'][int(i)]['id'])+'\n')
		
	while nexts!="":
		print("========================")
		response6 = requests.get(nexts,headers=headers2)
		link1=(response6.json()['next'])
		print(link1)
		nexts=link1
		for i in range(0,len(response6.json()['results'])):
			idd2.append(str(response6.json()['results'][int(i)]['id']))
			filefans.write(str(response5.json()['results'][int(i)]['id'])+'\n')
			#thread.start_new_thread(unfolcepet, (str(response6.json()['results'][int(i)]['id']),))
			z+=1
			print(z)
	print("debug")
	print(len(idd2))
	print(idd2)
	filefans.close()
	
	
def unfanback():
	print("____________________________________________________________")
	
	response5 = requests.get('https://id-api.spooncast.net/users/'+userid+'/followings/',headers=headers2)
	nexts=(response5.json()['next'])
	idd2=[]
	z=0
	
	for i in range(0,len(response5.json()['results'])):
		uid=str(response5.json()['results'][int(i)]['id'])
		responsel = requests.get('https://id-api.spooncast.net/users/'+uid+'/',headers=headers2)
		kode = responsel.json()['results'][0]['follow_status']
		if kode==1:
			thread.start_new_thread(unfolcepet, (str(response5.json()['results'][int(i)]['id']),))
			print('ada woy')
		else:
			print('gaada')
	
	#time.sleep(100)
	while nexts!="":
		print("========================")
		response6 = requests.get(nexts,headers=headers2)
		link1=(response6.json()['next'])
		print(link1)
		nexts=link1
		for i in range(0,len(response6.json()['results'])):
			uid=str(response6.json()['results'][int(i)]['id'])
			responsel = requests.get('https://id-api.spooncast.net/users/'+uid+'/',headers=headers2)
			kode = responsel.json()['results'][0]['follow_status']
			
			
			if kode==1:
				unfolcepet(str(response6.json()['results'][int(i)]['id']))
				z+=1
				print(z)
				print('ada dongs')
			else:
				print('nooooooooo gaada')
				
	print("debug")
	


def delfbcepet():
	print("____________________________________________________________")
	
	response5 = requests.get('https://id-api.spooncast.net/users/'+userid+'/fanmessages/',headers=headers2)
	nexts=(response5.json()['next'])
	idd2=[]
	z=0
	
	for i in range(0,len(response5.json()['results'])):
		uid=str(response5.json()['results'][int(i)]['id'])
		if True:
			thread.start_new_thread(delfb, (str(response5.json()['results'][int(i)]['id']),))
			print('ada woy')
		else:
			print('gaada')
	
	#time.sleep(100)
	while nexts!="":
		print("========================")
		response6 = requests.get(nexts,headers=headers2)
		link1=(response6.json()['next'])
		print(link1)
		nexts=link1
		for i in range(0,len(response6.json()['results'])):
			uid=str(response6.json()['results'][int(i)]['id'])
			if True:
				thread.start_new_thread(delfb, (str(response6.json()['results'][int(i)]['id']),))
				z+=1
				print(z)
				print('ada dongs')
			else:
				print('nooooooooo gaada')
				
	print("dah selesai")
	


def fancepet():
	try:
		if True:
			listid=open('listfans.johnson','r+').read().split('\n')
			z=0
			processes=[]
			with ThreadPoolExecutor(max_workers=10) as executor:
				for uid in listid:
					#thread.start_new_thread(folcepet, (uid,))
					processes.append(executor.submit(folcepet, uid))
					z+=1
					print(z)
					time.sleep(1)
				
	except Exception as e:
		print('ini error bawah definisi')
		print(traceback.format_exc())
		print(e)
		




def folcepet(idkickers):
	response = requests.post('https://id-api.spooncast.net/users/'+idkickers+'/follow/',headers=headers2,)
	
	try:
		statuskode = int(response.json()['status_code'])
				
	except:
		print(traceback.format_exc())
		print(response.json())
	if statuskode == 429:
				print('istirahat 10 detik')
				
				
				
				for x in range(10):
					cy = 10 - x
					print('lanjut setelah '+str(cy)+' detik')
					time.sleep(1)
	
	print(response.json())
	print(idkickers+" berhasil follow")
	fanb={"contents":random.choice(listfb)}
	fanboard=requests.post('https://id-api.spooncast.net/users/'+idkickers+'/fanmessages/',headers=headers2,json=fanb)
	#print(fanboard.json())

def unfolcepet(idkickers):
	response = requests.post('https://id-api.spooncast.net/users/'+idkickers+'/unfollow/',headers=headers2,)
	
	try:
				statuskode = int(response.json()['status_code'])
				
	except:
				print(traceback.format_exc())
				print(response.json())
			
	if statuskode == 429:
				print('istirahat 10 detik')
				
				
				
				for x in range(10):
					cy = 10 - x
					print('lanjut setelah '+str(cy)+' detik')
					time.sleep(1)
	
	print(response.json())
	print(idkickers+" berhasil diunfollow")
	
def delfb(idkickers):
	response = requests.delete('https://id-api.spooncast.net/fancomments/'+idkickers+'/',headers=headers2,)
	print(response.json())
	print(idkickers+" berhasil dihapus")
	
	
	
	


def refresher():
	global counter
	global usertoken
	#pesan='{"event":"live_health","type":"live_rpt","live_id":'+slink+',"user_id":'+userid+',"useragent":"Web","appversion":"5.4.9"}'
	pesan='{"event":"live_health","type":"live_rpt","live_id":'+slink+',"user_id":'+userid+',"useragent":"Web","appversion":"5.4.9"}'
	pesan='{"event":"live_health","type":"live_rpt","live_id":'+slink+',"user_id":'+idnyadj+',"useragent":"Web","appversion":"5.4.9"}'
	print("ini counrr "+str(counter))
	if counter >= 0:
		ws.send(pesan)
	counter+=1
	threading.Timer(10, refresher).start()
	

def autochat():
	global counter
	global usertoken
	olahankata="Jangan lupa fan to fan ya"
	
	if counter >= 2:
		ws.send('{"appversion":"5.4.9","event":"live_message","token":"29b0534f029ff4614cffbd466a5c1b2327f65f72","useragent":"Web","message":"'+olahankata+'","type":"live_rpt"}')
	counter+=1
	threading.Timer(180, autochat).start()
	
	
def infoer():
	z=open('listid.txt','r+').read().split('\n')
	print('______________________\n\n')
	
	print('Total keseluruhan yang telah difan '+str(len(z))+' akun')
	
	print('\n\n_______________________')
	
	
	threading.Timer(120, infoer).start()
	




def getslink(txtid):
	regex = re.compile(r'^(?:http|ftp)s?://', re.IGNORECASE)
	
	
	if re.match(regex, txtid) == None:
		txtid='https://'+txtid
	response = requests.get(txtid)
	url = response.url
	return url[34:-59]
	
	
def getlives(slink):
	response = requests.get('https://id-api.spooncast.net/lives/'+slink,headers=headers2).json()
	return response
	
#pastikan formatnya sama
#kalau beda pasti error
listfb=[
'ini kata-kata baru , tes',
'fanback kak , jangan pelit :p',
'fanback ya kak',
'fanback kak , kakak cakep deh',
'tadi keknya ketemu di room siapa ya lupa, fanback ya',
'aku lagi ultah kak , fanback ya . pengen punya banyak fans'
]

def on_message(ws, message):
	global penghitung
	chat = json.loads(message)
	#print(chat)
	
	try:
		evn=chat['event']
		if evn == "live_join" or evn == "live_shadowjoin" or evn == "live_like" or evn == "user_access":
			print(evn)
			appender=open('listid.txt','a+')
			listid=open('listid.txt','r+').read().split('\n')
			uid = str(chat['data']['author']['id'])
			if uid not in listid:
				following=requests.post('https://id-api.spooncast.net/users/'+uid+'/follow/',headers=headers2)
				fanb={"contents":random.choice(listfb)}
				fanboard=requests.post('https://id-api.spooncast.net/users/'+uid+'/fanmessages/',headers=headers2,json=fanb)
				appender.write(uid+'\n')
				penghitung+=1
				print(str(penghitung)+' berhasil ke id '+uid)
			else:
				print('skip '+uid)
				

	except Exception as e:
		print('ini error bawah definisi')
		print(traceback.format_exc())
		print(e)
	
	
	

def on_error(ws, error):
	print(error)

def on_close(ws):
	print("### closed ###")
	

def on_open(ws):
	def run(*args):
		global usertoken
		#print(usertoken)
		#time.sleep(5)
		#pesan0 = '{"live_id":'+slink+',"token":"'+usertoken+'","event":"live_state","appversion":"5.4.9","useragent":"Web","type":"live_req","user_id":'+userid+'}'
		#ws.send(pesan0)
		#pesan0 = '{"live_id":'+slink+',"event":"live_state","appversion":"5.4.9","useragent":"Web","type":"live_req","user_id":'+userid+'}'
		pesan0 = '{"live_id":'+slink+',"event":"live_state","appversion":"5.4.9","useragent":"Web","type":"live_req","user_id":'+userid+'}'
		
		if True:
			ws.send(pesan0)

		
		pesan = '{"live_id":'+slink+',"token":"'+usertoken+'","event":"live_join","appversion":"5.4.9","useragent":"Web","type":"live_req","retry":0,"reconnect":false}'
		ws.send(pesan) 
		
		refresher()
		#autochat()
		infoer()
		print(slink)
		print(userid)
		#print(usertoken)
		print("====")
	
	thread.start_new_thread(run, ())


nurut = False
usertoken = ''
if __name__ == "__main__":

	

	e="ini error"
	namaconfig='config.johnson'
	totid=[]
	try:
		k2=open('listid.txt','r+').read().split('\n')
	except:
		os.system('touch listid.txt')
		k2=open('listid.txt','r+').read().split('\n')
	
	
	with open(namaconfig, "r") as jsonFile:
		config = json.load(jsonFile)
	
	
	
	headers = {"User-Agent":"Mozilla/5.0",'origin':'https://www.spooncast.net','referer':'https://www.spooncast.net/','content-type':'application/json'}
	headers2={'User-Agent':'Mozilla/5.0','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3','origin':'https://www.spooncast.net','referer':'https://www.spooncast.net/','content-type':'application/json'}
	params1 = {'cv':'heimdallr'}
	params2 = {'cv':'heimdallr2'}

	print('autofan')
	
	print('total blacklist karena '+str(len(k2)))

	if True:
		if config['nomor']=='':
			print("Contoh seperti ini : 6285155415154")
			print("depannya harus 62")
			config['nomor'] = input('masukkan nomor telepon akun anda : ')
			config['password'] = input('masukkan password : ')
			with open(namaconfig, "w") as jsonFile:
				json.dump(config, jsonFile)
				
			os.system("python autofan.py")
		
		c = open('listid.txt','r+')
			
		nomer = config['nomor']
		password = config['password']
	
		
		print("nomor sekarang "+nomer)
		print("password sekarang "+password)
		print("otw login ...")
		if True:
			if True:
				ua = UserAgent()
				uafix = ua.random
				headers = {"User-Agent":uafix,'origin':'https://www.spooncast.net','referer':'https://www.spooncast.net/','content-type':'application/json'}
				tokens = requests.post('https://id-auth.spooncast.net/tokens',headers=headers,json={"device_unique_id":uafix,"auth_data":{"act_type":"phone","password":password,"msisdn":nomer}})
				
				try:
					jwt = tokens.json()['data']['jwt']
					rtoken = tokens.json()['data']['refresh_token']
					headers2 = {"Authorization":"Bearer "+jwt,"User-Agent":uafix,'origin':'https://www.spooncast.net','referer':'https://www.spooncast.net/','accept':'application/json','host':'id-api.spooncast.net','save-data':'on','sec-fetch-site':'same-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','accept-encoding':'gzip, deflate, br','accept-language':'en-US,en;q=0.9,ru;q=0.8','access-control-request-method':'GET','access-control-request-headers':'authorization'}
					headersopt = {"User-Agent":uafix,'origin':'https://www.spooncast.net','referer':'https://www.spooncast.net/','accept':'*/*','host':'id-api.spooncast.net','sec-fetch-site':'same-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','accept-encoding':'gzip, deflate, br','accept-language':'en-US,en;q=0.9,ru;q=0.8'}
					login = requests.post('https://id-api.spooncast.net/signin/?version=2',headers=headers2,json={"device_unique_id":uafix,"auth_data":{"act_type":"phone","password":password,"msisdn":nomer}}).json()
					#print(login)
					userid = str(login['results'][0]['id'])
					usertoken = 'Bearer '+jwt
					print('berhasil login')
					
					
				except:
					
					
					
					print(traceback.format_exc())
					print('_________________________________________________')
					print('AKUN GAGAL')
					print('SILAHKAN PILIH MENU NOMOR 3 UNTUK GANTI AKUN')
					print('_________________________________________________')
			print("""
MENU
0. \tGanti id
1. \tUnfollow semua following sampai 0  (mode cepat)
2. \tParkun di room rame + autofollowing + fanboard + autochat ngemis fan
3. \tGanti akun
4. \treset blacklist (fungsi blacklist adalah agar tidak spam ke fanboard orang lebih dari 1x)
5. \thapus bersih fanboard (mode cepat)
6. \tunfan semua yang gak fan back (mode cepat)



SCRIPT GW GA ABAL2
GAK DIPASANGIN PHISING
(KALAU DAPATNYA DARI NOMOR DIBAWAH INI)
CP : 085155415154
	""")
		
		pil = int(input("masukkan pilihan anda : "))
		infoer()
		if pil == 1:
			unfantozero()
			
		elif pil==0:
			txtid = input("masukkan id baru : @")
			params={'username':txtid}
			data = {'username':txtid}
			data_json = json.dumps(data)
			payload = {"json_payload",data_json}
			response = requests.post('https://id-api.spooncast.net/users/username/',headers=headers2,json={"username":txtid})
			print(response.json())
			if response.json()['status_code']==400:
				print("id tersebut telah dipakai orang lain atau dilarang oleh mimin")
			elif response.json()['status_code']==200:
				print("id telah terganti :') silahkan cek")
			
			os.system('python autofan.py')
			
		elif pil == 2:
			print('tips : masukkin ke room rame')
			print('sharelink room rame dibawah ini')
			print('contoh link https://spoon.click/id_live_7826870')
			txtid = input("masukkan link : ")
			slink = getslink(txtid)
			lives = getlives(slink)
			
			headers={'User-Agent':'Mozilla/5.0','Authorization':'Token '+usertoken,'origin':'https://www.spooncast.net','referer':'https://www.spooncast.net/','content-type':'application/json'}
			reqacc = requests.get('https://id-api.spooncast.net/lives/'+str(slink)+'/access/',headers=headers2)
			idnyadj = str(reqacc.json()['results'][0]['author']['id'])
			
			
			reqtemp = requests.get('https://id-api.spooncast.net/items/template/',headers=headers2)
			print(reqtemp.json())
			
		
			websocket.enableTrace(True)
			ws = websocket.WebSocketApp("wss://id-heimdallr.spooncast.net/"+slink,on_message = on_message,on_error = on_error,on_close = on_close,header={'User-Agent':'Mozilla/5.0'})
			ws.on_open = on_open
			ws.run_forever()
		elif pil==3:
			
			if True:
				print("Contoh seperti ini : 6285155415154")
				print("depannya harus 62")
				config['nomor'] = input('masukkan nomor telepon akun anda : ')
				config['password'] = input('masukkan password akun anda : ')
				with open(namaconfig, "w") as jsonFile:
					json.dump(config, jsonFile)
				
				os.system("python autofan.py")
			
		elif pil==4:
			getlistfans()
			print('berhasil')
			os.system("python autofan.py")
		
		elif pil==5:
			delfbcepet()
		
		
		elif pil==6:
			unfanback()
		elif pil==7:
			fancepet()
		

