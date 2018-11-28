#include <bits/stdc++.h>
#define rep(i,x) for(int i=0;i<x;i++)
using namespace std;
int main()
{
int n;
cin>>n;
for(int i=1;i<=n;i++)
{
  int count=0;
  string s;
  cin>>s;
  int n1=s.length();
  int k;
  cin>>k;
  int p=n1-k+1;
//  cout<<p<<endl;

  rep(i,n1)
  {
    if(s[i]=='-'&& i<p)
    {
      count++;
    //  cout<<"hhgj"<<endl;
      for(int j=i;j<i+k;j++)
      {
        if(s[j]=='-')s[j]='+';
        else
        s[j]='-';
      }
    }
  }
  int chek=0;
  rep(i,n1)
  {
    if(s[i]=='-')
  { chek=1;
    break;
  }
  }
  if(chek==1)
  {
  cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
  }
  else
  cout<<"Case #"<<i<<": "<<count<<endl;
}
}
