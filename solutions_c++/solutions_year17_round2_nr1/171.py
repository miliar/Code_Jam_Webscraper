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

//1000
const int N = 1000+5;

int D, n;
struct Horse{
	int x, v;
	bool operator<(const Horse &R)const{
		return x < R.x;
	}
};
Horse a[ N ];

void solve() {

	scanf("%d%d", &D, &n);
	for1(i,n){
		scanf("%d%d", &a[i].x, &a[i].v);
	}	
	sort(a+1,a+n+1);
	LD ma = 0.0;
	ford1(i,n){
		//D==a[i].x+t*a[i].v
		LD t = (LD)(D-a[i].x)/a[i].v;
		ma = max(ma,t);
	}
	cout<<D/ma<<endl;
}

void testgen() {
    FILE *f = fopen("input.txt", "w");
    // srand(time(0));
    fclose(f);
}

int  main(int argc, char* argv[]) {
#ifdef 	albert96
    // testgen();
    //freopen("input.txt", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    
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
