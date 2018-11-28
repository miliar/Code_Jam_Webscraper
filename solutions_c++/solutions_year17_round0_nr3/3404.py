/*input
5
4 2
5 2
6 2
1000 1000
1000 1
*/
#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define all(v) (v).begin(), (v).end()
#define uniq(v) (v).erase(unique(all(v)), v.end())
#define IOS ios::sync_with_stdio(0);
#define mt make_tuple

#define fr(a, b, c) for(int (a) = (b); (a) < (c); ++(a))
#define rp(a, b) fr(a,0,b)
#define cl(a, b) memset((a), (b), sizeof(a))
#define sc(a) scanf("%d", &a)
#define sc2(a, b) scanf("%d %d", &a, &b)
#define sc3(a, b, c) scanf("%d %d %d", &a, &b, &c)
#define pr(a) printf("%d\n", a);
#define pr2(a, b) printf("%d %d\n", a, b)
#define pr3(a, b, c) printf("%d %d %d\n", a, b, c)
#define IOS ios::sync_with_stdio(0);

typedef unsigned long long ull;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef pair<ll, ll> pll;

int main()
{
	ifstream in; in.open("cin.txt"); 
	ofstream out; out.open("cout.txt");
	int t;
	in >> t;
	fr(T, 0, t)
	{
		int n, k;
		in >> n >> k;
		//tuplas serao da forma <numero de elementos no intervalo, inicio, fim>  detalhe, inicio e fim nao estao no conjunto
		set<tuple<int, int, int> > intervals;
		intervals.insert(mt(n, 0, n+1));
		int mx, mn;
		fr(i, 0, k)
		{
			tuple<int, int, int> tp = *(intervals.rbegin());
			int tam = get<0>(tp);
			int ini = get<1>(tp);
			int end = get<2>(tp);
			int nxt = ini + ((end-ini)/2);
			intervals.insert(mt(nxt-ini-1, ini, nxt));
			intervals.insert(mt(end-nxt-1, nxt, end));
			intervals.erase(--intervals.end()); 
			if(i == k-1)
			{
				mx = end-nxt-1;
				mn = nxt-ini-1;
			}
		}
		if(mx < mn) swap(mx, mn);
		out << "Case #" << T+1 << ": " << mx << " " << mn << endl;

	}
	out.close();
	in.close();
	return 0;
}
