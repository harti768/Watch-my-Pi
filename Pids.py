import psutil
import sys
import os

def Pi(Core):
	Process_int = 0
	Processes = []
	Processes_D = {}
	pids = psutil.pids()
	draw = 0
	PID = "PID"
	CPU = "CPU"
	PID_name = "PID_name"
	warn = False
	
	for pid in pids:
		Process_int = Process_int + 1
		print Process_int, " current", Processes
		p = psutil.Process(int(pid))
		if (p.is_running() == True) & (p.status() == psutil.STATUS_RUNNING):
			pid_name = p.name()
			cpu = p.cpu_percent(interval=0.2) 
			
			if cpu > 8:
	
				print pid, " ", cpu," " , pid_name
				Processes.append(pid)
				PID = "PID"+str(draw)
				CPU = "CPU"+str(draw)
				PID_name = "PID_name"+str(draw)
				PR1 = {PID:pid,CPU:cpu,PID_name:pid_name}
				Processes_D.update(PR1)
				draw = draw + 1
			elif cpu >= (85*Core):
				print pid, " ", cpu," " , pid_name
				Processes.append(pid)
				PID = "PID"+str(draw)
				CPU = "CPU"+str(draw)
				PID_name = "PID_name"+str(draw)
				PR1 = {PID:pid,CPU:cpu,PID_name:pid_name}
				Processes_D.update(PR1)
				warn = True
				break
			else:
				os.system('clear')
		else:
			os.system('clear')	
	if (warn != True):
		print "total processes: ", Process_int
		for i in range(0,draw):
			try:
				p = psutil.Process(int(Processes_D["PID"+str(i)]))
				cpu1 = p.cpu_percent(interval=1)
				cpu2 = cpu1 / int(Core)
				print Core, " Core(s)" 
				#print Processes_D["PID"+str(i)], " ",cpu2 ,"percent of CPU  ", Processes_D["PID_name"+str(i)]  #Processes_D["CPU"+str(i)] 
				return "%d | %d percent of CPU | %s" % (Processes_D["PID"+str(i)], cpu2, Processes_D["PID_name"+str(i)])
				
			except:
				return "%d | %d percent of CPU | %s" % (Processes_D["PID"+str(i)], Processes_D["CPU"+str(i)], Processes_D["PID_name"+str(i)])
				
	else: 			
		print "WARNING! WARNING! System will be repaired..."
		PID.kill()
		return PID, " ", PID_name, "could be a problem for you, and may could damage your PC! Please keep that in mind."

