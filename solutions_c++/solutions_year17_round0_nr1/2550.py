#include <iostream>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <deque>
#include <string>

using namespace std;

#define pb push_back
#define mp make_pair
using ll = long long;
using pii = pair<int, int>;
using pll = pair<ll, ll>;

#define MAXS 1005

int T, K;
string s;

int main()
{
	int casenum = 1;
	cin >> T;
	while (T--)
	{
		int ans = 0;
		cin >> s >> K;
		for (int i = 0; i < s.length() - K + 1; ++i)
		{
			if (s[i] == '-')
			{
				ans++;
				for (int j = i; j < i + K; ++j) {
					if (s[j] == '+')
						s[j] = '-';
					else
						s[j] = '+';
				}
			}
		}
		int i;
		for (i = s.length() - K + 1; i < s.length(); ++i)
		{
			if (s[i] == '-')
				break;
		}
		if (i == s.length())
			cout << "Case #" << casenum << ": " << ans << endl;
		else
			cout << "Case #" << casenum << ": IMPOSSIBLE" << endl;
		casenum++;
	}
	return 0;
}