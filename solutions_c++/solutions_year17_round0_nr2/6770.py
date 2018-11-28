#include<iostream>
#include<math.h>
#include<string.h>
#include<map>
#include<vector>
#include<queue>
#include<stack>
#define pb push_back
#define inf 9999999999
#define ll long long
#define ld long double
#define mod 1000000007
#include<limits.h>
#include<algorithm>
#include<cstdio>
using namespace std;


int main()
{
    std::ios::sync_with_stdio(false);
   freopen("B-large.in","r",stdin);
   freopen("out.txt","w",stdout);
    ll tc;
    cin>>tc;
    for(ll c=1;c<=tc;c++)
    {
       string s;
       ll j;
       bool flag;
       cin>>s;
       while(1)
       {
           flag=true;
           for(ll i=1;i<s.size();i++)
       {
           ll x=s[i]-'0';
           ll y=s[i-1]-'0';

           if(x<y)
           {
              y=y-1;
              flag=false;
              s[i-1]=y+'0';
              j=i;
              while(j<s.size())
              {
                  s[j]='9';
                  j++;
              }
           }
       }
       if(flag)break;
       }
       cout<<"Case #"<<c<<":"<<' ';
       for(ll i=0;i<s.size();i++)if(s[i]!='0')cout<<s[i];
       cout<<endl;



    }

    return 0;
}
