#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define sz(x) (int)(x).size()
#define li long long
#define ld long double
#define x first
#define y second
#define pt pair<int, int>
#define pll pair<li, li>
#define forn(i, t) for(int i = 0; i < (t); i++)
#define fore(i, f, t) for(int i = (f); i < (t); i++)
#define forr(i, f, t) for(int i = (f) - 1; i >= (t); i--)
#define all(x) (x).begin(), (x).end()
#define ins insert

using namespace std;


const int INF = 1e9;
const int MOD = 1e9 + 7;
const li INF64 = 1e18;
const ld EPS = 1e-7;

mt19937 myrand(time(NULL));

const int N = 53;

int n, m;
double u;
double a[N];


bool read(){
	if(scanf("%d%d", &n, &m) != 2)
		return 0;
	scanf("%lf", &u);
	forn(i, n)
		scanf("%lf", &a[i]);
	return 1;
}


bool check(ld mid){
	ld k = u;
	forn(i, n)
		if (a[i] < mid)
			k -= (mid - a[i]);
	return (k > 0);
}


void print(ld mid){
	ld k = u;
	forn(i, n)
		if (a[i] < mid){
			k -= (mid - a[i]);
			a[i] = mid;
		}
	k /= n;
	forn(i, n)
		a[i] = min((ld)1.0, k + a[i]);
	ld ans = 1;
	forn(i, n)
		ans *= a[i];
	printf("%.15f\n", double(ans));
}


void solve(){
	ld l = 0, r = 1;
	forn(i, 300){
		ld m = (l + r) / 2;
		if (check(m))
			l = m;
		else
			r = m;
	}
	
	print(l);
}


int main(){
	#ifdef _DEBUG
		freopen("input.txt", "r", stdin);
	#endif
	int n;
	scanf("%d\n", &n);
	forn(i, n){
		read();
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}