        #include <fstream>
        #include <iostream>
        #include <string>
        #include <stdio.h>
        
        using namespace std;
        
        int main()
        {
            ofstream fout ("2015gcj3out.txt");
            ifstream fin ("2015gcj3in.txt");
            
            int t;
            long long n;
            long long k;
            long long aux;
            int p;
            long long twop;
            long long max;
            long long min;
          
                        
            fin >> t;
           
            for(int i=0; i<t; i++)
            {
            
            fin >> n;
            fin >> k;
            
            aux = k;
            twop = 1;
            
            for(p=0; aux>0 ;p++)
            {
            aux = aux/2;
            twop = 2*twop;
            }
            
            twop = twop/2;
            
            aux = (n-k)/(twop);
            
            max = (aux+1)/2;
            min = aux/2;
            
            //fout << aux << endl;
            fout << "Case #" << i+1 << ": " << max << " " << min << endl;
            
            } 
            return 0;
            
        }
        
        

