#include<bits/stdc++.h>

using namespace std;

int prob[1000];

int main()
{
	int T;
	cin>>T;
	
	int N,K;
	double u;
	int U;
	for(int tc=1;tc<=T;tc++)
	{
		cin>>N>>K;
		cin>>u;
		U = u*10000 + 1e-9;;
		priority_queue<int, vector<int>, greater<int> > pq;
		for(int i=0;i<N;i++)
		{
			double x;
			cin >> x;
			prob[i] = x*10000 + 1e-9;
			pq.push(prob[i]);
		}
		
		while(U--)
		{
			int z = pq.top(); pq.pop();
			pq.push(z+1);
		}
		double ans = 1;
		while(!pq.empty())
		{
			int z = pq.top(); pq.pop();
			double dz = z;
			dz = dz/10000;
			ans = ans * dz;
		}
		printf("Case #%d: %.6lf\n", tc,ans);
	}
	
	return 0;
}
