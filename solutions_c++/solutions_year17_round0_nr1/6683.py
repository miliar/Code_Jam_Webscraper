#include <bits/stdc++.h>
using namespace std;
#define ll long long





int main() {
    freopen("jammul.in", "r", stdin);
  freopen("jammul.out", "w", stdout);
    ll tt;
    cin>>tt;
     for (ll qq=1;qq<=tt;qq++)
 {

     string str;int k;
     cin>>str>>k;
    ll desc=0,cnt=0;
     for(ll i=0;i<str.length();i++)
     {
         if(str[i]=='-')
          {
              if(i+k<=str.length())
              {

         cnt++;
         for(int j=i;j<i+k;j++)
         {
             if(str[j]=='-')
             str[j]='+';
             else str[j]='-';

         }
              }
     }
     }
     //cout<<str<<" ";
      for(int i=0;i<str.length();i++)
     {
              if(str[i]=='+')
             desc++;
     }
cout<<"Case #"<<qq<<":"<<" ";
if(desc==str.length())
cout<<cnt;
else cout<<"IMPOSSIBLE";
cout<<"\n";
 }
  return 0;
}

