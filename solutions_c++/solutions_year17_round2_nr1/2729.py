#include <bits/stdc++.h>
using namespace std;
int T,N; long long D;
double K;
double S;
int main()
{
	ifstream cin("A-large.in");
	ofstream cout("A-large.out");
	cin>>T;
	for(int cases=1; cases<=T; cases++)
	{
		cin>>D>>N;
		double time=0;
		for(int i=1; i<=N; i++)
		{
			cin>>K>>S;
			time=max(time,(D-K)/S);
		}
		double speed=D/time;
		cout<<"Case #"<<cases<<": "<<fixed<<setprecision(6)<<speed<<endl;
	}
	return 0;
}
