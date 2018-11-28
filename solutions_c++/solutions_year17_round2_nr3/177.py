#define _CRT_SECURE_NO_WARNINGS
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
#include <unordered_set>
#include <queue>
#include <unordered_map>
#include <ctime>
#include <vector>
#include <bitset>
#include <list>
#include <stack>
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

const int N = 100+5;

int n, Q;
int e[ N ], s[ N ];
LL g[ N ][ N ];

int st[ N*N ], fi[ N*N ];

LD go[ N ][ N ];
void solve() {
	scanf("%d%d", &n, &Q);
	
	for1(i,n){
		scanf("%d%d", &e[i], &s[i]);
	}
	for1(i,n){
		for1(j,n){
			int x;
			scanf("%d", &x);
			g[i][j] = x;
		}
	}
	for1(i,Q){
		scanf("%d%d", &st[i], &fi[i]);
	}
	for1(k,n){
		for1(i,n){
			for1(j,n){
				if(i!=j && g[i][k]!=-1 && g[k][j]!=-1 && (g[i][j]==-1 || g[i][j] > g[i][k]+g[k][j]) ){
					g[i][j] = g[i][k]+g[k][j];
				}
			}
		}
	}
	for1(i,n){
		for1(j,n){
			go[i][j]=-1.0;
			if(g[i][j]!=-1 && g[i][j] <= e[i]){
				go[i][j] = (LD)g[i][j]/s[i];
			}
		}
	}
	const LD U = -0.5;
	for1(k,n){
		for1(i,n){
			for1(j,n){
				if(i!=j && go[i][k] > U && go[k][j] > U && (go[i][j] < U || go[i][j] > go[i][k]+go[k][j])){
					go[i][j] = go[i][k]+go[k][j];
				}
			}
		}
	}
	for1(i,Q){
		cout<<go[ st[i] ][ fi[i] ]<<" ";
	}
	cout<<endl;
}

void testgen() {
    FILE *f = fopen("input.txt", "w");
    // srand(time(0));
    fclose(f);
}

int  main(int argc, char* argv[]) {
#ifdef 	albert96
    // testgen();
//    freopen("input.txt", "r", stdin);
    
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    
    // freopen("output.txt", "w", stdout);
#else
#define task "blackjack"
    // freopen(task".in", "r", stdin);
    // freopen(task".out", "w", stdout);
#endif
	cout<<fixed;
	cout.precision(23);
	
    int T;
    scanf("%d", &T);
    for1(iter,T){
		printf("Case #%d: ", iter);
		solve();
	}

#ifdef albert96
    cerr << "\ntime = " << clock() / (double)CLOCKS_PER_SEC << endl;
#endif
    return 0;
}
