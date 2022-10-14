
#updated version
import json, requests
url = ('https://raw.githubusercontent.com/normansimonr/Dumb-Cogs/master/lolz/data/tranzlashun.json')
resp = requests.get(url)
data = json.loads(resp.text)

with open('english.txt', 'r') as input_file:
    with open('lolcat.txt', 'w') as output_file:
        for line in input_file:
            for word in line.split():
                output_file.write(data.get(word.lower(), word.lower()))
                output_file.write(' ')
            output_file.write('\n')

# coding: utf-8

# In[1]:


#Import file from url
import json, requests
url = ('https://raw.githubusercontent.com/normansimonr/Dumb-Cogs/master/lolz/data/tranzlashun.json')
resp = requests.get(url)
data = json.loads(resp.text)
data #-----> This was to test and make sure data loaded properly


# In[41]:


#Read txt file in english
#def translate(lol_dict):
user_file = input("Enter the txt file in English that you'd like translated:")
file = open(user_file , "r")
english_doc = file.readlines()
print(english_doc)


# In[42]:


#Populate iterative list
lolcat_dict = []
for line in english_doc:
    for word in line.split():
        translation = data.get(word.lower(), word)
        lolcat_dict.append(translation)


# In[43]:


print(lolcat_dict)


# In[44]:


#Save translation as new file
translated_file = open(user_file +"_lolcat.txt", "w")
for row in lolcat_dict:
    translated_file.write(row)
    #translated_file.close() #Make sure this isn't indented to close


# In[45]:


print(translated_file)

