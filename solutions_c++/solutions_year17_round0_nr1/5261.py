#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <cmath>
#include <string>
#include <ctime>
#include <cassert>

using namespace std;

typedef long long ll;
typedef pair <int, int> ii;
typedef long double ld;
typedef pair<ld, ld> pld;

#define mp make_pair
#define mt(a, b, c) mp(a, mp(b, c))
#define ZERO(x) memset((x), 0, sizeof(x))


int main()
{
#ifdef XXX
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		string s;
		int k;
		cin >> s >> k;

		int ans = 0;
		for (int i = 0; i <= s.size() - k; i++)
		{
			if (s[i] == '-')
			{
				ans++;
				for (int j = 0; j < k; j++)
				{
					if (s[i + j] == '-')
						s[i + j] = '+';
					else
						s[i + j] = '-';
				}
			}
		}

		bool flag = true;
		for (int i = 0; i < s.size(); i++)
		{
			if (s[i] == '-')
			{
				flag = false;
				break;
			}
		}
		if (flag)
			cout << "Case #" << t + 1 << ": " << ans << "\n";
		else
			cout << "Case #" << t + 1 << ": IMPOSSIBLE\n";
	}

	return 0;
}