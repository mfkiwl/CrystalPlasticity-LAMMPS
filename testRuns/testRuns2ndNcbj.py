def makeOAR( EXEC_DIR, node, core, time):
	someFile = open( 'oarScript.sh', 'w' )
	someFile.write('#!/bin/bash\n')
	someFile.write('EXEC_DIR=%s\n' %( EXEC_DIR ))
	someFile.write('module unload gcc/4.6.3;module load gcc/9.3.0\n')

	someFile.write("ovitos $EXEC_DIR/OvitosCna.py %s" %( args )) #--- cna analysis in ovito!
	someFile.close()										  


if __name__ == '__main__':
	import os

	nruns	 = 3
	nThreads = 1
	jobname  = 'glassFeNi' #--- existing directory
	args = 'FeNi_glass.dump FeNi_Cna.xyz' #--- input, output
	sourcePath = os.getcwd() + '/dataFiles'
	EXEC_DIR = '/mnt/home/kkarimi/Project/git/CrystalPlasticity/py' #--- path for executable file
	durtn = '29:59:59'
	SCRATCH = None
	resources = {'mem':'16gb', 'partition':'o12h','nodes':1,'ppn':1}
	#--- update data.txt and lammps script
	#---
	os.system( 'rm jobID.txt' )
	# --- loop for submitting multiple jobs
	counter = 0
	for irun in range( nruns ):
		print(' i = %s' % counter)
		writPath = os.getcwd() + '/%s/Run%s' % ( jobname, counter ) # --- curr. dir
#		os.system( 'mkdir -p %s' % ( writPath ) ) # --- create folder
		if irun == 0: #--- cp to directory
			path=os.getcwd() + '/%s' % ( jobname)
#			os.system( 'cp %s/%s %s' % ( EXEC_DIR, , path ) ) # --- create folder & mv oar scrip & cp executable
		#---
#		os.system( 'cp shearMG300-11.in %s/in.txt ' % writPath ) #--- lammps script: periodic x, pxx, vy, load
#		os.system( 'cp %s/FeNi_glass_300.data %s ' % (sourcePath, writPath) ) #--- lammps script: periodic x, pxx, vy, load
#		os.system( 'cp %s/parameters.meam %s ' % (sourcePath, writPath) ) #--- lammps script: periodic x, pxx, vy, load
#		os.system( 'cp %s/library_CoNiCrFeMn.meam %s ' % (sourcePath, writPath) ) #--- lammps script: periodic x, pxx, vy, load
		#---
		#---
		makeOAR( EXEC_DIR, 1, nThreads, durtn) # --- make oar script
		os.system( 'chmod +x oarScript.sh; mv oarScript.sh %s' % ( writPath) ) # --- create folder & mv oar scrip & cp executable
		os.system( 'qsub -q %s -l nodes=%s:ppn=%s -N %s.%s -o %s -e %s -d %s  %s/oarScript.sh'\
			%( resources['partition'], resources['nodes'], resources['ppn'], jobname, counter, writPath, writPath, writPath , writPath ) ) # --- runs oarScript.sh!
		counter += 1
											 
	os.system( 'mv jobID.txt %s' % ( os.getcwd() + '/%s' % ( jobname ) ) )
