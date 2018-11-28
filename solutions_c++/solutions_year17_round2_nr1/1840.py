        #include <fstream>
        #include <iostream>
        #include <string>
        #include <stdio.h>
        #include <math.h>
        #include <limits>
        #include <iomanip>

        
        
        using namespace std;
        
        
        int main()
        {
            ofstream fout ("1out.txt");
            ifstream fin ("1in.txt");
            
            int t;
            int d;
            int n;
            int k;
            int s;
            double res;
            double aux1;
            double aux2;
            double aux3;
            
            
            fin >> t;
            //fout << t << endl;    
            
            for(int i=0; i<t; i++)
            {
            fin >> d;
            fin >> n;
            // fout << d << endl;
            //fout << endl;
            res = 0;
            
            for(int j=0;j<n;j++)
            {
            fin >> k;
            fin >> s;
            //fout << k << endl;
            //fout << s << endl;
            aux1 = (double)(d);
            aux2 = (double)(d-k);
            aux2 = aux2/s;
            //fout << aux1 << endl;
            //fout << aux2 << endl;
            aux3 = aux1/aux2;
            if( j==0 || res > aux3)
            {
            res = aux3;
            //fout << "result " << res << endl;
            }
            }
            
            
                   
            fout << "Case #" << i+1 << ": ";
            fout << setprecision(10) << res << endl;
            }
            return 0;
              
        }
        
        
