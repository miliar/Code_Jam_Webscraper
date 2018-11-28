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


/*
 * Careful of stack overflow if N is much bigger than 5k
 */

bool adj[222][222];
bool done[222];
int origins[222];
int nn;

bool bpm(int x)
{
    if(done[x])
        return false;
    done[x]=true;
    for(int i=0; i<nn; i++)
    {
        if(adj[x][i])
        {
            if(origins[i]==-1)
            {
                origins[i]=x;
                return true;
            }
            else if(bpm(origins[i]))
            {
                origins[i]=x;
                return true;
                
            }
        }
    }
    return false;
}

int runBPM(int _n)
{
    nn=_n;
    int ans = 0;
    memset(origins,-1,sizeof(origins));
    for(int i=0; i<nn; i++)
    {
        memset(done,0,sizeof(done));
        if(bpm(i))
            ans++;
    }
    return ans;
}

void makeadj(int n)
{
    memset(adj,0,sizeof(adj));
    int i,j;
    for(i=0; i<n; i++)
    {
        for(j=0; j<n; j++)
        {
            adj[i+j][i-j+n-1]=true;
        }
    }
}

void deladj(int a, int b, int n)
{
    for(int k=0; k<2*n-1; k++)
    {
        adj[a+b][k]=false;
        adj[k][a-b+n-1]=false;
    }
}


bool isdiag[100][100];
bool iscross[100][100];

bool crossx[100];
bool crossy[100];

bool newstate[100][100];

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
        
        
        
        int n,m;
        
        fin >> n >> m;
        
        int i,j,k;
        char c;
        
        memset(isdiag,0,sizeof(isdiag));
        memset(iscross,0,sizeof(iscross));
        memset(crossx,0,sizeof(crossx));
        memset(crossy,0,sizeof(crossy));
        memset(newstate,0,sizeof(newstate));
        int crosstot,diagtot;
        crosstot=diagtot=0;
        
        makeadj(n);
        
        for(k=0; k<m; k++)
        {
            fin >> c >> i >> j;
            i--;
            j--;
            if(c=='o' || c=='x')
            {
                iscross[i][j]=true;
                crossx[i]=true;
                crossy[j]=true;
                crosstot++;
            }
            if(c=='o' || c=='+')
            {
                isdiag[i][j]=true;
                diagtot++;
                deladj(i,j,n);
            }
        }
        
        while(crosstot < n)
        {
            i=0;
            while(crossx[i])
                i++;
            j=0;
            while(crossy[j])
                j++;
            iscross[i][j]=true;
            newstate[i][j]=true;
            crossx[i]=true;
            crossy[j]=true;
            crosstot++;
        }
        
        int extras = runBPM(2*n-1);
        
        for(k=0; k<2*n-1; k++)
        {
            if(origins[k]!=-1)
            {
                int a = origins[k]; //sum
                int b = k-n+1; //diff
                isdiag[(a+b)/2][(a-b)/2]=true;
                newstate[(a+b)/2][(a-b)/2]=true;
                
            }
        }
        
        int ret1 = extras+diagtot+crosstot;
        int ret2= 0;
        for(i=0; i<n; i++)
        {
            for(j=0; j<n; j++)
            {
                if(newstate[i][j])
                    ret2++;
            }
        }
        
        cout << "Case #" << ct << ": ";
        fout << "Case #" << ct << ": ";
        
        fout <<ret1 << " " << ret2 << endl;
        cout << ret1 << " " << ret2 << endl;

        
        for(i=0; i<n; i++)
        {
            for(j=0; j<n; j++)
            {
                if(newstate[i][j])
                {
                    if(isdiag[i][j] && iscross[i][j])
                        c = 'o';
                    else if(isdiag[i][j])
                        c='+';
                    else
                        c='x';
                    cout << c << " " << i+1 << " " <<  j+1 << endl;
                    fout << c << " " << i+1 << " " <<  j+1 << endl;

                    
                }
            }
        }
        
       
       
        
        
        
        
      
        
    }
    
    
    return 0;
}

