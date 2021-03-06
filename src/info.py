import sys
import os
import platform

def CPUinfo():
#infofile on Linux machines:
  infofile = '/proc/cpuinfo'
  cpuinfo = {}
  if os.path.isfile(infofile):
    f = open(infofile, 'r')
    for line in f:
      try:
	name, value = [w.strip() for w in line.split(':')]
      except:
	continue
      if name == 'model name':
	cpuinfo['CPU type'] = value
      elif name == 'cache size':
	cpuinfo['cache size'] = value
      elif name == 'cpu MHz':
	cpuinfo['CPU speed'] = value + 'Hz'
      elif name == 'vendor ID':
	cpuinfo['vendor ID'] = value
    f.close()
  return cpuinfo

if __name__ == '__main__':
  r0 = CPUinfo()
  r1 = platform.uname()
  r2 = platform.platform()
  r3 = platform.python_version()
  r4 = platform.python_build()
  
  nombre=(sys.argv[1])
  
  try:
    fichero=open(nombre,'w')
    fichero.write ("%s\n" %r0)
    for h in r1:
      fichero.write ("%s\n" %h)
    fichero.write ("%s\n" %r2)
    fichero.write ("%s\n" %r3)
    for l in r4:
      fichero.write ("%s\n" %l)
    fichero.close()
  except IOError:
    print 'El fichero no existe'
    print r0 + r1 + r2 + r3 + r4
  
  
  