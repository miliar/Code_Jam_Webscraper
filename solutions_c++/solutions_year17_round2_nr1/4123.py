#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	int D,N;
	cin>>t;
	int c = 1;
	while(t--)
	{
		
		cin>>D>>N;
		vector< pair<double , double> > caballos;
		for(int i = 0 ; i < N; i++)
		{
			int a,b;
			cin>>a>>b;
			caballos.push_back( make_pair(a,b) );
		}
		double res = 0,T;
		if(N == 1)
		{
			T = (D -caballos[0].first) / caballos[0].second;
			res = D / T;
		}
		else
		{
			double t1,t2;
			sort(caballos.begin(), caballos.end());
			t1 = (D - caballos[0].first) / caballos[0].second;
			t2 = (D - caballos[1].first) / caballos[1].second;
			if(t1 < t2)
			{
				T = (D -caballos[1].first) / caballos[1].second;
				res = D / T;	
			}
			else
			{
				T = (D -caballos[0].first) / caballos[0].second;
				res = D / T;
			}
		}


		cout<<"Case #"<<c<<": "<<fixed<<setprecision(6)<<res<<'\n';
		c++;
	}
}