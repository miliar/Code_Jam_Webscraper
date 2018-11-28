#include<bits/stdc++.h>
using namespace std;
#define N 1005
#define pii pair<int,int>
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define ll long long 
#define mod 1000000007
#define barn cin.sync_with_stdio(0);cin.tie(0)
int main()
{
  barn;
  //freopen("inputf.in","r",stdin);
  //freopen("outputf.in","w",stdout);
  int k,t;
  string s;
  cin>>t;
  for(k=1;k<=t;k++)
  {
    int i,n,j,l,cnt=0,flag=0;
    cin>>s>>l;
    n=s.size();
    for(i=0;i<n;i++)
    {
      if(s[i]=='-')
      {
         if(i+l<=n)
         {
          for(j=i;j<i+l;j++)
          {
           if(s[j]=='-')
             s[j]='+';
           else
            s[j]='-';
          }
          cnt++;
         }
      }
    }
    for(i=0;i<n;i++)
    {
       if(s[i]=='-')
        flag=1;
    }
    if(flag==1)
      cout<<"Case #"<<k<<": IMPOSSIBLE\n";
    else
      cout<<"Case #"<<k<<": "<<cnt<<"\n";
  }
  return 0;
}