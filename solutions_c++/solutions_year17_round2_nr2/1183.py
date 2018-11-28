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

int cs, n, R, O, Y, G, B, V;

bool read()
{
	if (scanf("%d %d %d %d %d %d %d", &n, &R, &O, &Y, &G, &B, &V) != 7)
		return false;

	return true;
}

bool correct(string& s)
{
	if (R != 0 || B != 0 || Y != 0)
		return false;

	for (int i = 0; i < n; ++i)
		if (s[i] == s[(i + 1) % n])
			return false;

	return true;
}

void solve()
{
	++cs;
	printf("Case #%d: ", cs);

	if (O + G + V != 0)
	{
		printf("\n");
		return ;
	}

	if (n == 1)
	{
		if (R == 0) printf("R\n");
		if (Y == 0) printf("Y\n");
		if (B == 0) printf("B\n");
		return ;
	}

	if (max({R, Y, B}) * 2 > n)
	{
		printf("IMPOSSIBLE\n");
		return ;
	}

	string s;

	if (max({R, Y, B}) == R)
	{
		string t;

		for (; R > 0 || Y > 0; )
			if (Y == 0 || size(t) % 2 == 0)
				t.push_back('R'), --R;
			else
				t.push_back('Y'), --Y;

		for (int i = 0; i < n; ++i)
			if (i % 2 == 0 && B > 0)
				s.push_back('B'), --B;
			else
				s.push_back(t.back()), t.pop_back();
	}
	else
	{
		if (max({R, Y, B}) == B)
		{
			string t;

			for (; B > 0 || Y > 0; )
				if (Y == 0 || size(t) % 2 == 0)
					t.push_back('B'), --B;
				else
					t.push_back('Y'), --Y;

			for (int i = 0; i < n; ++i)
				if (i % 2 == 0 && R > 0)
					s.push_back('R'), --R;
				else
					s.push_back(t.back()), t.pop_back();
		}
		else if (max({R, Y, B}) == Y)
		{
			string t;

			for (; Y > 0 || R > 0; )
				if (R == 0 || size(t) % 2 == 0)
					t.push_back('Y'), --Y;
				else
					t.push_back('R'), --R;

			for (int i = 0; i < n; ++i)
				if (i % 2 == 0 && B > 0)
					s.push_back('B'), --B;
				else
					s.push_back(t.back()), t.pop_back();
		}
	}

	printf("%s\n", s.c_str());
}

void gen() { }
void naive() { }

int main()
{
#if SEREZHKA
	freopen("file.in", "r", stdin);
	freopen("file.out", "w", stdout);
#endif
	srand(time(nullptr));
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
