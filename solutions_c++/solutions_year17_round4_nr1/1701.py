#include <bits/stdc++.h>
using namespace std;

#define debug(args...) fprintf (stderr, args)

const int maxn = 1e2 + 10;

int t, n, p, g[maxn];

int solve ()
{
	if (p == 2)
	{
		int odd = 0;
		int even = 0;

		for (int i = 1; i <= n; ++i)
			if (g[i] % 2 == 0)
				++even;
			else
				++odd;

		return even + ((odd + 1)/ 2);
	}

	if (p == 3)
	{
		int mod[3];

		for (int i = 0; i <= 2; ++i)
			mod[i] = 0;

		for (int i = 1; i <= n; ++i)
			++mod[g[i] % 3];

		int ans = mod[0];

		int menor = min (mod[1], mod[2]);

		ans += menor;

		mod[1] -= menor;
		mod[2] -= menor;

		ans += (mod[1] / 3) + (mod[2] / 3);

		mod[1] %= 3;
		mod[2] %= 3;

		if (mod[1] || mod[2])
			++ans;

		return ans;
	}
}

int main ()
{
	//fprintf (stdin, "r", "in.txt");
	freopen ("out.txt", "w", stdout);

	scanf ("%d", &t);

	int test = 0;

	while (t--)
	{
		scanf ("%d %d", &n, &p);

		for (int i = 1; i <= n; ++i)
			scanf ("%d", &g[i]);

		printf ("Case #%d: %d\n", ++test, solve());
	}

	return 0;
}