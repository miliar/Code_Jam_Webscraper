        #include <fstream>
        #include <iostream>
        #include <string>
        #include <stdio.h>
        #include <math.h>
        #include <limits>
        
        
        using namespace std;
        
        
        int main()
        {
            ofstream fout ("2017gcj1out.txt");
            ifstream fin ("2017gcj1in.txt");
            
            int t;
            int k;
            string signs;
            
            int s;
            int res;
            int aux;
          
            fin >> t;      
            
            for(int i=0; i<t; i++)
            {
            
            fin >> signs;
            fin >> k;
            res =0;
            aux = 0;
                       
            s = signs.length();
            
            for(int j=0; j<s-k+1; j++)
            {
                    if( signs[j] == '-')
                    {
                        res++;
                        for(int r=0; r<k; r++)
                        {
                                if( signs[j+r] == '-')
                                signs[j+r] = '+';
                                else
                                signs[j+r] = '-';
                        }
                    }
            }
            
            for(int j=s-k+1; j<s; j++)
            {
                    if( signs[j] == '-')
                    {
                       aux = 1;
                       break; 
                    }
            }
            
            
            if(aux == 0)
            fout << "Case #" << i+1 << ": " << res << endl;
            else
            fout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
            }
            
       
            
            return 0;
              
        }
        
        
