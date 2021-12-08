opcode=['ADD','ADDF','AND','COMP','COMPF','DIV','DIVF','J','JEQ','JGT','JLT','JSUB','LDA','LDS','LDX','LDCH','LDF','LDL','LDT','LPS','MUL','MULF','OR','RD','RSUB','SSK','STA','STB','STCH','STF','STI','STL','STS','STSW','STT','STX','SUB','SUBF','TD','TIX','WD']
dec=['RESB','RESW','WORD','BYTE']
import fileinput as fp
ip=[]
ip2=[]
symtab={}
errtab={}
for line in fp.input(files='C:\\Users\Adarsha K K\Documents\Python Scripts\sicip.txt'):
     ip.append(line)
for i in ip:
    ip2.append(i.split())
loc=int(ip2[0][2])
l=len(ip2)
for i in range(1,l):
    if(len(ip2[i])<3):
        if(ip2[i][0] in opcode):
            loc=loc+3
        else:
            errtab[i+1]="invalid opcode"
            loc=loc+3
                
    if(len(ip2[i])==3):
        if(ip2[i][0] not in symtab.keys()):
            symtab[ip2[i][0]]=loc
        else:
            errtab[i+1]="Duplicate Symbol"       
        if(ip2[i][1] in opcode):
            loc=loc+3
        else:
            if(ip2[i][1] not in dec):
                   errtab[i+1]="invalid opcode/declaration"
        if(ip2[i][1]=="BYTE"):
            if((ip2[i][2][0:2]=="C'")or(ip2[i][2][0:2]=="X'")):
                loc=loc+len(ip2[i][2])-3
            else:
                loc=loc+1
        if(ip2[i][1]=="WORD"):
            if((ip2[i][2][0:2]=="C'")or(ip2[i][2][0:2]=="X'")):
                loc=loc+3*(len(ip2[i][2])-3)
            else:
                loc=loc+3
        if(ip2[i][1]=="RESB"):
            loc=loc+int(ip2[i][2])
        if(ip2[i][1]=="RESW"):
            loc=loc+3*(int(ip2[i][2]))
        
print(symtab)
print(errtab)