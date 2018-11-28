#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int tc=1;tc<=t;tc++)
	{
		int d,n;
		cin>>d>>n;
		double mx=0;
		while(n--)
		{
			int k,s;
			cin>>k>>s;
			mx=max(mx,(1.0*(d-k))/(1.0*s));
		}
		cout<<"Case #"<<tc<<": "; 
		cout<<fixed<<setprecision(6)<<(1.0*d)/mx<<endl;
	}
}