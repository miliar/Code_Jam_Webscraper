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

const int nax=24*60;

int n, m;

int zaj[nax+7][2];

int dp[nax+7][nax+7][2];

int wyn;

int main()
{
	int t;
	scanf("%d", &t);
	for (int tt=1; tt<=t; tt++)
	{
		debug() << tt;
		for (int i=0; i<=nax+3; i++)
			zaj[i][0]=zaj[i][1]=0;
		scanf("%d%d", &n, &m);
		for (int i=1; i<=n; i++)
		{
			int a, b;
			scanf("%d%d", &a, &b);
			for (int j=a+1; j<=b; j++)
				zaj[j][0]=1;
		}
		for (int i=1; i<=m; i++)
		{
			int a, b;
			scanf("%d%d", &a, &b);
			for (int j=a+1; j<=b; j++)
				zaj[j][1]=1;
		}
		wyn=nax+7;
		for (int h=0; h<2; h++)
		{
			for (int i=0; i<=nax+3; i++)
				for (int j=0; j<=nax+3; j++)
					dp[i][j][0]=dp[i][j][1]=nax+7;
			dp[0][0][h]=0;
			
			for (int i=0; i<=nax/2; i++)
				for (int j=0; j<=nax/2; j++)
					for (int l=0; l<2; l++)
						for (int d=0; d<2; d++)
							if (!zaj[i+j+1][d])
								dp[i+(d==0)][j+(d==1)][d]=min(dp[i+(d==0)][j+(d==1)][d], dp[i][j][l]+(d!=l));
			
			wyn=min(wyn, dp[nax/2][nax/2][h]);
			wyn=min(wyn, dp[nax/2][nax/2][h^1]+1);
		}
		printf("Case #%d: %d\n", tt, wyn);
	}
	return 0;
}
