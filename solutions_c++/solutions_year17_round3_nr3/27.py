#include<bits/stdc++.h>
using namespace std;

typedef long double ld;
int n,k;
ld u,p[100],ans;

bool check(ld k)
{
  ld tmp=0;
  for(int i=0;i<n;i++)
    if(p[i]<k)
      tmp+=k-p[i];
  if(tmp>u) return false;
  return true;
}
  
int main()
{
  int qw;
  cin>>qw;
  for(int q=1;q<=qw;q++)
    {
      cin>>n>>k>>u;
      for(int i=0;i<n;i++)
	cin>>p[i];
      ld l=0,r=1;
      for(int i=0;i<1000;i++)
	{
	  ld mid=(l+r)/2;
	  if(check(mid))
	    l=mid;
	  else
	    r=mid;
	}
      ans=1;
      for(int i=0;i<n;i++)
	ans*=(p[i]<l?l:p[i]);
      cout<<"Case #"<<q<<": ";
      cout<<fixed<<setprecision(6)<<ans<<endl;
    }
}
