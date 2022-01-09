#bt/ burst time = waktu yang dibutuhkan
#wt / waiting time = waktu tunggu
#tat / turn around time = waktu penyelesaian
#task = tugas
programs=[]
def Waktu_tunggu(Proses ,tugas,bt,wt,Quantum):
    sisaWaktu=[0]*tugas
    for totalWaktuSelesai in range(tugas):
        sisaWaktu[totalWaktuSelesai]=bt[totalWaktuSelesai]
    t=0
    while(1):
        done=True
        for totalWaktuSelesai in range(tugas):
            if(sisaWaktu[totalWaktuSelesai]>0):
                done=False
                if(sisaWaktu[totalWaktuSelesai]>Quantum):
                    t+=Quantum
                    programs.append(("P"+str(totalWaktuSelesai))*(Quantum))
                    sisaWaktu[totalWaktuSelesai]-=Quantum
                else:
                    t+=sisaWaktu[totalWaktuSelesai]
                    wt[totalWaktuSelesai]=t-bt[totalWaktuSelesai]
                    programs.append(("P"+str(totalWaktuSelesai))*(sisaWaktu[totalWaktuSelesai]))
                    sisaWaktu[totalWaktuSelesai]=0
        if(done==True):
            break

def TurnAroundTime(Proses,tugas,bt,wt,tat):
    for totalWaktuSelesai in range(tugas):
        tat[totalWaktuSelesai]=bt[totalWaktuSelesai]+wt[totalWaktuSelesai]
def FindAvgTime(Proses,tugas,bt,Quantum):
    wt=[0]*tugas
    tat=[0]*tugas
    Waktu_tunggu(Proses,tugas,bt,wt,Quantum)
    TurnAroundTime(Proses,tugas,bt,wt,tat)
    print("Program  Waktu yang dibutuhkan  Waktu tunggu", "Waktu penyelesaian")
    total_wt = 0
    total_tat = 0
    for totalWaktuSelesai in range(tugas):
        total_wt+=wt[totalWaktuSelesai]
        total_tat+=tat[totalWaktuSelesai]
        print(" ",totalWaktuSelesai+1, "\t\t", bt[totalWaktuSelesai],"\t\t", wt[totalWaktuSelesai], "\t\t", tat[totalWaktuSelesai])
    print("\nRata-rata Waktu Tunggu = %.2f "%(total_wt /tugas) ) 
    print("Rata-rata Waktu Penyelesaian = %.2f "% (total_tat /tugas)) 

JumlahProses=int(input("Masukkan Jumlah Proses-->"))
JatahWaktu=int(input("Masukkan Jatah Waktu-->"))
Burst_time=[]
Process_id=[0,1,2,3]
for totalWaktuSelesai in range(JumlahProses):
    Burst_time.append(int(input("Masukkan waktu Proses "+str(input("Nama Program : ")) +str(totalWaktuSelesai)+ "  ")))

def sort():
    return sorted(programs.items(), key=lambda item: item[1], reverse=False)
FindAvgTime(Process_id,JumlahProses,Burst_time,JatahWaktu)
Index=[int(totalWaktuSelesai) for totalWaktuSelesai in range(sum(Burst_time)+1)]
print("Banyak Program---->",*programs,"\nTotal Waktu Penyelesaian---->",*Index)
