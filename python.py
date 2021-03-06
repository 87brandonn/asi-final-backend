import pandas as pd
import sys
import string
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import RegexpTokenizer
import re
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
text_input = sys.argv[1]
df_ajaib = pd.read_csv('dataset_ajaib.csv')
df_ajaib['content'] = df_ajaib['content'].str.lower()
df_ajaib['content'] = df_ajaib['content'].str.replace('\d+', ' ')
df_ajaib['content'] = df_ajaib['content'].str.translate(str.maketrans("", "",  string.punctuation))
stop_factory = ['yang',
 'untuk',
 'pada',
 'ke',
 'para',
 'namun',
 'menurut',
 'antara',
 'dia',
 'dua',
 'ia',
 'seperti',
 'jika',
 'jika',
 'sehingga',
 'kembali',
 'dan',
 'tidak',
 'ini',
 'karena',
 'kepada',
 'oleh',
 'saat',
 'harus',
 'sementara',
 'setelah',
 'belum',
 'kami',
 'sekitar',
 'bagi',
 'serta',
 'di',
 'dari',
 'telah',
 'sebagai',
 'masih',
 'hal',
 'ketika',
 'adalah',
 'itu',
 'dalam',
 'bisa',
 'bahwa',
 'atau',
 'hanya',
 'kita',
 'dengan',
 'akan',
 'juga',
 'ada',
 'mereka',
 'sudah',
 'saya',
 'terhadap',
 'secara',
 'agar',
 'lain',
 'anda',
 'begitu',
 'mengapa',
 'kenapa',
 'yaitu',
 'yakni',
 'daripada',
 'itulah',
 'lagi',
 'maka',
 'tentang',
 'demi',
 'dimana',
 'kemana',
 'pula',
 'sambil',
 'sebelum',
 'sesudah',
 'supaya',
 'guna',
 'kah',
 'pun',
 'sampai',
 'sedangkan',
 'selagi',
 'sementara',
 'tetapi',
 'apakah',
 'kecuali',
 'sebab',
 'selain',
 'seolah',
 'seraya',
 'seterusnya',
 'tanpa',
 'agak',
 'boleh',
 'dapat',
 'dsb',
 'dst',
 'dll',
 'dahulu',
 'dulunya',
 'anu',
 'demikian',
 'tapi',
 'ingin',
 'juga',
 'nggak',
 'mari',
 'nanti',
 'melainkan',
 'oh',
 'ok',
 'seharusnya',
 'sebetulnya',
 'setiap',
 'setidaknya',
 'sesuatu',
 'pasti',
 'saja',
 'toh',
 'ya',
 'walau',
 'tolong',
 'tentu',
 'amat',
 'apalagi',
 'bagaimanapun']
df_ajaib['content'] = df_ajaib['content'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop_factory)]))
token = RegexpTokenizer(r'[a-zA-Z0-9]+')
cv = CountVectorizer(ngram_range = (1,1),tokenizer = token.tokenize)

text_counts = cv.fit_transform(df_ajaib['content'])
X_train, X_test, Y_train, Y_test = train_test_split(text_counts, df_ajaib['score'], test_size=0.4, random_state=10)
MNB = MultinomialNB()
MNB.fit(X_train, Y_train)
data1 = { "Content" : [text_input, "aplikasi bagus"]}
df_test1 = pd.DataFrame(data1)
text_count1 = cv.transform(df_test1['Content'])
predicted1 = MNB.predict(text_count1)
if(predicted1[0] < 3):
    print("negative")
else:
    print("positive")