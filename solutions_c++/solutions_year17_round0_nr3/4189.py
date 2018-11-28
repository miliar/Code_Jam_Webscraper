#include <bits/stdc++.h>
using namespace std;

int T;

int n, k;

struct node
{
	int l, r;
	node (int l, int r) : l(l), r(r) {}
};

bool operator < (node A, node B)
{
	return ((A.r - A.l + 1) > (B.r - B.l + 1)) || ((A.r - A.l + 1) == (B.r - B.l + 1) && A.l < B.l);
}

set < node > Set;

int main ()
{
	ofstream cout ("out.txt");

	scanf ("%d", &T);

	int t = 0;
	while (T--)
	{
		scanf ("%d %d", &n, &k);

		if (n == k)
		{
			cout << "Case #" << ++t << ": 0 0\n";
			continue; 
		}

		Set.clear();
		Set.insert (node (1, n));

		int lastL, lastR;
		for (int K = 1; K <= k; ++K)
		{
			int l = Set.begin()->l;
			int r = Set.begin()->r;

			Set.erase (Set.begin());

			int mid = (l + r) / 2;
			lastL = (mid - 1 - l + 1);
			lastR = (r - (mid + 1) + 1);

			if (mid + 1 <= r)
				Set.insert (node (mid + 1, r));

			if (mid - 1 >= l)
				Set.insert (node (l, mid - 1));
		}

		cout << "Case #" << ++t << ": " << max (lastL, lastR) << " " << min (lastL, lastR )<< '\n';
	}

	return 0;
}