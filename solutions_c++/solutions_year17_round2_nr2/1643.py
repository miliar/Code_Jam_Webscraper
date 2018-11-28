        #include <fstream>
        #include <iostream>
        #include <string>
        #include <stdio.h>
        #include <math.h>
        
        
        
        using namespace std;
        
        int main()
        {
            ofstream fout ("2out.txt");
            ifstream fin ("2in.txt");
            
            
            int t;
            int n;
            int col[6];
            char let[6];
            
            let[0]='R';
            let[1]='O';
            let[2]='Y';
            let[3]='G';
            let[4]='B';
            let[5]='V';
            
            
            fin >> t;
            
            int first;
            int current;
            int count;
            int aux;       
                      
            for(int i=0; i<t; i++)
            {
            fin >> n;
            
            for(int j=0;j<6;j++)
            {
            fin >> col[j];
            //fout << col[j] << endl;
            }
            
            if(n < 2*col[0] || n < 2*col[2] || n < 2*col[4])
            fout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
            else
            {
            fout << "Case #" << i+1 << ": ";
            first = 0;
            for(int j=0; j<6; j++)
            if( col[j] > col[first])
            first = j;
            
            fout << let[first];
            current = first;
            col[first]--;
            
            for(int count=n-1;count > 0;count--)
            {
            //fout << count << endl;
            aux = 0;
            
            if(current == 0)
            aux = 1;
            
            for(int j=0; j<6; j++)
            {
            if( j != current && col[j] > col[aux])
            aux = j;
            if( j != current && col[j] == col[aux] && j == first)
            aux = j;
            }
            
            fout << let[aux];
            current = aux;
            col[aux]--;
            }
            fout << endl;
            //fout << first << "  " << current << endl;
            }
            }            
                                   
            
            return 0;
            
        }
        
        
