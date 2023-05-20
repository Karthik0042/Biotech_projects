amino_acids = {
    "Ala": ["GCU", "GCC", "GCA", "GCG"],
    "Arg": ["CGA", "CGG", "AGA", "AGG"],
    "Asn": ["AAU", "AAC"],
    "Asp": ["GAU", "GAC"],
    "Cys": ["UGU", "UGC"],
    "Gln": ["CAA", "CAG"],
    "Glu": ["GAA", "GAG"],
    "Gly": ["GGU", "GGC", "GGA", "GGG"],
    "His": ["CAU", "CAC"],
    "Ile": ["AUU", "AUC", "AUA"],
    "Leu": ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"],
    "Lys": ["AAA", "AAG"],
    "Met": ["AUG"],
    "Phe": ["UUU", "UUC"],
    "Pro": ["CCU", "CCC", "CCA", "CCG"],
    "Ser": ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"],
    "Thr": ["ACU", "ACC", "ACA", "ACG"],
    "Trp": ["UGG"],
    "Tyr": ["UAU", "UAC"],
    "Val": ["GUU", "GUC", "GUA", "GUG"]
}

bases = ['A', 'C', 'G', 'U']
codons_list = [a + b + c for a in bases for b in bases for c in bases]

def reverse_complement(seq):
    complement = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join(complement[base] for base in reversed(seq)) #Generating complementary base pairs

def transcribe(dna):
    return dna.replace("T", "U") #Transcription done
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




dna="ACTTGTATGGGATCGCACATTATGCGTTAAGTATTA"
print(f"{dna} is the original DNA strand")
mRNA=(transcribe(reverse_complement(dna)))
print(f"The mRNA sequence after transcription {mRNA}")
print("Translating the mRNA sequence we get")
forward_translate(mRNA)
reverse_translate(mRNA)
