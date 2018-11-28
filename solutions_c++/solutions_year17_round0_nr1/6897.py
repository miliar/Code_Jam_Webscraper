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
	int _t;
	cin >> _t;

	for(int t=1; t<=_t; t++)
	{
		string S;
		cin >> S;

		int k;
		cin >> k;

		vector <int> A;

		for(char s: S)
			A.pb(1 * (s == '-'));

		int n = S.size();
		int ans = 0;

		for(int i=0; i <= (n-k); i++)
			if(A[i]) 
			{
				for(int j=0; j < k; j++)
					A[i + j] ^= 1;

				ans++;
			}

		int sum = 0;
		for(int i=0; i<n; i++)
			sum += A[i];

		printf("Case #%d: ", t);
		if(sum)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << ans << endl;
	}

	return (0-0);	
}