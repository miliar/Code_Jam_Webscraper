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

ll stupid(ll x)
{
	for (ll y = x; y >= 1; y--)
	{
		ll cy = y;
		int prev = 9;
		int cur = cy % 10;
		bool flag = true;
		int i = 0;
		while (i < 21)
		{
			if (prev < cur)
			{
				flag = false;
				break;
			}
			cy /= 10;
			prev = cur;
			cur = cy % 10;
			i++;
		}
		if (flag)
			return y;
	}
}

ll my_solve(ll x)
{
	vector < int > t;
	ll cx = x;
	while (cx > 0)
	{
		t.push_back(cx % 10);
		cx /= 10;
	}

	reverse(t.begin(), t.end());

	int pos = -1;
	for (int i = 0; i < t.size() - 1; i++)
		if (t[i] > t[i + 1])
		{
			pos = i;
			t[i]--;
			break;
		}
	if (pos == -1)
		return x;

	int j = 0;
	for (int i = pos; i > 0; i--)
	{
		if (t[i] < t[i - 1])
		{
			t[i - 1]--;
			j--;
		}
		else
			break;
	}
	pos += j;

	ll ans = 0;
	for (int i = 0; i <= pos; i++)
	{
		ans += t[i];
		ans *= 10;
	}
	for (int i = pos + 1; i < t.size(); i++)
	{
		ans += 9;
		if (i != t.size() - 1)
			ans *= 10;
	}
	return ans;
}

int main()
{
#ifdef XXX
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		ll x;
		cin >> x;

		ll res1 = my_solve(x);
		cout << "Case #" << i + 1 << ": " << res1 << "\n";
	}

	return 0;
}