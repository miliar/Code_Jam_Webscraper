#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <cassert>
#define pb push_back
#define mk make_pair
#define F first
#define S second

#define MOD (1000000007)
using namespace std;
int r[3];
int a[3][10];
int N,M;
int gr[10][10];
int rng[10][10][2];
bool bpm( int u, bool seen[], int matchR[])
{
    for (int v = 0; v < N; v++)
    {
        if (gr[u][v] && !seen[v])
        {
            seen[v] = true;
            
            if (matchR[v] < 0 || bpm(matchR[v], seen, matchR))
            {
                matchR[v] = u;
                return true;
            }
        }
    }
    return false;
}

int maxBPM()
{
    int matchR[N];
    
    memset(matchR, -1, sizeof(matchR));
    
    int result = 0;
    for (int u = 0; u < M; u++)
    {
        bool seen[N];
        memset(seen, 0, sizeof(seen));
        
        if (bpm( u, seen, matchR))
            result++;
    }
    return result;
}
int main(void)
{
    ifstream infile;
    infile.open("in.txt");
    
    ofstream outfile;
    outfile.open("out.txt");
    
    int t,n,p,cc=1;
    string s;
    infile >> t;
    cout<<t<<endl;
    while(t--)
    {
        infile>>n>>p;
        for(int i=0;i<n;i++)
            infile>>r[i];
        for(int i=0;i<n;i++)
            for(int j=0;j<p;j++)
            { infile>>a[i][j];
                rng[i][j][0]=ceil ((double)a[i][j]/(1.1*r[i]));
                rng[i][j][1]=(int)((double)a[i][j]/(0.9*r[i]));
                cout<<rng[i][j][0]<<" "<<rng[i][j][1]<<endl;
                if(rng[i][j][0]>rng[i][j][1])
                {rng[i][j][0]=rng[i][j][1]=-1;}
            }
        if(n==1)
        {
            int cnt=0;
            for(int i=0;i<p;i++)
                if(rng[0][i][0]!=-1)
                    cnt++;
            outfile<<"Case #"<<cc++<<": "<<cnt<<endl;
            continue;
        }
        N=p;
        M=p;
        for(int i=0;i<p;i++)
            for(int j=0;j<p;j++)
                gr[i][j]=0;
        for(int i=0;i<p;i++)
            for(int j=0;j<p;j++)
            {
                if(rng[0][i][0]==-1 || rng[1][j][0]==-1)
                    continue;
                if(rng[0][i][0]<=rng[1][j][0] && rng[1][j][0]<=rng[0][i][1])
                    gr[i][j]=1;
                else if(rng[1][j][0]<=rng[0][i][0] && rng[0][i][0]<=rng[1][j][1])
                    gr[i][j]=1;
            }
        
        
        outfile<<"Case #"<<cc++<<": "<<maxBPM()<<endl;
        cout<<"next"<<endl;
        
        
    }
    outfile.close();
    infile.close();
}