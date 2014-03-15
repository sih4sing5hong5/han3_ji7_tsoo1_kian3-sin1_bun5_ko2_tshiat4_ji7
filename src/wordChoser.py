
新聞原始稿=open('/home/Ihc/新聞稿-add sharp2','r') 
輸出稿=open('/home/Ihc/新聞稿字根','w')

for 行 in 新聞原始稿:
	if len(行.strip().split()) >1:
		continue
	else: 
		輸出稿.write(行[0]+'\n')
	#if 行的陣列[1] == "##":
	#	continue
	#else:
	#	輸出稿.write(行的陣列[0]+'\n')
		
