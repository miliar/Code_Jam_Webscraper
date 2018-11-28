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

int cs;
llong n, k;

bool read()
{
	if (scanf("%lld %lld", &n, &k) != 2)
		return false;

	return true;
}

void solve()
{
	++cs;
	printf("Case #%d: ", cs);

	multiset<llong> ls;
	ls.insert(n);

	for (int i = 0; i < k - 1; ++i)
	{
		llong cur = *ls.rbegin();
		ls.erase(ls.find(cur));
		if (cur >= 3) ls.insert((cur - 1) / 2);
		if (cur >= 2) ls.insert(cur - 1 - (cur - 1) / 2);
	}

	llong cur = *ls.rbegin();
	printf("%lld %lld\n", cur / 2, (cur - 1) / 2);
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
