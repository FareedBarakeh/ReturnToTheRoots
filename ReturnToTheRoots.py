# !/usr/bin/env python
# -*- coding: utf-8 -*-
    

def utf(x):
    return x.encode('utf-8')

def getbranches(x, y, z):
    return [((AHAMZAUP) + (x) + (y) + (z)), #أعلم 
     ((x) + (y) + (z) + (A) + (N) + (E)), #علماني 
     ((M) + (x) + (y) + (O) + (z) + (A) + (T)), #معلومات 
     ((x) + (y) + (A) + (z)), #علام 
     ((M) + (x) + (y) + (O) + (z) + (TA)), #معلومة
     ((M) + (x) + (y) + (z)), #معلم x
     ((M) + (x) + (y) + (A) + (L) + (z)), #معالم
     ((A) + (x) + (y) + (A) + (z)), #أعلام x
     ((M) + (x) + (y) + (z) + (TA)) , #معلمة x
     ((x) + (y) + (z) + (A) + (N) + (E) + (TA)) , #علمانية
     ((T) + (x) + (y) + (z) + (E) + (M) + (E)) , #تعليمي
     ((T) + (x) + (y) + (E) + (z) + (A) + (T)) , #تعليمات 
     ((T) + (x) + (y) + (E) + (z)) , #تعليم
     ((AHAMZAUPDOWN) + (x) + (y) + (A) + (z) + (E)) , #إعلامي
     ((M) + (x) + (y) + (O) + (z)), #معلوم
     ((T) + (x) + (y) + (z)) , #تعلم
     ((A) + (S) + (T) + (x) + (y) + (A) + (z)) , #استعلام
     ((x) + (A) + (y) + (z) + (TA)) , #عالمة
     ((x) + (A) + (y) + (z) + (E) + (TA)) , #عالمية
     ((x) + (A) + (y) + (z)) , #عالم x 
     ((M) + (T) + (x) + (y) + (z)) , #متعلم
     ((x) + (A) + (y) + (z) + (E)) , #عالمي
     ((x) + (y) + (A) + (z) + (TA)) , #علامةx
     ((AHAMZAUPDOWN) + (x) + (y) + (A) + (z)) , #إعلام
     ((x) + (y) + (A) + (z)) , #علام
     ((AHAMZAUP) + (x) + (y) + (A) + (z)) , #أعلام
     ((x) + (y) + (E) + (z)) , #عليمX
     ((AHAMZAUP) + (x) + (y) + (O) + (z) + (TA)) , #أعلومة
     ((T) + (x) + (y) + (A) + (z)+ (TA)) , #تعلامة
     ((x) + (y) + (z) + (E)) , #علمي
     ((x) + (y) + (z)) , #علم x
     ((M) + (x) + (y) + (O) + (z) + (E) + (TA)) , #معلومية
     ((x) + (y) + (z) + (E) + (TA)) , #علمية
     ((x) + (O) + (A) + (y) + (z)) , #عوالم
     ((x) + (y) + (O) + (z)) , #علوم
     ((T) + (x) + (A) + (y) + (z))  #تعالم
     ]

A = utf(u'ا')
AHAMZAUP = utf(u"أ")
AHAMZAUPDOWN = utf(u"إ")
B = utf(u"ب")
T = utf(u"ت")
TA =utf(u"ة")
TH = utf(u"ث")
J = utf(u"ج")
H = utf(u"ح")
KH = utf(u"خ")
D = utf(u"د")
Z = utf(u"ذ")
R = utf(u"ر")
ZA = utf(u"ز")
S = utf(u"س")
SH = utf(u"ش")
SA = utf(u"ص")
DA = utf(u"ض")
TAA = utf(u"ط")
DAA = utf(u"ظ")
AE = utf(u"ع")
GA = utf(u"غ")
F = utf(u"ف")
K = utf(u"ق")
KA = utf(u"ك")
L = utf(u"ل")
M = utf(u"م")
N = utf(u"ن")
HA = utf(u"ه")
O = utf(u"و")
E = utf(u"ي")
AA = utf(u"ى")
HAMZA = utf(u"ء")


words = getbranches(N, DAA, M)


#with open('./temp.txt', 'w', encoding='utf-8') as f:
with open('S:\Projects\Programing Projects\-\Projects\Arabic-Tree/derivations.txt', 'w', encoding='utf-8') as f:

    for word in words:
        f.write(word.decode('utf-8'))
        f.write('\n')
        












