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
char gr[30][30];
int main(void)
{
    ifstream infile;
    infile.open("in.txt");
    
    ofstream outfile;
    outfile.open("out.txt");
    
    int t,n,m,tmp,pre,cc=1;
    string s;
    char ch;
    infile >> t;
    cout<<t<<endl;
    while(t--)
    {
        infile>>n>>m;
        cout<<n<<" "<<m<<endl;
        for(int i=0;i<n;i++)
        {
            infile>>s;
            for(int j=0;j<m;j++)
            gr[i][j]=s[j];
            
        }
        
        for(int i=0;i<n;i++)
        {  for(int j=0;j<m;j++)
            if(gr[i][j]!='?')
            {
                for(int t=0;t<j;t++)
                    if(gr[i][t]=='?')
                        gr[i][t]=gr[i][j];
                for(int t=j+1;t<m && gr[i][t]=='?';t++)
                    gr[i][t]=gr[i][j];
            }
        }
        
        for(int i=0;i<n;i++)
        {
            if(gr[i][0]=='?')
            {
                tmp=i+1;
                while(tmp<n && gr[tmp][0]=='?')
                    tmp++;
                if(tmp<n)
                {
                    for(int j=0;j<m;j++)
                        gr[i][j]=gr[tmp][j];
                    continue;
                }
                tmp=i-1;
                while(tmp>=0 && gr[tmp][0]=='?')
                    tmp--;
                assert(tmp>=0);
                for(int j=0;j<m;j++)
                    gr[i][j]=gr[tmp][j];
            }
        }
        
        outfile<<"Case #"<<cc++<<": "<<endl;
        for(int i=0;i<n;i++)
        { for(int j=0;j<m;j++)
            outfile<<gr[i][j];
            outfile<<endl;
        }

        
    }
    outfile.close();
    infile.close();
}