#include <bits/stdc++.h>
using namespace std;

int count_letters(string s) {
    int c = 0;
    for (auto el: s) {
        if (el != '?') {++c;};        
    }
    return c;
}



int main(int argc, char **argv)
{
    
    //freopen("..\\sample-in.in", "r", stdin);
    //freopen("..\\input.in", "r", stdin);
    //freopen("..\\output.out", "w", stdout);
    
    int T; cin >> T;
    
    for(int t=0; t<T; ++t){
        
        int R,C; cin >> R >> C;
        
        vector <string> cake (R);
        for (int r=0; r<R; ++r) {
            cin >> cake[r];
        }
                

        /*
        char letter = '?';
        //char last = '?';
        
        bool l = true;
        int gap_r, gap_c;
        
        for (int gap=0; gap < R && l; ++gap) {
            for (int i = 0; i < gap && l ; ++i) {
                if (cake[gap][i]!='?') {
                    l = false;
                    letter = cake[gap][i];
                    gap_r = gap;
                    gap_c = i;
                } else if (cake[i][gap]!='?') {
                    l = false;
                    letter = cake[i][gap];
                    gap_r = i;
                    gap_c = gap;
                } 
            }
            
            if (l && cake[gap][gap]!='?') {
                l = false;
                letter = cake[gap][gap];
                gap_c = gap;
                gap_r = gap;                
            }             
        }
        */
                  
        
        for (int i=0; i<R; ++i) {            
            if (count_letters (cake[i])) {
                if (count_letters (cake[i]) < C) {
                    
                    char prev = '?';
                    for (int pos=0; pos < C; ++pos) {

                        if (cake[i][pos]=='?')  
                            {cake[i][pos]=prev;}
                        else prev = cake[i][pos];
                    }
                    
                     prev = '?';
                    for (int pos=C-1; pos>=0; --pos) {
                        if (cake[i][pos]=='?')  cake[i][pos]=prev;
                        else prev = cake[i][pos];
                    } 
                     
                }
            }
        }

        
        for (int i=0; i<C; ++i) {            

            char prev = '?';
            for (int pos=0; pos < R; ++pos) {

                if (cake[pos][i]=='?')  
                    {cake[pos][i]=prev;}
                else prev = cake[pos][i];
            }
            
             prev = '?';
            for (int pos=R-1; pos>=0; --pos) {
                if (cake[pos][i]=='?')  cake[pos][i]=prev;
                else prev = cake[pos][i];
            } 
             

        }
        
        
        printf("Case #%d: \n", t+1);  
        
        //printf("%d %d: \n", gap_r, gap_c); 
    
        for (int r=0; r<R; ++r) {
            cout << cake[r] << endl;
        }       
        
    }

	return 0;
}
