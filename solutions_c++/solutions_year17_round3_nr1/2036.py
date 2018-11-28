
#include<iostream>
#include<iomanip>
#include<cstdio>
#include<utility>
#include<vector>
#include<queue>
#include<cmath>
#include<algorithm>
using namespace std;
#define pie 3.141592653589793
#define INF 999999999999
long double dp[1010][1010];
long double func(long long int index,vector<pair<long double,long double> > v,long long int howmany,long long int n,long long int k)
{
  //cout<<index<<" "<<howmany<<endl;
  std::cout <<std::fixed;
  std::cout.precision(10);
  if(howmany==k)
    return 0;
  if(index==n&&howmany<k)
    return -INF;
  long double ans=0;
  if(dp[index][howmany]==-1)
  {
  if(howmany!=k-1)
  ans=max(func(index+1,v,howmany,n,k),2*pie*v[index].first*v[index].second+func(index+1,v,howmany+1,n,k));
else
{
  ans=max(func(index+1,v,howmany,n,k),2*pie*v[index].first*v[index].second+pie*v[index].first*v[index].first+func(index+1,v,howmany+1,n,k));
}
dp[index][howmany]=ans;
}
return dp[index][howmany];

}
int main()
{
  long long int i,j,k,l,n,t,c=0;
  long double x,y,r,z;
std::cout <<std::fixed;
  std::cout.precision(10);
  scanf("%lld",&t);
  while(t--)
  {c++;
    scanf("%lld",&n);
    scanf("%lld",&k);
  
  pair<long double,long double> foo;
  vector<pair<long double,long double> > v;
  for(i=0;i<n;i++)
  {
    cin>>x>>y;
    foo=make_pair(x,y);
    v.push_back(foo);
  }
  sort(v.begin(),v.end());

long double ans;
for(i=0;i<=n;i++)
for(j=0;j<=k;j++)
  dp[i][j]=-1;
ans=func(0,v,0,n,k);
cout<<"Case #"<<c<<": ";
cout<<ans<<endl;


}





return 0;  
}