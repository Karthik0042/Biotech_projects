amino_acids = {
    "Ala": ["GCT", "GCC", "GCA", "GCG"],
    "Arg": ["CGT", "CGC", "CGA", "CGG", "AGA", "AGG"],
    "Asn": ["AAT", "AAC"],
    "Asp": ["GAT", "GAC"],
    "Cys": ["TGT", "TGC"],
    "Gln": ["CAA", "CAG"],
    "Glu": ["GAA", "GAG"],
    "Gly": ["GGT", "GGC", "GGA", "GGG"],
    "His": ["CAT", "CAC"],
    "Ile": ["ATT", "ATC", "ATA"],
    "Leu": ["TTA", "TTG", "CTT", "CTC", "CTA", "CTG"],
    "Lys": ["AAA", "AAG"],
    "Met": ["ATG"],
    "Phe": ["TTT", "TTC"],
    "Pro": ["CCT", "CCC", "CCA", "CCG"],
    "Ser": ["TCT", "TCC", "TCA", "TCG", "AGT", "AGC"],
    "Thr": ["ACT", "ACC", "ACA", "ACG"],
    "Trp": ["TGG"],
    "Tyr": ["TAT", "TAC"],
    "Val": ["GTT", "GTC", "GTA", "GTG"]
}
bases = ['A', 'C', 'G', 'T']
codons_list = [a + b + c for a in bases for b in bases for c in bases]

string=input("INPUT- ")



def forward_translate(string):


    list1 = [string[i:i + 3] for i in range(0, len(string) - 2, 3) if len(string[i:i + 3]) == 3]
    string=string[1:]
    list2=[string[i:i + 3] for i in range(0, len(string) - 2, 3) if len(string[i:i + 3]) == 3]
    string=string[1:]
    list3 = [string[i:i + 3] for i in range(0, len(string) - 2, 3) if len(string[i:i + 3]) == 3]

    protienseq1 = []
    for i in list1:
        for amino, codons in amino_acids.items():
            if i in codons:
                protienseq1.append(amino)
    protienseq1string = "-".join(protienseq1)
    print(protienseq1string)

    protienseq2 = []
    for i in list2:
        for amino, codons in amino_acids.items():
            if i in codons:
                protienseq2.append(amino)
    protienseq2string = "-".join(protienseq2)
    print(protienseq2string)

    protienseq3 = []
    for i in list3:
        for amino, codons in amino_acids.items():
            if i in codons:
                protienseq3.append(amino)
    protienseq3string = "-".join(protienseq3)
    print(protienseq3string)


def reverse_translate(string):
    rev_string=string[::-1]
    list1=[rev_string[i:i + 3] for i in range(0, len(string) - 2, 3) if len(string[i:i + 3]) == 3]
    rev_string=rev_string[1:]

    list2 = [rev_string[i:i + 3] for i in range(0, len(string) - 2, 3) if len(string[i:i + 3]) == 3]
    rev_string=rev_string[1:]

    list3 = [rev_string[i:i + 3] for i in range(0, len(string) - 2, 3) if len(string[i:i + 3]) == 3]

    protienseq1 = []
    for i in list1:
        for amino, codons in amino_acids.items():
            if i in codons:
                protienseq1.append(amino)
    protienseq1string = "-".join(protienseq1)
    print(protienseq1string)

    protienseq2 = []
    for i in list2:
        for amino, codons in amino_acids.items():
            if i in codons:
                protienseq2.append(amino)
    protienseq2string = "-".join(protienseq2)
    print(protienseq2string)

    protienseq3 = []
    for i in list3:
        for amino, codons in amino_acids.items():
            if i in codons:
                protienseq3.append(amino)
    protienseq3string = "-".join(protienseq3)
    print(protienseq3string)




forward_translate(string)
reverse_translate(string)
