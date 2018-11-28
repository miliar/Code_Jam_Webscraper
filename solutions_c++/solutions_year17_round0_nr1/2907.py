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

const int N = 1000 + 7;

string s;
int n, k;
char buf[N];


bool read(){
	if(scanf("%s %d\n", buf, &k) != 2)
		return 0;
	s = buf;
	n = sz(s);
	return 1;
}


int solve(){
	set<int> pos;
	int res = 0;
	forn(i, n - k + 1){
		if (((s[i] == '-') + sz(pos)) % 2){
			pos.insert(i + k);
			res++;
		}
		if (*pos.begin() == i + 1)
			pos.erase(pos.begin());
	}
	fore(i, n - k + 1, n){
		if (((s[i] == '-') + sz(pos)) % 2)
			return -1;
		if (*pos.begin() == i + 1)
			pos.erase(pos.begin());
	}
	return res;
}


int main(){
	#ifdef _DEBUG
		freopen("input.txt", "r", stdin);
	#endif
	int n;
	scanf("%d\n", &n);
	int cnt = 1;
	forn(i, n){
		read();
		int res = solve();
		printf("Case #%d: ", cnt++);
		if (res == -1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", res);
	}
	return 0;
}