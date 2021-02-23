command=''
loop=False
while True:
	file=open('newfile.txt','a+')
	try:
		if not loop and len(command)==0:
			code=(input('>>'))
			command +=code
		
		if  command[-1]==':' or loop:
			code=(input('....'))
			command +=code
			loop=True
			if code != '':
				continue
			else:
				loop=False
		
		else:
			try:
				result=eval(command)
				print(result)
				file.write(command+':'+str(result)+'\n')
				file.close()
				command=''
			except:
				try:
					result=exec(command)
					file.write(command+':'+str(result)+'\n')
					file.close()
					command=''
				except:
					print('Error on Execution')
					command=''
	except:
		print('Error while taking input')
	
