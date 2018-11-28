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
        int m;
        
        int n;
        int i,j,k;
        
        fin >> s >> m;
        
        n =s.size()+2;
        
        for(i=0; i<s.size(); i++)
        {
            if(s[i]=='+')
                isok[i+1]=true;
            else
                isok[i+1]=false;
        }
        isok[0]=isok[n-1]=true;
        
        int ret = 0;
        bool cando=true;
        
        for(i=1;i+m<n; i++)
        {
            if(isok[i]!=isok[i-1])
            {
                ret++;
                for(j=0; j<m; j++)
                    isok[i+j]=!isok[i+j];
            }
            if(!isok[i])
                cando=false;
        }
        while(i<n)
        {
            if(!isok[i])
                cando=false;
            i++;
        }
        
        if(!cando)
        {
        
        cout << "IMPOSSIBLE";
        fout << "IMPOSSIBLE";
       
        }
        else{
            cout << ret;
            fout << ret;
        }
        
        
        fout << endl;
        cout << endl;
        
    }
    
    
    return 0;
}

