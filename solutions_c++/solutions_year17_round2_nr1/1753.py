#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define int64 long long int
#define unit64 unsigned long long int

const int MM = 1e3 + 5;
int64 X[MM], S[MM];
int64 D, N;

bool check (long double v)
{
	long double t = D/(long double) (v);

	for (int i = 0; i < N; i++) {
		long double tt = (D - X[i])/(long double) (S[i]);
		if (t + 1e-10 < tt) return false;
	}
	return true;
}
void solve (int T)
{
	scanf ("%lld %lld", &D, &N);
	for (int i = 0; i < N; i++) {
		scanf ("%lld %lld", &X[i], &S[i]);
	}
	long double ans = 0.0;
	long double l = 0.0, r = 1e18;
	for (int i = 0; i < 400; i++) {
		long double m = (l + r)/2;
		if (check (m)) {
			ans = m;
			l = m;
		} else r = m;
	}
	printf ("Case #%d: %.10LF\n", T, ans);
}
int main ()
{
	int t;
	scanf ("%d", &t);
	for (int i = 1; i <= t; i++) solve (i);
	return 0;
}
