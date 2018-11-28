#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define int64 long long int
using namespace std;

string S;
int ans[30];

bool tryy (int ix, bool eq, int prv)
{
	if (ix == S.size ()) return true;
	if (!eq) {
		ans[ix] = 9;
		return tryy (ix + 1, eq, 9);
	}
	for (int i = 9; i >= 0; i--) {
		if ((eq && (i > (S[ix] - '0'))) or (i < prv)) continue;
		if (eq && (i == (S[ix] - '0'))) {
			ans[ix] = i;
			if (tryy (ix + 1, true, i))
				return true;
			continue;
		}
		ans[ix] = i;
		if (tryy (ix + 1, false, i))
			return true;
	}
	return false;
}
void solve (int T)
{
	cin >> S;
	tryy (0, true, 0);
	printf ("Case #%d: ", T);
	int ix = 0;
	while (ans[ix] == 0) ix++;
	for (int i = ix; i < S.size (); i++) printf ("%d", ans[i]);
	puts ("");
}
int main ()
{
	int t;
	scanf ("%d", &t);
	for (int i = 1; i <= t; i++) solve (i);
	return 0;
}
