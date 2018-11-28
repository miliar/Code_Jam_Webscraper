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
string s;

bool read()
{
	if (scanf("%s", buff) != 1)
		return false;

	s = string(buff);
	return true;
}

bool good(string s)
{
	for (int i = 1; i < size(s); ++i)
		if (s[i] < s[i - 1])
			return false;

	return true;
}

void improve(string& s)
{
	reverse(s.begin(), s.end());
	for (; size(s) > 1 && s.back() == '0'; s.pop_back());
	reverse(s.begin(), s.end());
}

void solve()
{
	++cs;
	printf("Case #%d: ", cs);

	if (good(s))
	{
		printf("%s\n", s.c_str());
		return ;
	}

	string ans;

	for (int i = size(s) - 2; i >= 0; --i)
	{
		string t = s;
		
		if (t[i] >= '1')
		{
			--t[i];

			for (int j = i + 1; j < size(t); ++j)
				t[j] = '9';
		}

		if (good(t))
		{
			improve(t);

			if (ans.empty() || (size(t) > size(ans) || (size(t) == size(ans) && t > ans)))
				ans = t;
		}
	}

	printf("%s\n", ans.c_str());
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
