#include <bits/stdc++.h>

using namespace std;

#define MOD 1000000007
#define ll long long int
#define ld long double
#define pb push_back
#define mkp make_pair
#define pii pair<int, int> 
#define pll pair<long long int, long long int>
#define sci(x) scanf("%d", &x)
#define scl(x) scanf("%lld", &x)

string str;

int main()
{
	int k, t, i, j, n, c, tc;
	tc = 0;
	cin >> t;
	while (t--) {
		cout << "Case #" << ++tc << ": ";
		c = 0;
		cin >> str >> k;
		n = str.size();
		for (i = 0; i <= n-k; ++i) {
			if (str[i] == '-') {
				c++;
				for (j = 0; j < k; ++j) {
					if (str[i+j] == '-') str[i+j] = '+';
					else str[i+j] = '-';
				}
			}
		}
		j = 1;
		for (i = 0; i < n; ++i) {
			if (str[i] == '-') j = 0;
		}
		if (j == 1) {
			cout << c << endl;
		} else {
			cout << "IMPOSSIBLE" << endl;
		}
	}

	return 0;
}
