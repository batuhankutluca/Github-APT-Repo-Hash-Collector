from github import Github 
import re

g = Github("input access token here")

repo = g.get_user().get_repo("APT_Digital_Weapon")

contents = repo.get_contents("")

"""for content_file in contents:
	print(content_file)"""
hashlist = []
hashlist2 = []
while contents:
	file_content = contents.pop(0)
	if file_content.type == "file":
		if file_content.name == "LICENSE":
			pass
		elif file_content.name == "logo.png":
			pass
		elif file_content.name == "README.md":
			pass
		elif file_content.name == "README.MD":
			pass
		else:
			hashlist.append(file_content.decoded_content.decode("utf-8"))
	else:
		contents.extend(repo.get_contents(file_content.path))
for i in range(0,len(hashlist)):
	hash = re.findall(r"\[(.*?)\]",hashlist[i])
	for j in range(0,len(hash)):
		hashlist2.append(hash[j])
#print(hashlist2)
f = open('enter path here','w')
for hsh in hashlist2:
	f.write(hsh+"\n")
f.close()
