#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t,n,i = 1;
	double d,k,s,time;
	cin>>t;
	while(t--)
	{
		time = 0;
		cin>>d>>n;
		while(n--)
		{
			cin>>k>>s;
			if((d-k)/s > time)
				time = (d-k)/s;
		}
		cout<<"Case #"<<i++<<": "<<setprecision(6)<<fixed<<d/time<<endl;
	}
	
	return 0;
}
