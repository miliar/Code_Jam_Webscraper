#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

long long int d, n;
long long int k[1001], s[1001];

bool check(long double speed)
{
	for(int i = 0 ; i < n ;i++)
	{
		if(speed <= s[i])
		{
			continue;
		}

		long double meet = k[i] / (speed - s[i]);
		long double left = (long double)(d - k[i]) / s[i];

//		cout<<meet<<' '<<left<<'\n';
		if(meet < left)
		{
			return false;
		}
	}
	return true;
}

int main()
{
//	ios_base::sync_with_stdio(0);cin.tie(0);
//
	freopen("A-large.in", "r", stdin);
	freopen("output2.txt", "w", stdout);

	int t;
	cin>>t;

	for(int tc = 1 ; tc <= t; tc++)
	{
		cout<<"Case #"<<tc<<": ";

		cin>>d>>n;
		for(int i = 0 ; i < n ; i++)
		{
			cin>>k[i]>>s[i];	
		}

		long double left = 0;
		long double right = 123456789123456789123456789123456789.;
		long double answer;

		for(int i = 0 ; i < 100000; i++)
		{
			long double mid = (left + right) / 2.;	

			if(check(mid))
			{
				left = mid;
				answer = mid;	
			}
			else
			{
				right = mid;
			}
		}

		printf("%.6Lf\n", answer);
	}
		

	return 0;
}
