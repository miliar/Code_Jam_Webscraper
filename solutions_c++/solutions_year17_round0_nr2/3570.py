        #include <fstream>
        #include <iostream>
        #include <string>
        #include <stdio.h>
        #include <math.h>
        
        
        
        using namespace std;
        
        int main()
        {
            ofstream fout ("2015gcj2out.txt");
            ifstream fin ("2015gcj2in.txt");
            
            
            int t;
            
            string num;
            int s;
            int pos1;
            int pos2;
            
            
            fin >> t;
                      
                      
            for(int i=0; i<t; i++)
            {
            fin >> num;
            pos1 = -1;
            pos2 = -1;
            s = num.length();
            int digit[s];
            
            for(int j=0; j<s;j++)
            digit[j] = num[j]-'0';
            
            
            
            for(int j =1; j<s; j++)
            if( digit[j] < digit[j-1])
            {
            pos1 = j;
            break;            
            }
            
            for(int j=pos1-1; j>=0; j--)
            if(digit[j] > digit[j-1])
            {
            pos2 = j;
            }
            //fout << pos1 << "    " << pos2 << endl;
            fout << "Case #" << i+1 << ": ";
            
            if(pos1 == -1)
            fout << num;
            else
            {
            if(pos2 == -1)
            {
            if(digit[0] > 1)
            fout << digit[0]-1;
            
            for(int j=1; j<s; j++)
            fout << "9";
            }
            else
            {
            for(int j=0; j<pos2; j++)
            fout << digit[j];
            
            fout << digit[pos2]-1;
            
            for(int j=pos2+1; j<s; j++)
            fout << "9";
            }
            }                 
        
      
            
           
            
    
            
            fout << endl;
            }            
                                   
            
            return 0;
            
        }
        
        
