#include <bits/stdc++.h>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	int t, T, N, K, n, i;
	vector<pair<long double, long double> > P;
	vector<long double> H;
	long double surf_area, side_area, r, h, ans;
	
	cin>>T;
	
	for(t = 1; t <= T; t++)
	{
		cin>>N>>K;
		//cout<<"TEST : "<<N<<' '<<K<<endl;
		ans = 0;
		P.resize(N);
		
		for(i = 0; i < N; i++)
		{
			cin>>P[i].first>>P[i].second;
			surf_area = P[i].first * P[i].first * M_PI;
			side_area =  M_PI * (2.00 * P[i].first * P[i].second);
			
			P[i].first = surf_area;
			P[i].second = side_area;
		}
		
		sort(P.rbegin(), P.rend());
		
		for(i = 0; i <= (N - K); i++)
		{
			surf_area = P[i].first;
			side_area = P[i].second;
			
			H.resize(N - i - 1);
			
			int j = 0;
			for(n = i + 1; n < N; n++)
			{
				H[j++] = P[n].second;
			}
				
			sort(H.rbegin(), H.rend());
			
			
			for(n = 0; n < K - 1; n++)
			{
				side_area += H[n];
			}
			
			ans = max(ans, (side_area + surf_area));
		}
		
		cout<<"Case #"<<t<<": "<<fixed<<setprecision(9)<<ans<<endl;
	}
	
	return 0;
}
