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

int custs[1000];
int seats[1000];
int custseats[1000];
int seatcounts[1000];

int main(void)
{
    int ttt=0;
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
        
        double ans=0.0;
        int i,j,k;
        
        int n,c,m;
        
        fin >> n >> c >> m;
        memset(custseats,0,sizeof(custseats));
        memset(seatcounts,0,sizeof(seatcounts));
        
        for(k=0; k<m; k++)
        {
            fin >> i >> j;
            i--;
            j--;
            seats[k]=i;
            custs[k]=j;
            custseats[custs[k]]++;
            seatcounts[seats[k]]++;
            
        }
        
        int ret1=0;
        for(i=0; i<c; i++)
        {
            if(custseats[i]>ret1)
                ret1=custseats[i];
        }
        k =0;
        for(j=0; j<n; j++)
        {
            k+=seatcounts[j];
            while(ret1*(j+1)<k)
                ret1++;
        }
        int ret2=0;
        for(j=0; j<n; j++)
        {
            if(seatcounts[j]>ret1)
                ret2+=seatcounts[j]-ret1;
        }
        
        
        cout << "Case #" << ct << ": ";
        fout << "Case #" << ct << ": ";
        
        
        cout << ret1 << " " << ret2;
        fout << ret1 << " " << ret2;
        
        
        
        
        
        fout << endl;
        cout << endl;
        
    }
    
    
    return 0;
}

