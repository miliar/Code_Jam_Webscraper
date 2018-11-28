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

const int N = 1000 + 13;
const int M = 6;

int n;
int a[M];


bool read(){
	if(scanf("%d", &n) != 1)
		return 0;
	forn(i, M)
		scanf("%d", &a[i]);
	return 1;
}


char res[] = {'R', 'O', 'Y', 'G', 'B', 'V'};
int perm[] = {0, 2, 4};


bool comp(const int &b, const int &c){
	return a[b] > a[c];
}


void solve(){
	sort(perm, perm + 3, comp);
	string ans = "";
	if (a[1] != 0 || a[3] != 0 || a[5] != 0){
		printf("IMPOSSIBLE\n");
		return;
	}
	int cur = 0;
	forn(i, n)
		ans += '-';
	for (int i = 0; i < n; i += 2){
		while (a[perm[cur]] == 0)
			++cur;
		ans[i] = res[perm[cur]];
		--a[perm[cur]];
	}
	for (int i = 1; i < n; i += 2){
		while (a[perm[cur]] == 0)
			++cur;
		ans[i] = res[perm[cur]];
		--a[perm[cur]];
	}
	forn(i, n)
		if (ans[i] == ans[(i + 1) % n]){
			printf("IMPOSSIBLE\n");
			return;
		}
	printf("%s\n", ans.c_str());
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