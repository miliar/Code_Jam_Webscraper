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
//#define max(a,b) ((a)>(b)?:(a):(b))
using namespace std;
vector<int>ans;
set<int> v;
int x,o;
int solve(int n)
{
    if(x!=-1)
        v.insert(x);
    if(o!=-1)
        v.insert(o);
    
    if(x!=-1)
    {  ans.pb(0);ans.pb(1);ans.pb(x); o=x;}//o
    if(x==-1 && o==-1)
    {
        v.insert(n);
        ans.pb(0);ans.pb(1);ans.pb(n);
        o=n;
    }
    for(int c=1;c<=n;c++)
    {
        if(v.find(c)==v.end())
        { ans.pb(1);ans.pb(1);ans.pb(c);}
    }
    for(int c=2;c<n;c++)
    {
        ans.pb(1);//+
        ans.pb(n);
        ans.pb(c);
    }
    int r=2,c=o-1;
    while(r<=n && c>=1)
    {
        ans.pb(2);//x
        ans.pb(r);
        ans.pb(c);
        r++;
        c--;
    }
    r=n,c=n;
    while(r>1 && c>o)
    {
        ans.pb(2);ans.pb(r);ans.pb(c);
        r--;c--;
    }
    return (n+1)+max(0,n-2)+max(0,n-1);
        
    
}
int main(void)
{
    ifstream infile;
    infile.open("in.txt");
    
    ofstream outfile;
    outfile.open("out.txt");
    
    int t,cc=1,n,m,r,c,sco;
    string ch,str;
    infile>>t;
    while(t--)
    {
        infile>>n>>m;
        v.clear();
        ans.clear();
        x=-1;o=-1;
        for(int i=0;i<m;i++)
        {
            infile>>ch>>r>>c;
            if(ch[0]=='+')
                v.insert(c);
            else if(ch[0]=='x')
                x=c;
            else
               o=c;
        }
        sco=solve(n);
        outfile<<"Case #"<<cc++<<": "<<sco<<" "<<ans.size()/3<<endl;
        for(int i=0;i<ans.size();i+=3)
        {
            if(ans[i]==0)
                str="o";
            else if(ans[i]==1)
                str="+";
            else
                str="x";
            outfile<<str<<" "<<ans[i+1]<<" "<<ans[i+2]<<endl;
        }
    }
    outfile.close();
    infile.close();

    return 0;
}