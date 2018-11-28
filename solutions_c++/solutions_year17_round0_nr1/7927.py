#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <list>
#include <utility>
#include <iterator>
#include <map>
#include <stack>
#include <queue>
#include <set>
#include <deque>
#include <bitset>

#define mod 1000000007
#define ima 1000000004
#define imi -1000000004
#define llma 1000000000000000004
#define llmi -1000000000000000004
#define lp(i,n) for(i=0;i<n;i++)
#define li(i,n) for(i=n-1;i>=0;i--)
#define tree vector<list<int > >
#define ll long long int
#define ld long double
#define f first

#define pa pair<ll,ll>
#define pad pair<double ,double>
#define pai pair<int,int>
#define mp make_pair
#define nn 100005
#define pi 3.1415926535898
#define inf 1e35
#define md 359999
#define it ::iterator
#define pb push_back
#define sync ios::sync_with_stdio(false);cout.tie(0);cin.tie(0);
using namespace std;


string s;
int main()
{ll t,i,an,coun,j,k,size;
    cin>>t;int l=1;
    for(l=1;l<=t;++l)
    {
        cin>>s;
        cin>>k;
        i=0;
        coun=0; size=0;
        
        size=s.length();
        
        for(i=0;i<=size-k;++i)
        {
            if(s[i]=='-')
            {
                for(j=i;j<i+k;j++)
                {
                    if(s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                }
                //	  cout<<s<<endl;
                ++coun;
            }
        }
        
        i=0; an=1;
        while(s[i]!='\0')
        {
            if(s[i]=='-')
                an=0;
            ++i;
        }
        if(an==0)
            cout<<"Case #"<<l<<": IMPOSSIBLE"<<endl;
        else
            cout<<"Case #"<<l<<": "<<coun<<endl;
    }}
