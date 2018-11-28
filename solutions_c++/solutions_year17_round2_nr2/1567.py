
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
string arr(int a,int b,int c,char aa,char bb,char cc,int n)
{
    int i=0;
    string s="";
    if(a>n/2)
        return "IMPOSSIBLE";
    for(int i=0;i<n;i++)
        s+='-';
    while(i<n && a>0)
    {
        s[i]=aa;
        i+=2;
        a--;
    }
    i-=1;
    while(i<n && b>0)
    {
        s[i]=bb;
        i+=2;
        b--;
       // cout<<i<<endl;
    }
   // cout<<s<<endl; cout<<n<<endl;
    for(int i=0;i<n;i++)
        if(s[i]=='-')
        {
            if(b)
            { s[i]=bb; b--;}
            else if(c)
            {
                s[i]=cc;c--;
            }
        }
    return s.substr(0,n);
        
}
int main(void)
{
    ifstream infile;
    infile.open("in.txt");
    
    ofstream outfile;
    outfile.open("out.txt");
    
    int cc=1;
    int t,n,r,o,y,b,g,v,i,tmp;
    infile>>t;
    string s="";
    while(t--)
    { infile>>n;
      infile>>r>>o>>y>>g>>b>>v;
     
        
        if(r>=y && y>=b)
            s=arr(r,y,b,'R','Y','B',n);
        else if(r>=b && b>=y)
          s=arr(r,b,y,'R','B','Y',n);
        else if(y>=r && r>=b)
            s=arr(y,r,b,'Y','R','B',n);
        else if(y>=b && b>=r)
            s=arr(y,b,r,'Y','B','R',n);
        else if(b>=r && r>=y)
            s=arr(b,r,y,'B','R','Y',n);
        else if(b>=y && y>=r)
            s=arr(b,y,r,'B','Y','R',n);
        
        //printf("%d %d %d %d %d %d\n",r,o,y,g,b,v);
        printf("Case #%d: ",cc);
        cout<<s<<endl;
     outfile<<"Case #"<<cc++<<": "<<s<<endl;
    }
    return 0;
}