#include<stdio.h>
#include<bits/stdc++.h>
using namespace std;
#define ll long long
string s;
int main()
{
  ///freopen("A-large.in", "r", stdin);
  //freopen("a.out", "w", stdout);
  int t,i,n,fl,j,k,ans,m;
  scanf("%d",&t);
  for(i=1;i<=t;i++)
  {
    ans=0;
    cin>>s>>k;
    for(j=s.length()-1;j-k+1>=0;j--)
    {
      if(s[j]=='-')
      {
        ans++;
        for(m=0;m<k;m++)
        {
          if(s[j-m]=='-')
           s[j-m]='+';
          else
           s[j-m]='-';
        }
      }
    }
    for(j=0;j<s.length();j++)
     if(s[j]=='-')
      break;
    if(j<s.length())
     cout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
    else
     cout<<"Case #"<<i<<": "<<ans<<endl;
  }
  return 0;
}
