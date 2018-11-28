// wrong

#include <bits/stdc++.h>

#define forn(i, n) for (llong i = 0ll; i < (llong) n; ++i)
#define fornn(i, l, r) for (llong i = (llong) l; i < (llong) r; ++i)
#define size(x) ((int) (x.size()))

using namespace std;

typedef long long llong;
const llong inf = (llong) 1e+9 + 7ll;
const llong linf = (llong) 1e+18 + 7ll;
const long double eps = (long double) 1e-10;
const long double pi = acosl((long double) -1.0);
const int alph = 26;

static char buff[(int) 2e6 + 17]; // reads std::string
const int maxn = (int) 1e6 + 17;

int d, n, cs;
int p[maxn], v[maxn];

bool read()
{
	if (scanf("%d %d", &d, &n) != 2)
		return false;

	forn (i, n)
		scanf("%d %d", p + i, v + i);

	return true;
}

void solve()
{
	++cs;
	printf("Case #%d: ", cs);
	double t = 0;

	for (int i = 0; i < n; ++i)
		t = max(t, (double) (d - p[i]) / v[i]);

	printf("%.7f\n", (double) d / t);
}

void gen() { }
void naive() { }

int main()
{
#if SEREZHKA
	freopen("file.in", "r", stdin);
	freopen("file.out", "w", stdout);
#endif
	//srand(time(nullptr));
	int T;
	scanf("%d", &T);

	if (1)
	{
		while (read())
			solve();
	}
	else
	{
		for (;;)
		{
			gen();
			solve();
			naive();
		}
	}

	return 0;
}
