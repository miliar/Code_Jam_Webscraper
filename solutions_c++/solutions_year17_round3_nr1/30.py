//PRZEMYSL ASSERTY

//SPRAWDZ CORNER CASE'Y, MINIMALNE I MAKSYMALNE WEJŚCIE I WYJŚCIE

//MODULO = 1

//while (clock()<=69*CLOCKS_PER_SEC)

#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace __gnu_pbds;
using namespace std;

template <typename T>
using ordered_set =
    tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;

#define sim template < class c
#define ris return * this
#define dor > debug & operator <<
#define eni(x) sim > typename \
  enable_if<sizeof dud<c>(0) x 1, debug&>::type operator<<(c i) {
sim > struct rge { c b, e; };
sim > rge<c> range(c i, c j) { return rge<c>{i, j}; }
sim > auto dud(c* x) -> decltype(cerr << *x, 0);
sim > char dud(...);
struct debug {
#ifdef LOCAL
~debug() { cerr << endl; }
eni(!=) cerr << boolalpha << i; ris; }
eni(==) ris << range(begin(i), end(i)); }
sim, class b dor(pair < b, c > d) {
  ris << "(" << d.first << ", " << d.second << ")";
}
sim dor(rge<c> d) {
  *this << "[";
  for (auto it = d.b; it != d.e; ++it)
    *this << ", " + 2 * (it == d.b) << *it;
  ris << "]";
}
#else
sim dor(const c&) { ris; }
#endif
};
#define imie(...) " [" << #__VA_ARGS__ ": " << (__VA_ARGS__) << "] "

#define shandom_ruffle random_shuffle

const int nax=1007;

int n, k;

pair <long long,long long> tab[nax];

double dp[nax][nax];
double wyn;

double obw(int v)
{
	return tab[v].first*tab[v].second*M_PI*2.0;
}

double pole(int v)
{
	return tab[v].first*tab[v].first*M_PI;
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int tt=1; tt<=t; tt++)
	{
		scanf("%d%d", &n, &k);
		for (int i=1; i<=n; i++)
			scanf("%lld%lld", &tab[i].first, &tab[i].second);
		sort(tab+1, tab+1+n);
		for (int i=0; i<=n; i++)
			for (int j=0; j<=n; j++)
				dp[i][j]=0.0;
		wyn=0.0;
		for (int i=0; i<n; i++)
		{
			for (int j=0; j<=i; j++)
			{
				dp[i+1][j]=max(dp[i+1][j], dp[i][j]);
				dp[i+1][j+1]=max(dp[i+1][j+1], dp[i][j]+obw(i+1));
			}
		}
		for (int i=1; i<=n; i++)
			wyn=max(wyn, dp[i-1][k-1]+obw(i)+pole(i));
		printf("Case #%d: %.9lf\n", tt, wyn);
	}
	return 0;
}
