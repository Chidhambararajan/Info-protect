import datetime
import pickle
class info_protect:
    def __init__(self,path,mode):
        self.passfile=str(input("Enter the passfile name:"))
        self.path=path
        self.mode=mode
        self.inbytes=bytearray(open(self.path,'rb').read())
        self.outbytes=bytearray()
        self.basebytes=bytearray(range(256))*2
        self.temp=[]
        self.venue=''
        self.date=''
        self.time=''
        self.file=self.path.split('.')
        self.dest=''
        self.inbytes2=bytearray()
        self.extension=self.file[-1]
        if len(self.file)>2:
            self.fil_name='.'.join(self.file[:len(self.file)-1])
        else:
            self.fil_name=self.file[0]
        self.passkey=bytearray(open(self.passfile,'rb').read())
        

    def encrypt(self):
        a=-1
        while True :
            try:
                a+=1
                if a==0 :
                    file=open(self.fil_name+'.secure02','rb')
                else:
                    file=open(self.fil_name+str(a)+'.secure02','rb')
                
            except IOError :
                if a==0 :
                    self.dest=self.fil_name+'.secure02'
                    file=open(self.dest,'wb')
                else:
                    self.dest=self.fil_name+str(a)+'.secure02'
                    file=open(self.dest,'wb')
                break
        file.close()
        file=open('$temp.dat','wb')
        pickle.dump(self.inbytes,file)
        pickle.dump(self.extension,file)
        #pickle.dump(self.inbytes,file)
        file.close()
        self.inbytes2=bytearray(open('$temp.dat','rb').read())
        for i in range(len(self.inbytes2)):
                val=self.inbytes2[i]+self.passkey[i%len(self.passkey)]
                self.outbytes.append(self.basebytes[val])
        file=open(self.dest,'wb')
        file.write(self.outbytes)
        file.close()

    def decrypt(self):

        for i in range(len(self.inbytes)):
                val=self.inbytes[i]-self.passkey[i%len(self.passkey)]
                self.outbytes.append(self.basebytes[val])
        file=open('$temp.dat','wb')
        file.write(self.outbytes)
        file.close()
        file=open('$temp.dat','rb')
        self.outbytes=pickle.load(file)
        self.extension=pickle.load(file)        
        file.close()
        file=open(self.fil_name+'_decrypted'+'.'+self.extension,'wb')
        file.write(bytearray(self.outbytes))
        file.close()

    def process(self):
        if self.mode=="Enc":
            self.encrypt()
        elif self.mode=="Dec":
            self.decrypt()
        self.venue=str(datetime.datetime.now())
        self.date,self.time=self.venue.split(' ')
        self.time=self.time.split(':')
        if int(self.time[0])>=12 :
            if int(self.time[0])==12:
                self.time=str(int(self.time[0]))+':'+self.time[1]+' PM'
            else:
                self.time=str(int(self.time[0])%12)+':'+self.time[1]+' PM'
        else:
            self.time=self.time[0]+':'+self.time[1]+ ' AM' + ' , ' + self.time[2] + ' sec'
try:
    #global file
    file1=open("univlogv2.dat",'rb')
    file1.close()
    file1=open("univlogv2.dat",'ab')
except IOError:
    file1=open("univlogv2.dat",'ab')


while True :
    print('------------------------------------------------------------------------------------------------------------')
    choice=int(input("\n\n\nTo encrypt enter 1, to decrypt enter 2 , to view log enter 3 , to quit enter any other number :"))
    if choice==1 :
        print('Please Ensure That the password file is smaller than input file for encryption')
        try:
            enc_file=info_protect(input('\n Enter the path name of file :'),'Enc')
            enc_file.process()
            pickle.dump(enc_file.path,file1)
            pickle.dump(enc_file.passfile,file1)
            pickle.dump(enc_file.mode,file1)
            pickle.dump(enc_file.date,file1)
            pickle.dump(enc_file.time,file1)
            
        except IOError :
            print('\nPlease enter a valid path name next time!!!')
            
        else:
            print("\nFile Successfully Encrypted!!")
            
    elif choice==2 :
        try:
            dec_file=info_protect(input('\n Enter the path name of file :'),'Dec')
            dec_file.process()
            pickle.dump(dec_file.path,file1)
            pickle.dump(dec_file.passfile,file1)
            pickle.dump(dec_file.mode,file1)
            pickle.dump(dec_file.date,file1)
            pickle.dump(dec_file.time,file1)
        except IOError :
            print('\nPlease enter a valid path name next time!!!')
            
        else:
            print("\nFile Successfully Decrypted!!")
            
    elif choice==3 :
        try:
           file1.close()
           file1=open("univlogv2.dat",'rb')
           a=1
           while True :
                   
                   print('========================Entry %d=========================='%(a))
                   print('\nFile path     :'+' '+pickle.load(file1))
                   print('\nPassfile path :'+' '+pickle.load(file1))
                   print('\nProcess       :'+' '+pickle.load(file1)+'ryption')
                   print('\nDate          :'+' '+pickle.load(file1))
                   print('\nTime          :'+' '+pickle.load(file1))
                   print()
                   print('==========================================================')
                   a+=1
        except EOFError :
           if a==1:
               print("No Records found")
           else:            
               print("\nThat's it---------")
    else :
        print("\nThanks for using me!!!!!!!!!")
        break
        
        
                                   











                                   
        
