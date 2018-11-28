#include<bits/stdc++.h>
#include<iomanip>

using namespace std;
int main()
{
	int T;
	cin>>T;
	
	for(int i=1;i<=T;i++)
	{
		unsigned long long int D;
		int N;
		cin>>D>>N;
		long double t=0.0;long double tmax=0.0;
		unsigned long long int K,S;
		for(int j = 1;j<=N;j++)
		{
			cin>>K>>S;
			t = (D - K)/((long double)S*1.0);
			if(t>tmax) 
				tmax = t;	
			//cout<<tmax<<"\n";		
		}
		cout<<"Case #"<<i<<": "<<setprecision(10)<<((long double)D/(tmax*1.0))<<"\n";
	}
}
