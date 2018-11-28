#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <queue>
#include <cassert>
#include <map>
#include <string>
#include <iomanip>
#include <set>
//#include <unordered_set>
#include <queue>
//#include <unordered_map>
#include <ctime>
#include <vector>
#include <bitset>
#include <list>
#include <stack>
#include <cmath>

using namespace std;

#define FOR(i, n) for (int i = 0; i < (int)(n); ++i)
#define pb push_back
#define sz(v) (int)(v).size()
#define mp make_pair
#define all(v) (v).begin(), (v).end()
#define for1(i,n) for(int i = 1; i <= (int)(n); ++ i)
#define ford1(i,n) for(int i = (int)(n); i >= 1; -- i)
#define ford(i,n) for(int i = (int)(n)-1; i >= 0; -- i)
#define forn(i,n) for(int i = 0; i < (int)(n); ++ i)
#define debug(x) cerr << #x << " = " << x << endl
typedef vector<int> vi;
typedef vector<pair<int, int> > vpi;
typedef pair<int, int> pii;
typedef long long LL;
typedef long double LD;

//using namespace std;

const int N = 1000+10;
const int M = 2*N*N;
int n, C, m;
int p[ N ], b[ N ];


int tope;
int la[N];
int f[M], u[M], c[M], to[M], v[M], ne[M];

struct Flow{
	


	int so, si, nf;

	int ind[N];
	void init(){
		memset(la, -1, sizeof la);		
		tope = 0;
	}
	void add_edge(int v, int to, int u, int c){
		::to[tope] = to;
		::v[tope] = v;
		::u[tope] = u;
		::c[tope] = c;
		ne[tope] = la[v];
		f[tope] = 0;
		la[v] = tope;

		++tope;
		::to[tope] = v;
		::v[tope] = to;
		::u[tope] = 0;
		::c[tope] = -c;
		ne[tope] = la[to];
		la[to] = tope;
		f[tope] = 0;
		++tope;
	}

	int qu[N];
	LL d[N];
	static const LL INF = (LL)1000000000 * 1000000000;

	int inqu[N];
	int p[N];
	LL bellman(bool & ok){
		int st = 0, fi = 0;
		forn(i, nf){
			d[i] = INF;
			inqu[i] = 0;
			p[i] = -1;
		}
		d[so] = 0;
		qu[fi++] = so;
		inqu[so] = 1;
		while (st != fi){
			int v = qu[st++];
			inqu[v] = 0;

			if (st == N)st = 0;
			for (int in = la[v]; in != -1; in = ne[in]){
				int to = ::to[in];
				if (u[in] > f[in] && d[to] > d[v] + c[in]){
					d[to] = d[v] + c[in];
					p[to] = in;
					if (!inqu[to]){
						qu[fi++] = to;
						if (fi == N)
							fi = 0;
						inqu[to] = 1;
					}
				}
			}
		}
		int cr = si;
		if(p[cr]==-1){
			ok = false;
			return 0;
		}
		ok = true;
		while (cr != -1 && p[cr] != -1){
			int in = p[cr];
			++f[in];
			--f[in ^ 1];
			cr = v[in];
		}
		return d[si];
	}
	pair<int,int> mincostflow(){
		int res = 0;		
		int FL = 0;
		while(1){
			bool ok;
			int G = bellman(ok);
			if(!ok)
				break;

			res += G;
			++ FL;
		}
		return mp(FL,res);
	}	
} F;
void solve() {
	//My Clear Code
	scanf("%d%d%d", &n, &C, &m);
	for1(i,m)
		scanf("%d%d", &p[i], &b[i]);
	//C = 2
	F.init();
	F.so = 0;
	F.si = m+1;
	F.nf = F.si+1;
	
	for1(i,m){
		if(b[i]==1){
			F.add_edge(F.so,i,1,0);
		}else{
			F.add_edge(i,F.si,1,0);
		}
	}
	for1(i,m){
		for1(j,i-1){
			if(b[i]!=b[j]){
				if(p[i]==1 && p[j]==1)
					continue;
				bool ok = (p[i]==p[j]);
				
				if(b[i]==1)
					F.add_edge(i,j,1,ok);
				else
					F.add_edge(j,i,1,ok);
			}
		}
	}
	pair<int,int> ans = F.mincostflow();
	printf("%d %d\n", m-ans.first, ans.second);
	//minimum cost maximum matching
}
	

void testgen() {
    FILE *f = fopen("input.txt", "w");
//    srand(time(0));
    fclose(f);
}

int  main(int argc, char* argv[]) {
#ifdef 	albert96
//    testgen();
//    freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);
    
    freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
#else
#define task "blackjack"
    // freopen(task".in", "r", stdin);
    // freopen(task".out", "w", stdout);
#endif

	cout<<fixed;
	cout.precision(4);
	
	cerr<<fixed;
	cerr.precision(12);
	
	int T = 0;
	scanf("%d", &T);
	for1(iter,T){
		cerr<<iter<<endl;
		printf("Case #%d: ", iter);
		solve();
	}

#ifdef albert96
    cerr << "\ntime = " << clock() / (double)CLOCKS_PER_SEC << endl;
#endif
    return 0;
}
