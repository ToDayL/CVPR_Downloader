# HTML Parser

import os
import bs4
import requests

CVPR_OpenAccess = open('../HTML/CVPR_Open_Access.html')
CVPR_OpenAccess_bs4 = bs4.BeautifulSoup(CVPR_OpenAccess)

# CVPR_OpenAccess_List = open('../Webpage/CVPR_Open_Access.txt', 'w')

Article_Dic = {}
# print(CVPR_OpenAccess_bs4.prettify())

DownloadRegion = CVPR_OpenAccess_bs4.find('dl')
currentPointer = DownloadRegion.find_next('dt')

total = 0

while True:
    # print(currentPointer.a.string)
    paperName = currentPointer.a.string
    # CVPR_OpenAccess_List.write(currentPointer.a.string + '\n')
    currentPointer = currentPointer.find_next('dd')
    currentPointer = currentPointer.find_next('dd')
    # print(currentPointer.a['href'])
    # CVPR_OpenAccess_List.write(currentPointer.a['href'] + '\n' + '\n')

    if paperName in Article_Dic:
        continue
    else:
        Article_Dic[paperName] = currentPointer.a['href']
        total = total + 1

    currentPointer = currentPointer.find_next('dt')
    if currentPointer is None:
        break

print('Parcer CVPR_OpenAccess List Done')
# CVPR_MC_List = open('../Webpage/CVPR_MC.txt', 'w')

CVPR2017_MC_Web = open('../Webpage/CVPR2017.html')
CVPR2017_MC_Web_bs4 = bs4.BeautifulSoup(CVPR2017_MC_Web)
mainTable_Pointer = CVPR2017_MC_Web_bs4.find('h4')
mainTable_Pointer = mainTable_Pointer.find_next('h4', id='program_schedule')
mainTable_Pointer = mainTable_Pointer.find_next('table')

cnt = 0
Category = ''
while True:
    mainTable_Pointer = mainTable_Pointer.find_next('tr')

    if cnt == 51:
        print(cnt)

    if mainTable_Pointer is None:
        break

    for j in range(5):
        mainTable_Pointer = mainTable_Pointer.find_next('td')

    mainTable_Pointer = mainTable_Pointer.find_next('td')
    if mainTable_Pointer.string is not None:
        Category = mainTable_Pointer.string
        FolderName = Category.replace(' ', '').replace('/', '')
        if not os.path.exists('../Papers/' + FolderName):
            os.mkdir('../Papers/' + FolderName)

    print(Category)
    mainTable_Pointer = mainTable_Pointer.find_next('td')
    mainTable_Pointer = mainTable_Pointer.find_next('td')

    print(mainTable_Pointer.string)
    if mainTable_Pointer.string in Article_Dic:
        filename = os.path.basename(Article_Dic[mainTable_Pointer.string])
        if os.path.exists('../Papers/' + FolderName + '/' + filename):
            cnt = cnt + 1
            print('skip ' + filename)
        else:
            print('Downloading from ' + Article_Dic[mainTable_Pointer.string])
            pdf_data = requests.get(Article_Dic[mainTable_Pointer.string])

            pdf_file = open('../Papers/' + FolderName + '/' + filename, 'wb')
            pdf_file.write(pdf_data.content)
            pdf_file.close()
            cnt = cnt + 1
            print('Download ' + filename + ' to ' + FolderName + ' Done!')
        print('current/total: ' + str(cnt) + '/' + str(total))

    mainTable_Pointer = mainTable_Pointer.find_next('td')
    print(mainTable_Pointer.string + '\n')
    # CVPR_MC_List.write('\n')

# CVPR_MC_List.close()
# CVPR_OpenAccess_List.close()
