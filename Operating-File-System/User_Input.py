import File_Structure

class take_input():
    
    def __init__(self):
        self.create_cmd=0 #to know file is created or not
        self.open_cmd=0   #to know file is open or not which helps when we have to close file
        self.basics()
        
    def basics(self):
        while 1:
            di= input("Do you want to create file system? (y/n)\nPress 'Q' to quit\n")
            if di.lower()=='y':
                print("creating New disk space")
                self.commands()
                #break
            elif di.lower()=='n':
                print("Using existing file system")
                disk.get_from_file()
                self.commands()
                #break
            elif di.lower()=='q':
                break
            else:
                print("Please enter valid option")

                
    def commands(self):
        print("Entered command")
        a=input("1 : Execute commands\n2 : Test commands\n")
        print("a",type(a))
        if a == '1':
            print("Enter following commands:\n\tCREATE type name\n\tOPEN mode name\n\tCLOSE\n\tDELETE name\n\tREAD n\n\tWRITE n data\n\tSEEK base offset ")
        elif a== '2':
            print("automated testcase")
            disk.command()
            #automation
        else:
            print("Default mode 'Execute command' is selected")
        while 1:
            cmd=input("$  ")   
            d=cmd.split(' ')
            cmd_len=len(d)
            if cmd_len == 0:
                print("Please enter command")
            if cmd_len == 1:
                for i in d:
                    init=i
                if init.upper() == 'QUIT' or init.upper() == 'EXIT' or init.upper() == 'Q':
                    a=input("Do you want save before exit?(y/n)? ")
                    if a.upper() == 'Y':
                        self.initial_cmd('save')
                        break
                    elif a.upper() == 'N':
                        break
                        
                self.initial_cmd(init)
            if cmd_len == 2:
                init,x=d
                self.initial_cmd(init,x)
            if cmd_len >= 3:
                if cmd_len>3:
                    y=' '.join(d[2:])
                    d=d[:2]
                    init,x=d
                else:
                    init,x,y=d
                #print(init,x,y)
                self.initial_cmd(init,x,y)
            
    def initial_cmd(self,init,x=0,y=0):
        
        if init.upper()== 'CREATE':
            if '-' not in x:
                print("Enter valid commands\n\tCREATE -d/-u name")
                return
            self.create_cmd=1
            if not x and not y:
                print("Enter Valid command\n\tCREATE -d/-u name")
                return
            x=x[1:]
            #print(x.upper(),y)
            if x.upper() != 'U' and x.upper() !='D':
                print("Enter valid command")
                return
            if x.upper() == 'U' and '.' not in y:
                print("Enter proper filename")
                return
            self.state='create'
            #print("Inside CREATE")
            disk.create(x,y)
            return
        
        elif init.upper()=='OPEN':
            if '-' not in x:
                print("Enter valid commands\n\t\tOPEN -i/-u/-o filename")
                return
            x=x[1:]
            self.open_cmd=1
            if x.upper() !='I' and x.upper() != 'U' and x.upper() != 'O':
                print("please enter valid open type")
                return
            
            disk.opens(x,y)
            return
        
        elif init.upper()== 'CLOSE':
            self.create_cmd=0;self.open_cmd=0
            disk.close()
            return
        
        elif init.upper()=='DELETE':
            disk.delete(x)
            return
        
        elif init.upper()== 'READ':
            disk.read(x)
            return
        
        elif init.upper() == 'FREE':
            print(disk.free_space_list)
            return
        
        elif init.upper()=='WRITE':
            if not y:
                print("Enter valid command\n\tWRITE n data")
                return
            if self.create_cmd or self.open_cmd:
                disk.write(x,y)
            else:
                print("open a file before write")
                return
            return
        
        # show the structure of file system
        elif init.upper() == 'LS':
            disk.ls()
            return
        
        # show the block structures
        elif init.upper() == 'BLOCK':
            if x:
                disk.print_block(int(x)+1)
            else:
                disk.print_block()
            return

        # show the content of the file
        elif init.upper() == "CAT":
            if not x:
                print("Enter filename")
                return
            disk.cat(x)
            return
        
        elif init.upper()== 'SEEK':
            if not x and not y:
                print("Enter Valid command\SEEK base offset")
                return
            disk.seeks(x,y)
            return
        elif init.upper() == 'SAVE':
            disk.write_to_file()
            
        elif init.upper() == 'HELP':
            if x:
                if x.upper() == "OPEN":
                    print("\tOPEN mode name \n\t mode = (I)\t'INPUT'  : Read and Seek\t (or)")
                    print("\t\t(U)\t'UPDATE' : Read,Write (rewrite), Seek\t\t(or)\n\t\t(O)\t'OUTPUT' : Write(padding) ")
                
                if x.upper() == "SEEK":
                    print("\tSEEK base offset")
                    print("\t\t base= -1 , poiting to Begining of file")
                    print("\t\t\t0, Pointing to current position ")
                    print("\t\t\t +1, Pointing to End of file position")
                    print("\t Example: 'SEEK -1 0' is a rewind\n\t\t'SEEK +1 0' is equivalent to a position to end of 	file")
                    print("\t\t 'SEEK 0 -5' positions the file pointer backward by five bytes")
            else:
                print("\tCREATE type name\n\tOPEN mode name\n\tCLOSE\n\tDELETE name\n\tREAD n\n\tWRITE n data\n\tSEEK base offset")
            return
        else:
            print("Enter valid commands")
        
 
disk = File_Structure.FileSpace()       
getInput = take_input()   
