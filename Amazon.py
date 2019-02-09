data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 #count = count + 1
		if count % 1000 == 0:    # %是求餘數
		    print(len(data)) #每讀一行列出來進度
print('檔案讀取完了,總共有', len(data), '筆資料') #讀取留言檔

#print(data)  #印出data清單
#print(data[0]) #印出第一筆留言
#print('-------------------------------')
#print(data[1]) #印出第二筆留言


#算出留言平均長度

sum_len = 0
for d in data:   #每一筆資料都叫做d 
    sum_len = sum_len + len(d) 
    print(sum_len)

print('留言的平均長度為', sum_len/len(data))

#篩選概念

new = []  #先創一個空白清單
for d in data:  #把清單(data)裡的留言 d(字串) 一個一個拿出來
    if len(d) < 100:  #如果你的長度小於100 就裝入 new 清單
        new.append(d)
print('一共有', len(new), '筆留言長度小於100')



good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')
print(good[0])
