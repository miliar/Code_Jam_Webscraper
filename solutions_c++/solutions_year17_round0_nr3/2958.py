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

const int N = 1000 * 1000 + 7;

li k, n;


bool read(){
	if(scanf("%lld%lld", &n, &k) != 2)
		return 0;
	return 1;
}

map<li, li> cur;


void get(li n){
	cur[n]++;
	//printf("\n");
	while (1){
		//printf("[");
		//for (auto it : cur)
		//	printf("(%lld %lld) ", it.x, it.y);
		//printf("] ");
		pll tmp = *(cur.rbegin());
		//printf("{%lld %lld} ", tmp.x, tmp.y);
		cur.erase(tmp.x);
		//printf("2[");
		//for (auto it : cur)
		//	printf("(%lld %lld) ", it.x, it.y);
		//printf("] ");
		li t = max(0ll, tmp.x - 1);
		if (t == 0)
			break;
		if (tmp.y > k){
			printf("%lld %lld\n", t - t / 2, t / 2);
			return;
		}
		else{
			k -= tmp.y;
			cur[t - t / 2] += tmp.y;
			cur[t / 2] += tmp.y;
		}
	}
	printf("0 0\n");
}


void solve(){
	cur = map<li, li>();
	--k;
	get(n);
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