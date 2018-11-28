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
        
        long long n,k,i,j;
        
        long long lowv, lowcount, upv, upcount;
        
        fin >> n >> k;
        
        lowv=n;
        lowcount=1;
        upv=n+1;
        upcount=0;
        
        long long ret = -1;
        
        while(k>0)
        {
            if(k<=upcount)
            {
                ret=upv;
                k=0;
                break;
            }
            else if(k<=upcount+lowcount)
            {
                ret=lowv;
                k=0;
                break;
            }
            k-=(upcount+lowcount);
            
            if(lowv%2==1)
            {
                long long newlowv = (lowv-1)/2;
                long long newupv = (lowv+1)/2;
                long long newlowcount = 0;
                long long newupcount = 0;
                newlowcount+=lowcount*2;
                newlowcount+=upcount;
                newupcount+=upcount;
                
                lowv=newlowv;
                upv=newupv;
                lowcount=newlowcount;
                upcount=newupcount;
            }
            else
            {
                long long newlowv = (upv-3)/2;
                long long newupv = (upv-1)/2;
                long long newlowcount = 0;
                long long newupcount = 0;
                newlowcount+=lowcount;
                newupcount+=lowcount;
                newupcount+=upcount*2;
                
                lowv=newlowv;
                upv=newupv;
                lowcount=newlowcount;
                upcount=newupcount;
            }
        }
        
        long long mn = (ret-1)/2;
        long long mx = (ret-1-mn);
        
        
        cout << "Case #" << ct << ": ";
        fout << "Case #" << ct << ": ";
        
        
        cout << mx << " " << mn;
        fout << mx << " " << mn;
        
        
        fout << endl;
        cout << endl;
        
    }
    
    
    return 0;
}

