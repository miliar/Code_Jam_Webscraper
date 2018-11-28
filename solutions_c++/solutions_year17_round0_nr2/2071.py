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
vector<int> v;
int check(int ind)
{
  int flag=0,i;
  for(i=ind;i<v.size()-1;i++)
  {
    if(v[i]>v[i+1])
      flag=1;      
  }
  if(flag==1)
    return 0;
  else
    return 1;
}
int main()
{
  barn;
  //freopen("inputf.in","r",stdin);
  //freopen("outputf.in","w",stdout);
  int k,t;
  cin>>t;
  for(k=1;k<=t;k++)
  {
     ll n;
     int len=0,i,j;
     cin>>n;
     v.clear();
     if(n==1)
      cout<<"Case #"<<k<<": "<<n<<"\n";
     else
     {
      while(n>0)
      {
        v.pb(n%10);
        n=n/10;
      }
      len=v.size();
      reverse(v.begin(),v.end());
      for(i=len-2;i>=0;i--)
      {
       if(v[i]>v[i+1])
       {
          if(v[i]!=0)
          {
             v[i]--;
             for(j=i+1;j<len;j++)
              v[j]=9;
          }
       }
      }
      cout<<"Case #"<<k<<": ";
      i=0;
      if(v[i]==0)
        i++;  
      for(;i<len;i++)
      {
         cout<<v[i];
      }    
      cout<<"\n";
    }

  }
  return 0;
}