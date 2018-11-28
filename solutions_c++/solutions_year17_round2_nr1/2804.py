#include <bits/stdc++.h>
#include <stdio.h>
using namespace std;

int main()
{
	freopen("hu.in","r",stdin);
  freopen("out.txt","w",stdout);
  int t;
  cin>>t;
  for (int i = 1; i <= t; ++i)
  {
	  double d;
	  int n;
	  cin>>d>>n;
	  double mi=0.0;
	  for (int j = 0; j < n; ++j)
	  {
	  	double pos,speed;
		cin>>pos>>speed;
		double xxx=(d-pos)/speed;
		mi=max(mi,xxx);
	  }
	 // cout<<mi<<endl;
	  double ans=d/mi;
	  cout<<"Case #"<<i<<": ";
	  cout<<setprecision(10)<<ans; cout<<endl;
  }
}
