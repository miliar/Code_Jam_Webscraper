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

const int N=100000;
vector <int> implies[2*N]; //wymuszenia, 2*x to zmienna 2*x+1 to jej zaprzeczenie
int sat_val[2*N],sat_vis[2*N],sat_sort[2*N],sat_ile;

inline void sat_or(int a,int b)
{
    implies[a^1].push_back(b);
    implies[b^1].push_back(a);
}

void sat_dfs_mark(int x)
{
    sat_vis[x]=1;
    sat_val[x]=sat_val[x^1]==-1;
    for (int it=0; it<implies[x].size(); it++)
    if (!sat_vis[implies[x][it]])
    sat_dfs_mark(implies[x][it]);
}

void sat_dfs(int x)
{
    sat_vis[x]=1;
    for (int it=0; it<implies[x^1].size(); it++)
    if (!sat_vis[implies[x^1][it]^1])
    sat_dfs(implies[x^1][it]^1);
    sat_sort[sat_ile++]=x;
}

int sat2(int n)
{
    sat_ile=0;
    for (int i=0; i<2*n; i++)
    sat_vis[i]=0,sat_val[i]=-1;
    for (int i=0; i<2*n; i++)
    if (!sat_vis[i])
    sat_dfs(i);
    for (int i=0; i<2*n; i++)
    sat_vis[i]=0;
    for (int i=2*n-1; i>=0; i--)
    if (!sat_vis[sat_sort[i]])
    sat_dfs_mark(sat_sort[i]);
    for (int i=0; i<2*n; i++)
    if (sat_val[i])
    for (int it=0; it<implies[i].size(); it++)
    if (!sat_val[implies[i][it]])
    return 0;
    return 1;
}

const int nax=1007;

int n, m;

char wcz[nax][nax];
int num[nax][nax];

int l;
pair <int,int> tab[nax];

vector < pair <int,int> > zaw[nax][2];
vector < int > co_tu[nax][nax];

int zjeb[nax][2];

int nope;

int rx[]={-1, 0, 1, 0};
int ry[]={0, -1, 0, 1};

void dfs(int v, int u, int kier, vector < pair <int,int> > &zap)
{
	if (v<1 || v>n || u<1 || u>m || wcz[v][u]=='#')
		return;
	zap.push_back({v, u});
	if (wcz[v][u]=='-' || wcz[v][u]=='|')
		return;
	if (wcz[v][u]=='/')
		kier^=3;
	if (wcz[v][u]==92)
		kier^=1;
	dfs(v+rx[kier], u+ry[kier], kier, zap);
}

void test_case(int t)
{
	debug() << "test " << t;
	scanf("%d%d", &n, &m);
	nope=0;
	for (int i=1; i<=n; i++)
		scanf("%s", wcz[i]+1);
	l=0;
	for (int i=1; i<=n; i++)
	{
		for (int j=1; j<=m; j++)
		{
			if (wcz[i][j]=='-' || wcz[i][j]=='|')
			{
				tab[l]={i, j};
				num[i][j]=l;
				zjeb[l][0]=zjeb[l][1]=0;
				l++;
			}
		}
	}
	for (int i=0; i<2*l; i++)
	{
		sat_val[i]=sat_vis[i]=sat_sort[i]=sat_ile=0;
		implies[i].clear();
	}
	for (int i=0; i<=l; i++)
	{
		zaw[i][0].clear();
		zaw[i][1].clear();
	}
	for (int i=1; i<=n; i++)
		for (int j=1; j<=m; j++)
			co_tu[i][j].clear();
	for (int i=0; i<l; i++)
	{
		for (int h=0; h<2; h++)
		{
			for (int y=0; y<=2; y+=2)
				dfs(tab[i].first+rx[h+y], tab[i].second+ry[h+y], h+y, zaw[i][h]);
			//debug() << i << " " << h << " " << zaw[i][h];
			int czy=0;
			for (auto j : zaw[i][h])
			{
				if (wcz[j.first][j.second]=='-' || wcz[j.first][j.second]=='|')
					czy=1;
			}
			if (czy)
			{
				sat_or(2*i^h^1, 2*i^h^1);
				zjeb[i][h]=1;
			}
			else
			{
				for (auto j : zaw[i][h])
				{
					co_tu[j.first][j.second].push_back(2*i+h);
				}
			}
		}
		if (zjeb[i][0] && zjeb[i][1])
		{
			printf("Case #%d: IMPOSSIBLE\n", t);
			return;
		}
	}
	for (int i=1; i<=n; i++)
	{
		for (int j=1; j<=m; j++)
		{
			if (wcz[i][j]=='.')
			{
				if (co_tu[i][j].empty())
				{
					printf("Case #%d: IMPOSSIBLE\n", t);
					return;
				}
				if (co_tu[i][j].size()==1)
				{
					sat_or(co_tu[i][j][0], co_tu[i][j][0]);
					continue;
				}
				if (co_tu[i][j].size()==2)
				{
					sat_or(co_tu[i][j][0], co_tu[i][j][1]);
					continue;
				}
				assert(false);
			}
		}
	}
	if (!sat2(l))
	{
		printf("Case #%d: IMPOSSIBLE\n", t);
		return;
	}
	printf("Case #%d: POSSIBLE\n", t);
	for (int i=1; i<=n; i++)
	{
		for (int j=1; j<=m; j++)
		{
			if (wcz[i][j]!='-' && wcz[i][j]!='|')
			{
				printf("%c", wcz[i][j]);
				continue;
			}
			if (sat_val[num[i][j]*2])
				printf("|");
			else
				printf("-");
		}
		printf("\n");
	}
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int tt=1; tt<=t; tt++)
		test_case(tt);
	return 0;
}
