import socket
import sys
import struct
def mync(adder,port):
	ap=(str(adder),int(port))
	s=socket.socket()
	s.connect(ap)
	s.settimeout(.1)
	pat="<5s10s5si5si5si"
	try:
		while(True):
			cmd=raw_input("> ")
			s.sendall(cmd+'\n')
			try:
				ret=s.recv(0x8000)
				if "STRUCT" in ret:
					vals=struct.unpack(pat,ret[:-1])
					print reduce(lambda i,v: i+v+' ',map(str,vals),'')
				elif "PAT" in ret:
					print "prev: "+pat
					pat=ret.split(' ')[2]
					print "new:  "+pat
				else:
					print ret[:-1]
			except socket.timeout:
				continue
	finally:
		s.close()

	
if __name__=="__main__":
	mync(sys.argv[1],sys.argv[2])
