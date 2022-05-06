if __name__ == '__main__':
	import sys
	import os
	import numpy as np
	#---
	lnums = [ 33, 39, 46, 88   ]
	string=open('Preparation.py').readlines() #--- python script
	#---
#        MC = [-0.25,-0.1,0.0,0.1,0.2]
#        B = [1.1,1.2,1.3]
#        DF = [1.3,1.4,1.5]
#	PHI = np.logspace(-5.0,-2.0,nphi,endpoint=True)
#	PHI = np.linspace(2.3,2.9,nphi,endpoint=True)
#	PHI = np.linspace(0.05,0.45,nphi,endpoint=True)
#	PHI=range(0,200,1) 
#	PHI = [12500,25000,50000]
#	PHI = np.linspace(1800, 3000, 10, endpoint=True, dtype=int) #--- melt. temp.
	PHI ={
#			'0':'CuZr3',
#             '0':'FeNi',
#             '1':'CoNiFe',
#            '2':'CoNiCrFe',
#            '3' :'CoCrFeMn',
#             '4':'CoNiCrFeMn',
             '5':'Co5Cr2Fe40Mn27Ni26'
         }
	EPS = { 
#			'0':1.0,
#			'1':2.0,
#			'2':4.0,
			'3':8.0
		  }

	nphi = len(PHI)
	#---
#	nn = 4
#	NTHRESH = np.linspace(0.05,0.11,nn,endpoint=True)
	#---
	times=np.arange(0,200+1,8) #[0,50,101,120,195] #np.arange(0,200+8,8)
	#--- 
	count = 0
	for iphi in PHI:
		for epsi in EPS:
			for itime in times:
			#---	
			#---	densities
				inums = lnums[ 0 ] - 1
				string[ inums ] = "\t4:'ElasticityT300/%s/eps%s/itime%s',\n"%(PHI[iphi],epsi,itime) #--- change job name
			#---
				inums = lnums[ 1 ] - 1
				string[ inums ] = "\t3:'/../glass%s',\n"%(PHI[iphi])
#				string[ inums ] = "\t2:'/CuZrNatom32KT300Tdot1E-1Sheared',\n"
			#---
				inums = lnums[ 2 ] - 1
				string[ inums ] = "\t3:['data.%s.txt','%s_glass.dump','%s.txt'],\n"%(itime,PHI[iphi],PHI[iphi])
#				string[ inums ] = "\t6:['data.%s.txt','dumpSheared.xyz'],\n"%(itime)
			#---
				inums = lnums[ 3 ] - 1
#				string[ inums ] = "\t10:' -var T 300.0 -var teq  2.0 -var nevery 100 -var ParseData 1 -var DataFile data.%s.txt',\n"%(itime)
				string[ inums ] = "\t11:' -var T 300.0 -var A 0.1 -var Tp %s -var nevery 100 -var DumpFile shearOscillation.xyz -var ParseData 1 -var DataFile data.%s.txt',\n"%(EPS[epsi],itime)

				sfile=open('junk%s.py'%count,'w');sfile.writelines(string);sfile.close()
				os.system( 'python junk%s.py'%count )
				os.system( 'rm junk%s.py'%count )
				count += 1
