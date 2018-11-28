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
	int t, tc, i, j, k, n;
	cin >> t;
	tc = 0;
	while (t--) {
		cout << "Case #" << ++tc << ": ";
		cin >> str;
		n = str.size();
		for (k = 0; k < 18; ++k) {
			for (i = 0; i < n-1; ++i) {
				if (str[i] > str[i+1]) {
					str[i] -= 1;
					for (j = i+1; j < n; ++j) {
						str[j] = '9';
					}
					break;
				}
			}
		}
		i = 0;
		if (str[i] == '0') i++;
		for (; i < n; ++i) {
			putchar(str[i]);
		}
		puts("");
	}

	return 0;
}
