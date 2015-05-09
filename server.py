import socket
import sys
import threading
import time
import struct
#modeHz=0
#posHz=0
#dirHz=0
#kill=0
#sema=threading.Semaphore()
ip='127.0.0.1'#socket.gethostbyname(socket.gethostname())#"127.0.0.1"
a={'mode':1,'pos':28,'dir':1}
def server(port=2222):	
	s=socket.socket()
	s.bind(('',port))
	s.listen(1)
	cs,ca=s.accept()
	#ip=str(ca[0])
	print ip
	print ca
	#automode=0
	#autopos=0
	#autodir=0
	#mode=threading.Thread(name='mode',target=mode_sender)
	#pos=threading.Thread(name='pos',target=pos_sender)
	#dir=threading.Thread(name='dir',target=dir_sender)
	#mode.start()
	#pos.start()
	#dir.start()
	r=''
	pat="<5s10s5si5si5si"
	try:
		while True:
			r=cs.recv(0x4000)
			input=r.split(' ')
			if r[:3]=="GET":
				try:
					cs.sendall('RET '+str(a[input[1][:-1]])+'\n')
				except:
					cs.sendall(struct.pack(pat,"RET","STRUCT",'mode',a['mode'],'pos',a['pos'],'dir',a['dir'])+'\n')
					#packet=struct.pack("<5s5si5si5si","RET ",'mode',a['mode'],'pos',a['pos'],'dir',a['dir'])
					#cs.sendall(repr(packet)[1:-1]+'\n')
					#print repr(packet)[1:-1]
			elif r[:3]=="PAT":
				cs.sendall("RET PAT "+pat+' \n')
			elif r[:3]=="SET":
				a[input[1]]=int(input[2][:-1])
			#elif r[:3]=="REF":
			#	if input[1]=='mode':
			#		modeHZ=int(input[2][:-1])
			#	elif input[1]=='pos':
			#		posHZ=int(input[2][:-1])
			#	elif input[1]=='dir':
			#		dirHZ=float(input[2][:-1])
			r=''
	finally:
		#kill=1
		#sema.acquire()
		#sema.acquire()
		#sema.acquire()
		cs.close()
		s.close()
"""
def mode_sender():
	global ip
	global kill
	global modeHz
	s=socket.socket()
	s.connect((ip,3333))
	while True:
		if kill==1:
			s.close()
			break
		if modeHz==0:
			continue
		else:
			s.sendall('%d\n'%a['mode'])
			time.sleep(1.0/modeHz)
	sema.release()
	
def dir_sender():
	global ip
	global kill
	global dirHz
	s=socket.socket()
	s.connect((ip,4444))
	while True:
		if kill==1:
			s.close()
			break
		if dirHz==0:
			continue
		else:
			s.sendall('%d\n'%a['dir'])
			time.sleep(1.0/dirHz)
	sema.release()
	
			
def pos_sender():
	global ip
	global kill
	global posHz
	s=socket.socket()
	s.connect((ip,5555))
	while True:
		if kill==1:
			s.close()
			break
		if posHz==0:
			continue
		else:
			s.sendall('%d\n'%a['pos'])
			time.sleep(1.0/posHz)
	sema.release()
"""			
if __name__=='__main__':
	if len(sys.argv)==2:
		server(int(sys.argv[1]))
	else:
		server()
		
