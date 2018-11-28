#include<iostream>
#include<math.h>
#include<string.h>
#include<map>
#include<vector>
#include<queue>
#include<stack>
#define pb push_back
#define inf 9999999999
#define ll int
#define ld long double
#define mod 1000000007
#include<limits.h>
#include<algorithm>
#include<cstdio>
using namespace std;


int main()
{
    std::ios::sync_with_stdio(false);
    freopen("A-large (1).in","r",stdin);
    freopen("out.txt","w",stdout);
    ll tc;
    cin>>tc;
    for(ll c=1;c<=tc;c++)
    {
       string s;
       ll k;
       bool flag=true;
       cin>>s>>k;
       ll ans=0;
       for(ll i=0;i<s.size();i++)
       {
           if(s[i]=='-' && i+k<=s.size())
           {
               ans++;
               for(ll j=i;j<i+k;j++)
               {
                   if(s[j]=='-')s[j]='+';
                   else if(s[j]=='+')s[j]='-';
               }
           }
       }
       for(ll i=0;i<s.size();i++)
       {
           if(s[i]=='-'){flag=false;break;}
       }
       if(flag)cout<<"Case #"<<c<<":"<<' '<<ans<<endl;
       else cout<<"Case #"<<c<<":"<<' '<<"IMPOSSIBLE"<<endl;


    }

    return 0;
}
