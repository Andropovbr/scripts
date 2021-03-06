#Author: André Luiz Fernandes dos Santos
#Contact: andresantosbr@gmail.com
#Date: 04/23/2019

#This script is coded in Python 3.7.3, its purpose is to take a list of subdomains,
#extract the domain name from each subdomain, removing any redundant domain

import tldextract

#Read ACLs from file
file_acl = open("file.txt", "r")
list_subdomains = file_acl.readlines()
int_subdomains_count = len(list_subdomains)

list_domains = []
i = 0

#Extract domain name from subdomains
for item in list_subdomains:
	list_domains.append(tldextract.extract(item.rstrip()).registered_domain)
	i += 1
	print("Processed "+ str(i) + " entries of "+ str(int_subdomains_count), end='\r')

#Remove redundant domains
list_domains = list(dict.fromkeys(list_domains))
domain_count = len(list_domains)

print("\n"+"Deleted entries: "+str(int_subdomains_count - domain_count))
print("Domain count: "+str(domain_count))

#Write result in a file
with open('acl_new.txt', mode='wt', encoding='utf-8') as myfile:
    myfile.write('\n'.join(list_domains))

file_acl.close()