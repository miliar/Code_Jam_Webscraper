#include <bits/stdc++.h>
#define ll long long 
#define m 1000000007
using namespace std;

int main() {
	// your code goes here
	std::ios::sync_with_stdio(false);
	ll t,n,y=1;
	long double x,v,d,temp;
	cin>>t;
	while(t--)
	{
		cin>>d>>n;
		long double g=0;
		while(n--)
		{ 
			
			cin>>x>>v;
			 temp=(d-x)/v;
			 
			if(temp>g)
			g=temp;

		}
		cout<<"Case #"<<y<<": ";
		long double x=d/g;
		cout<<setprecision(8)<<x;
	//	printf("%0.6lf",x);
		cout<<endl;
		y++;
	}
	

	
	return 0;
}
