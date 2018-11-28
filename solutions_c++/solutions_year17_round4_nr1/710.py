#include <bits/stdc++.h>
using namespace std;

#pragma GCC diagnostic warning "-Wconversion"

#define pb push_back
#define mp make_pair
#define eb emplace_back
#define all(a) begin(a), end(a)
#define has(a, b) (a.find(b) != a.end())
#define fora(i, n) for(int i = 0; i < n; i++)
#define forb(i, n) for(int i = 1; i <= n; i++)
#define forc(a, b) for(const auto &a : b)
#define ford(i, n) for(int i = n; i >= 0; i--)
#define maxval(t) numeric_limits<t>::max()
#define minval(t) numeric_limits<t>::min()
#define imin(a, b) a = min(a, b)
#define imax(a, b) a = max(a, b)

#define dbgs(x) #x << " = " << x
#define dbgs2(x, y) dbgs(x) << ", " << dbgs(y)
#define dbgs3(x, y, z) dbgs2(x, y) << ", " << dbgs(z)
#define dbgs4(w, x, y, z) dbgs3(w, x, y) << ", " << dbgs(z)

using ll = long long;

int mod[5];

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int T;
	cin >> T;

	forb(t, T)
	{
		int n, p;
		cin >> n >> p;

		fill(all(mod), 0);

		fora(i, n)
		{
			int g;
			cin >> g;
			mod[g % p]++;
		}

		ll res = mod[0];
		if (p == 2)
		{
			res += (mod[1] / 2) + (mod[1] % 2);
		}
		else if (p == 3)
		{
			res += min(mod[1], mod[2]);
			int diff = abs(mod[1] - mod[2]);
			res += (diff / 3);
			if (diff % 3 != 0)
				res++;
		}
		else if (p == 4)
		{
			res += (mod[2] / 2) + (mod[2] % 2);
			res += min(mod[1], mod[3]);
			int diff = abs(mod[1] - mod[3]);
			if (diff > 2)
			{
				diff -= 2;
				res += diff / 4;
				if (diff % 4 != 0)
					res++;
			}
		}

		cout << "Case #" << t << ": " << res << endl;
	}
}
