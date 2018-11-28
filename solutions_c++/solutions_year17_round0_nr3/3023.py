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

long long n, k;

map <long long, long long> mapa;
map <long long, long long>::iterator it;

int main()
{
	int t;
	scanf("%d", &t);
	for (int tt=1; tt<=t; tt++)
	{
		printf("Case #%d: ", tt);
		scanf("%lld%lld", &n, &k);
		k--;
		mapa.clear();
		mapa[n]=1;
		while(k)
		{
			it=mapa.end();
			it--;
			long long w=it->first;
			long long x=min(mapa[w], k);
			mapa[w]-=x;
			k-=x;
			if (!mapa[w])
				mapa.erase(w);
			w--;
			mapa[w/2]+=x;
			mapa[(w+1)/2]+=x;
		}
		it=mapa.end();
		it--;
		long long w=it->first;
		w--;
		printf("%lld %lld\n", (w+1)/2, w/2);
	}
	return 0;
}
