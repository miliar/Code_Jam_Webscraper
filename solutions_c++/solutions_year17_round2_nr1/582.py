#include <bits/stdc++.h>
using namespace std;

#define debug(args...) fprintf (stderr, args)

typedef long double LD;
typedef pair <LD, LD> pii;

LD d;
int n;

vector <pii> p;

bool ok (LD v)
{
	LD X = 0;
	LD Y = v;

	LD speed = 1e18;

	for (int i = 0; i < n; ++i)
	{
		LD x = p[i].first;
		LD y = p[i].second;

		speed = min (speed, y);

		if (speed == Y)
			continue;

		LD T = (X - x) / (speed - Y);

		if (T <= 0)
			continue;

		if (v * T <= d)
			return false;
	}

	return true;
}

int main ()
{
	freopen ("output.txt", "w", stdout);

	cin.sync_with_stdio (false);
	cin.tie (0);
	cout.tie (0);

	int T;
	cin >> T;

	int test = 0;

	while (T--)
	{
		cin >> d >> n;

		p.clear();

		for (int i = 0; i < n; ++i)
		{
			LD x, y;
			cin >> x >> y;
			p.push_back (pii (x, y));
		}

		sort (p.begin(), p.end());
		p.push_back (pii (d, 0.0));

		LD ini = 0;
		LD fim = 1e18;

		for (int k = 0; k < 200; ++k)
		{
			LD mid = (ini + fim) / 2.0;

			if (ok (mid))
				ini = mid;
			else
				fim = mid;
		}

		cout << "Case #" << ++test << ": ";
		cout << fixed << setprecision (15) << ini << '\n';

	}

	return 0;
}