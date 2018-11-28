#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mp make_pair
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef complex<double> point;
#define xx real()
#define yy imag()

#define REP(i, a, b) for(int i = (a); i < (int)(b); i++)
#define REPN(i, a, b) for(int i = (a); i <= (int)(b); i++)
#define FA(it, x) for(__typeof((x).begin()) it = (x).begin(); it != (x).end(); it++)
#define SZ(x) (int)(x).size()
#define BE(x) (x).begin(), (x).end()
#define SORT(x) sort(BE(x))
#define _1 first
#define _2 second

#define x1 gray_cat_x1
#define y1 gray_cat_y1

template<class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }

#define file "I1"

const double EPS = 1e-9;
const double PI = acos(-1.);
const int INF = 1e9;
const ll MOD = 1e9 + 7;

const int MAXN = 1e3 + 5;

char c[MAXN][MAXN];

void solve(int t){
	int n, m;
	scanf("%d%d", &n, &m);
	REP(i, 0, n){
		scanf("%s", &c[i][0]);
	}
	REP(i, 0, n){
		char last = '?';
		REP(j, 0, m){
			if (c[i][j] != '?'){
				last = c[i][j];
			} else {
				c[i][j] = last;
			}
		}
		
		last = '?';
		for(int j = m - 1; j >= 0; j--){
			if (c[i][j] != '?'){
				last = c[i][j];
			} else {
				c[i][j] = last;
			}
		}
	}
	
	REP(j, 0, m){
		char last = '?';
		REP(i, 0, n){
			if (c[i][j] != '?'){
				last = c[i][j];
			} else {
				c[i][j] = last;
			}
		}
		
		last = '?';
		for(int i = n - 1; i >= 0; i--){
			if (c[i][j] != '?'){
				last = c[i][j];
			} else {
				c[i][j] = last;
			}
		}
	}
	
	printf("Case #%d:\n", t);
	REP(i, 0, n){
		printf("%s\n", c[i]);
	}
}   

int main(){
#ifndef ONLINE_JUDGE
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    //freopen(file".in", "r", stdin); freopen(file".out", "w", stdout);
    int t = 1;
    //cin >> t;
    cin >> t;
    for(int i = 1; i <= t; i++){
        solve(i);    
    }
}
