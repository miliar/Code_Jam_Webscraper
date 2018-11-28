#include <vector>
#include <string>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <map>
#include <ctime>
#include <cassert>

using namespace std;

ofstream fout("../../../output.txt");
ifstream fin("../../../input.txt");

bool isok[1100];

int main(void)
{
    int ttt;
    fin >> ttt;
    int ct = 0;
    string s;
    
    cout.precision(9);
    fout.precision(9);
    
    cout << "HELLO" <<  " " << ttt << endl;
    
    
    
    while(ttt>0)
    {
        ct++;
        ttt--;
        
        cout << "Case #" << ct << ": ";
        fout << "Case #" << ct << ": ";
        
        
        string s;
        fin >> s;
        
        int n = s.size();
        int i,j,k;
        
        bool isok = true;
        bool isdone=false;
        k=-1;
        for(j=0; j+1<s.size(); j++)
        {
            if(s[j]>s[j+1])
            {
                isok=false;
                k=j;
                break;
            }
        }
        
        if(isok)
        {
            isdone=true;
            fout <<s;
            cout << s;
        }
        
        else{
            i=k;
            s[i]--;
            i--;
            while(i>=0 && s[i]>s[i+1])
            {
                s[i]--;
                i--;
            }
            i+=2;
            while(i<s.size())
            {
                s[i]='9';
                i++;
            }
            
            if(s[0]>'0')
            {
                cout << s[0];
                fout << s[0];
                
            }
            for(i=1; i<s.size(); i++)
            {
                cout << s[i];
                fout << s[i];
            }
            
        }
        
        
        fout << endl;
        cout << endl;
        
    }
    
    
    return 0;
}

