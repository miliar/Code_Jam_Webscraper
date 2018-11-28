/*
	  /\ 
	 /  \ 
	.∧＿＿∧ 
	( ･ω･｡)つ━☆・*。 
	⊂　 ノ 　　　・゜+. 
	しーＪ　　　°。+ *´¨) 
	　　　　　　　　　.· ´¸.·*´¨) ¸.·*¨) 
	　　　　　　　　　　(¸.·´ (¸.·'* ☆  вжух
*/

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
const int maxn = (int) 5e2 + 17;

int n, k, cs;
string s;

bool read()
{
	if (scanf("%s", buff) != 1)
		return false;

	s = string(buff);
	scanf("%d", &k);
	return true;
}

void solve()
{
	n = size(s);
	int ans = 0;
	++cs;

	for (int i = 0; i + k <= n; ++i)
		if (s[i] == '-')
		{
			++ans;

			for (int j = i; j < i + k; ++j)
				s[j] = (s[j] == '+') ? '-' : '+';
		}

	if (count(s.begin(), s.end(), '-') == 0)
		printf("Case #%d: %d\n", cs, ans);
	else
		printf("Case #%d: IMPOSSIBLE\n", cs);
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
