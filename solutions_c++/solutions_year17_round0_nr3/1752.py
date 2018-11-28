#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define int64 long long int
using namespace std;

map<int64, int64> A;
set <int64> Set;

void solve (int T)
{
	A.clear ();
	Set.clear ();
	int64 n, k, c = 0;
	scanf ("%lld %lld", &n, &k);
	A[n] = 1;
	Set.insert (n);
	c = 1;
	while (c < k) {
		int64 cur = *(Set.rbegin ());
		int64 xcount = A[cur];
		if (cur % 2 == 0) {
			if (c + xcount <= k) {
				Set.erase (cur);
				Set.insert (cur/2);
				Set.insert (cur/2 - 1);
				A[cur] = 0;
				A[cur/2] += xcount;
				A[cur/2 - 1] += xcount;
				c += xcount;
			} else goto out;
		} else {
			if (c + xcount <= k) {
				Set.erase (cur);
				Set.insert (cur/2);
				A[cur] = 0;
				A[cur/2] += 2 * xcount;
				c += xcount;
			} else goto out;
		}
	}
	out :;
	int64 mx = *(Set.rbegin ());
	int64 x = 0, y = 0;
	if (mx % 2) y = x = mx/2;
	else x = mx/2, y = x - 1;

	printf ("Case #%d: %lld %lld\n", T, x, y);
}
int main ()
{
	int t;
	scanf ("%d", &t);
	for (int i = 1; i <= t; i++) solve (i);
	return 0;
}
