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
