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
map<ll,ll> mark;
vector<ll> v;
ll max(ll a,ll b)
{
  return (a>b?a:b);
}
ll min(ll a,ll b)
{
  return (a<b?a:b);
}
void solve(ll n)
{
  if(mark.find(n)!=mark.end())
  {
     return;
  }
  v.pb(n);
  mark[n]=1;
  if(n%2==1)
  {
    if(n/2>0)
     solve(n/2);
  }
  else
  {
    if(n/2-1>0)
     solve(n/2-1);
    if(n/2>0)
     solve(n/2);
  }
}
int main()
{
  barn;
  //freopen("inputf.in","r",stdin);
  //freopen("outputf.in","w",stdout);
  int j,t;
  cin>>t;
  for(j=1;j<=t;j++)
  {
   ll n,k;
   cin>>n>>k;
   mark.clear();
   v.clear();
   solve(n);
   ll i,l,r;
   sort(v.begin(),v.end());
   mark.clear();
   reverse(v.begin(),v.end());
   mark[v[0]]++;
   for(i=0;i<v.size();i++)
   {
      if(v[i]%2==1)
      {
          l=v[i]/2;
          mark[l]+=2*mark[v[i]];
      }
      else
      {
          l=v[i]/2-1;
          if(l>0)
            mark[l]+=mark[v[i]];
          r=v[i]/2;  
          mark[r]+=mark[v[i]];
      }
   }
   for(i=0;i<v.size();i++)
   {
     if(v[i]!=0)
     {
       if(k>mark[v[i]])
        k-=mark[v[i]];
       else
       {
        if(v[i]%2==0)
        {
           l=v[i]/2-1;
           r=v[i]/2;
        } 
        else
        {
           l=v[i]/2;
           r=v[i]/2;
        }
        cout<<"Case #"<<j<<": "<<max(l,r)<<" "<<min(l,r)<<"\n";
        break;
       }
     }
   }
 }
   return 0;
}