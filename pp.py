import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt
data=[]
df=pd.read_csv('/data/MOCK_DATA.csv')#Data file
data=df['email']#Selecting Columns

email_data=[]
for i in range(0,len(data)):#I have no clue why I did this...But it works
    
    while i in data:
        email_data.append(re.findall("(?<=@)[\w+.-]+",data[i]))#Regular expression for filtering email domain name from data
        i=i+1
    break
filtered_email_data=[' '.join([str(c) for c in lst]) for lst in email_data]#converting nested lists into strings
domain_list=[]
j=0#initializing index

for j in range(0,len(filtered_email_data)):#adding domail expections to array
    domain_list.append(re.findall(("[.].*"),filtered_email_data[j]))#regular expression for filtering email-domain extention from data
    j=j+1

filtered_domain_list=[' '.join([str(c) for c in lst]) for lst in domain_list]#Converting nested lists into strings

x=np.array(filtered_domain_list)
unique,counts=np.unique(x,return_counts=True)

############################|||Plottig|||######################

plt.plot(counts,unique)
plt.xlabel('Counts')
plt.ylabel('Email domain-extension name')
plt.show()