from prettytable import PrettyTable

def round_robin():
    numb = int(input("Enter the number of processes: "))
    quant = int(input("Enter the Quantum range: "))
    a=[]
    for i in range(numb):
        b=[]
        name = str(input("Enter process name: "))
        burst = int(input("Enter the burst time: "))
        b.append(name)
        b.append(burst)
        a.append(b)
    print("Initial list:",a)

    bt=[]
    prc=[]
    fbt=[]
    for i in range(len(a)):
        bt.append(a[i][1])
        fbt.append(a[i][1])
        prc.append(a[i][0])
    print("burst time: ",bt)
    print("The processes: ", prc)
    print("\n")
            
    #to print the time line of the process    
    line=[]
    add=0
    while any(bt[i]!=0 for i in range(len(bt))):
        for j in range(len(bt)):
            if (bt[j]<quant and bt[j]!=0):
                evry=[]
                add+=bt[j]
                evry.append(prc[j])
                evry.append(add)
                line.append(evry)
                bt[j]-=bt[j]
            elif bt[j]>=quant:
                evry=[]
                add+=quant
                bt[j]-=quant
                evry.append(prc[j])
                evry.append(add)
                line.append(evry)
    print(line)


    #to associate the processes and their turn around time
    dit={}
    for i in range(len(line)):
        if line[i][0] in dit.keys():
            dit[line[i][0]]=line[i][1]
        elif line[i][0] not in dit.keys():
            dit.update({line[i][0]:line[i][1]})
                    
    print("processes and tat", dit)

    #to find the turn adound time from the dictionary above
    tat=[]
    for i in dit.keys():
        tat.append(dit[i])
    print('turn around time: ', tat)


    #to find waiting time (wt=tat-bt)
    wt=[]
    for i in range(len(fbt)):
        wt.append(tat[i]-fbt[i])
    print("waiting time: ",wt)

    #to present all the data in the form of a tabular-data
    t = PrettyTable(['Process', 'Turnaround Time', "Waiting Time"])
    for i in range(len(prc)):
        t.add_row([prc[i],tat[i],wt[i]])
    print(t)
        

    #average turn around time
    sum1=0
    for i in tat:
        sum1+=i
        h1=(sum1/len(tat))
    print("Average turn around time: ", h1)

    #average waiting time
    sum2=0
    for i in wt:
        sum2+=i
        h2=sum2/len(wt)
    print("Average waiting time: ", h2)

           
    
round_robin()
