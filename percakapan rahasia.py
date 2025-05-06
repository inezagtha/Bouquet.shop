def deskripsi_kalimat_rahasia(kalimat_rahasia):
    
    kata_kata = kalimat_rahasia.split()

    kalimat_normal = ' '.join(kata[::-1] for kata in kata_kata)
    return kalimat_normal

contoh = [
    "italem irad irigayaj",
    "iadab itsap ulalreb",
    "nalub kusutret gnalali"
]

for i, contoh in enumerate(contoh, start=1):
    print(f"hasil untuk contoh #{i} : {deskripsi_kalimat_rahasia(contoh)}")