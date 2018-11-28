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

const int N = 100+5;
int n, p;
int a[ N ];
int q[ N ];
void solve() {
	//My Clear Code
	forn(i,10)
		q[i] = 0;
		
	scanf("%d%d", &n, &p);

	for1(i,n){
		scanf("%d", &a[i]);
		a[i] = a[i]%p;
		++ q[ a[i] ];
	}
	
	//q[0], q[1], q[2], q[3]
	int res = q[0];
	
	if(p==2){
		res+=(q[1]+1)/2;
	}else
	if(p==3){
		int m = min(q[1],q[2]);
		res+=m;
		q[1]-=m;
		q[2]-=m;
		res+=(q[1]+2)/3;
		res+=(q[2]+2)/3;
	}else{
		int m = min(q[1],q[3]);
		res+=m;
		res+=q[2]/2;
		q[2] = q[2]%2;

		q[1]-=m;
		q[3]-=m;

		if(q[2]==0){
			res+=(q[1]+3)/4;
			res+=(q[3]+3)/4;
		}

		int k = max(q[1],q[3]);
		
		if(q[2] && !k)
			++ res;
		
		if(q[2] && k){
			++ res;
			if(k >= 2){
				k-=2;
				res+=(k+3)/4;				
			}
		}

	}
	printf("%d\n", res);
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
    
    freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
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
		printf("Case #%d: ", iter);
		solve();
	}

#ifdef albert96
    cerr << "\ntime = " << clock() / (double)CLOCKS_PER_SEC << endl;
#endif
    return 0;
}
