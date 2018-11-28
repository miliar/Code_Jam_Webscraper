#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007
int main()
{
	ios::sync_with_stdio(0);
	int T;
	cin>>T;
	int tc = 1;
	while (T--)
	{
		int N, K;
		cin>>N>>K;
		long double U;
		cin>>U;
		long double arr[N];
		for (int i = 0; i < N; ++i)
		{
			cin>>arr[i];
		}
		sort(arr, arr+N);
		for (int i = 0; i < N-1; ++i)
		{
			if (U == 0) break;
			if (U/(long double)(i+1) >= (arr[i+1] - arr[i]))
			{
				U -= (long double)(i+1)*(arr[i+1] - arr[i]);
				for (int j = 0; j <= i; ++j)
				{
					arr[j] = arr[i+1];
				}
			}
			else
			{
				for (int j = 0; j <= i; ++j)
				{
					arr[j] += (U / (long double)(i+1));
				}
				U = 0;
				break;
			}
		}
		if (U > 0)
		{
			for (int i = 0; i < N; ++i)
			{
				arr[i] += (U / (long double)N);
			}
		}
		long double ans = 1;
		for (int i = 0; i < N; ++i)
		{
			ans *= arr[i];
		}
		cout<<"Case #"<<tc++<<": "<<fixed<<setprecision(9)<<ans<<'\n';
	}	
}