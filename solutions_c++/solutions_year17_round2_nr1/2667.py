#include <bits/stdc++.h>

using namespace std;

bool cmp(pair<int ,int> a, pair<int ,int> b)
{
	return a.first > b.first;
}
int main()
{

	int T;
	cin >> T;
	for(int t = 1; t <= T; t++)
	{
		cout << "Case #"<<t<<": ";
		int D,N,a,b;
		cin >> D >>N;
		pair<int,int> K[1001]; //1 initial position, maximum speed
		for(int i = 0; i < N; i++){
			cin >> a >> b;
			K[i] = {a,b};
			
		}
		sort(K, K+N, cmp);
		double ti = 0;
		for(int i = 0; i < N; i++)
			ti = max(ti, 1.0*(D-K[i].first)/K[i].second);
		
		cout << fixed<<setprecision(10)<<1.0*D/ti<<endl;


		
	}

	return 0;
}