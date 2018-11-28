#include <bits/stdc++.h>
using namespace std;

#define ll long long

int main()
{
  ll t;
  cin>>t;

  ll p =1;
  while(t--)
  {
    ll count = 0;
    string s;
    ll k;
    cin>>s>>k;

    ll n = s.size();
    for(ll i=0;i<=(n-k);i++)
    {
      if(s[i]=='-'){
        count++;
      for(ll j=i;j<i+k;j++)
      {
          if(s[j]=='+')
            s[j]='-';
          else
            s[j]='+';
      }
    }
    }

    ll flag=0;
    for(ll i=0;i<n;i++)
    {
      if(s[i]=='-')
      {
        flag=1;
        break;
      }
    }

    cout<<"Case #"<<p<<": ";
    p++;
    if(flag==0)
    cout<<count<<endl;
    else
      cout<<"IMPOSSIBLE"<<endl;
  }
}
