kalimat = (input("Kalimat yang ingin diteliti : "))
kata = (input("Kata yang ingin dicari : "))

for i in kalimat: 
    rumus = kalimat.count(kata)
    print("Jumlah kata yang dicari :",rumus)
    break


