from datetime import datetime 
with open(datetime.now().strftime('%d-%m-%y'),'w') as file:
    file.write('Automated using python')