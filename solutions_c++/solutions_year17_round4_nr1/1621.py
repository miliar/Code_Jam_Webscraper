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
#define pi 3.1415926535

#define MOD (1000000007)
using namespace std;
int rem[5];
int proc(int a,int b,int c)
{
    int ans=0;
    if(a<0 || b<0 || c<0)
        return -1000;
    if(a==0 && b==0 && c==0)
        return 0;
    
    ans=max(ans,proc(a-4,b,c));
    ans=max(ans,proc(a,b-2,c));
    ans=max(ans,proc(a,b,c-4));
    ans=max(ans,proc(a-1,b,c-1));
    ans=max(ans,proc(a-2,b-1,c));
    ans=max(ans,proc(a,b-1,c-2));
    
    if(a+b+c!=0)
        ans=max(1,ans);
    return ans;
}
int main(void)
{
    ifstream infile;
    infile.open("in.txt");
    
    ofstream outfile;
    outfile.open("out.txt");
    int t,n,p,g,ans,cc=1;
    infile>>t;
    while(t--)
    {
        infile>>n>>p;
        ans=0;
        for(int i=0;i<5;i++)
            rem[i]=0;
        for(int i=0;i<n;i++)
        {
            infile>>g;
            rem[g%p]++;
        }
        if(p==2)
        {
            ans=rem[0] + rem[1]/2 +(rem[1]%2==1?1:0);
        }
        else if(p==3)
        {
            ans=rem[0];
            if(rem[1]<=rem[2])
            {
                ans+=rem[1];
                rem[2]-=rem[1];
                ans+=rem[2]/3;
                if(rem[2]%3!=0)
                    ans++;
            }
            else{
                ans+=rem[2];
                rem[1]-=rem[2];
                ans+=rem[1]/3;
                if(rem[1]%3!=0)
                    ans++;
            }
        }
        else
        {
            ans=rem[0]+proc(rem[1],rem[2],rem[3]);
        }
        printf("Case #%d: %d\n",cc,ans);
        outfile<<"Case #"<<cc++<<": "<<ans<<endl;
    }
    outfile.close();
    infile.close();
    return 0;
}
