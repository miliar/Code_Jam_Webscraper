#include <bits/stdc++.h>

#define lli long long int
#define pb push_back
#define pii pair <int, int>
#define pll pair <lli, lli>
#define _F first
#define _S second
#define mset(x) memset(x, 0, sizeof(x))
#define fastio() ios_base::sync_with_stdio(0)

using namespace std;

int main()
{
	int T;
	cin >> T;

	for(int _t=1; _t<=T; _t++)
	{
		double d, n;
		cin >> d >> n;

		vector <double> K(n), S(n), T(n+1, 0);

		for(int i=0; i<n; i++)
			cin >> K[i] >> S[i];

		for(int i=n-1; i>=0; i--)
		{
			T[i] = (d - K[i]) / S[i];
			T[i] = max(T[i], T[i+1]);
		}


		double t = T[0];
		double s = d / t;

		printf("Case #%d: %0.9f\n", _t, s);
	}

	return (0-0);	
}