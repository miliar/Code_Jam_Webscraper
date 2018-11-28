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

const int nax=107;

int n, p;

int ile[nax];
int dp[nax][nax][nax][nax];

vector <int> co;

int &daj(vector <int> wek)
{
	while((int)wek.size()<4)
		wek.push_back(0);
	return dp[wek[0]][wek[1]][wek[2]][wek[3]];
}

int czy_ok(const vector <int> &wek)
{
	int r=0;
	for (int i=0; i<wek.size(); i++)
		r+=i*wek[i];
	r%=p;
	return (!r);
}

void check()
{
	daj(co)=-nax;
	int nook=0;
	for (int i=0; i<p; i++)
	{
		if (co[i])
		{
			vector <int> now=co;
			now[i]--;
			nook=1;
			daj(co)=max(daj(co), daj(now)+czy_ok(now));
		}
	}
	if (!nook)
		daj(co)=0;
}

void rek(int v)
{
	if (v==p)
	{
		check();
		return;
	}
	for (int i=0; i<=ile[v]; i++)
	{
		co.push_back(i);
		rek(v+1);
		co.pop_back();
	}
}

void test_case(int t)
{
	debug() << "test " << t;
	scanf("%d%d", &n, &p);
	for (int i=0; i<p; i++)
		ile[i]=0;
	for (int i=1; i<=n; i++)
	{
		int x;
		scanf("%d", &x);
		ile[x%p]++;
	}
	rek(0);
	vector <int> zrob;
	for (int i=0; i<p; i++)
		zrob.push_back(ile[i]);
	printf("Case #%d: %d\n", t, daj(zrob));
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int tt=1; tt<=t; tt++)
		test_case(tt);
	return 0;
}
