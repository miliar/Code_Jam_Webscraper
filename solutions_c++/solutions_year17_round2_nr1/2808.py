#include <bits/stdc++.h>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	
	int t, T;
	int N, i;
	long double D, slowest = -1, K, S, curr;
	
	cin>>T;
	
	for(t = 1; t <= T; t++)
	{	
		cin>>D>>N;
		slowest = -1;
		
		for(i = 0; i < N; i++)
		{
			cin>>K>>S;
			
			curr = (D - K) / S;
			
			if(curr > slowest)
				slowest = curr;
		}
		cout<<"Case #"<<t<<": "<<fixed<<setprecision(6)<<(D / slowest)<<endl;
	}
	
	return 0;
}
