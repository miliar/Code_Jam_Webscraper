#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007
int main()
{
	ios::sync_with_stdio(0);
	int T;
	cin>>T;
	for (int t = 1; t <= T; ++t)
	{
		long long D, N;
		cin>>D>>N;
		long long k[N], s[N];
		long double minspeed = DBL_MIN;
		for (int i = 0; i < N; ++i)
		{
			cin>>k[i]>>s[i];
			long double x = D - k[i];
			x /= s[i];
			minspeed = max(x, minspeed);
		}

		long double ans = D;
		ans /= minspeed;
		cout<<"Case #"<<t<<": "<<fixed<<setprecision(6)<<ans<<'\n';
	}
}