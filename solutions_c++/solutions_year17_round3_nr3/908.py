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

	for(int t=1; t<=T; t++)
	{
		int n, k;
		cin >> n >> k;

		double u, A[n+1];
		cin >> u;
		for(int i=0; i<n; i++)
			cin >> A[i];

		if(n == k)
		{
			while(u > 1e-6)
			{
				sort(A, A + n);

				double m = A[0];
				int x = 0;

				A[n] = A[n-1];
				while(A[x] == m) x++;

				x = min(x, n);

				if(x == n)
				{
					double g = u / ((double) n);
					for(int i=0; i<n; i++)
						A[i] += g;

					u = 0;
				}
				else
				{
					double needed = x * (A[x] - m);
					double avail = min(u, needed);

					double g = (avail) / ((double) x);
					for(int i=0; i<x; i++)
						A[i] += g;

					u -= avail; 
				}
			}

			double ans = 1;

			for(int i=0; i<n; i++)
				ans *= A[i];

			printf("Case #%d: ", t);
			cout << fixed << setprecision(10) << ans << endl;
		}
		else
			printf("Case #%d: 0.0\n", t);
	}

	return (0-0);	
}