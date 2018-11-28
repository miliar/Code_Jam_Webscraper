#include <bits/stdc++.h>
#define REP(i, a, b) for (int i = a; i <= b; ++i)
#define PER(i, a, b) for (int i = a; i >= b; --i)
#define RVC(i, S) for (int i = 0; i < S.size(); ++i)
#define mp make_pair
#define pb push_back
#define debug(...) fprintf(stderr, __VA_ARGS__)
#define fi first
#define se second
using namespace std;
 
typedef long long LL;
typedef pair<int, int> pii;
typedef vector<int> VI;
 
inline int read(){
	int x = 0, ch = getchar(), f = 1;
	while (!isdigit(ch)){if (ch == '-') f = -1; ch = getchar();}
	while (isdigit(ch)) x = x * 10 + ch - '0', ch = getchar();
	return x * f;
}

int n, p, a[105], perm[10];
vector<pair<pii, pii> > sol;

void solve(){
	n = read(), p = read();
	REP(i, 1, n) a[i] = read();
	if (p == 2){
		int even = 0;
		REP(i, 1, n) even += a[i] % 2 == 0;
		cout << even + (n - even + 1) / 2 << endl;
	}
	else if (p == 3){
		int cnt[3] = {0, 0, 0};
		REP(i, 1, n) cnt[a[i] % 3]++;
		int ans = cnt[0] + min(cnt[1], cnt[2])
			+ (int)ceil(1.0 * abs(cnt[1] - cnt[2]) / 3);
		cout << ans << endl;
	}
	else{
		int cnt[4] = {0, 0, 0, 0};
		REP(i, 1, n) cnt[a[i] % 4]++;
		int ans = 0;
		REP(i, 1, 7) perm[i] = i;
		do{
			int fuck = 0, A = cnt[1], B = cnt[2], C = cnt[3];
			for (int i = 1; i <= n; i++) {
					int t = perm[i];
                    if (t == 1) {
                        int tmp = min(A, C);
                        fuck += tmp;
                        A -= tmp;
                        C -= tmp;
                    }
                    if (t == 2) {
                        int tmp = B / 2;
                        fuck += tmp;
                        B = B % 2;
                    }
                    if (t == 3) {
                        int t = min(A / 2, B);
                        fuck += t;
                        A -= t * 2;
                        B -= t;
                    }
                    if (t == 4) {
                        int t = min(B, C / 2);
                        fuck += t;
                        B -= t;
                        C -= t * 2;
                    }
                    if (t == 5) {
                        fuck += A / 4;
                        A %= 4;
                    }
                    if (t == 6) {
                        fuck += B / 4;
                        B %= 4;
                    }
                    if (t == 7) {
                        fuck += C / 4;
                        C %= 4;
                    }
            
            }
			if (A || B || C) ++ fuck;
			ans = max(ans, fuck);
		} while (next_permutation(perm + 1, perm + 7 + 1));
		printf("%d\n", ans + cnt[0]);
	}
}

int main(){

	/*REP(i, 1, 3) REP(j, 1, 3)
		if (i <= j && (i + j) % 4 == 0) sol.pb(mp(mp(i, j), mp(0, 0)));
	REP(i, 1, 3) REP(j, 1, 3) REP(k, 1, 3)
		if (i <= j && j <= k && (i + j + k) % 4 == 0)
			sol.pb(mp(i, j), mp(k, 0));
	REP(i, 1, 3) REP(j, 1, 3) REP(k, 1, 3) REP(l, 1, 3)
		if (i <= j && j <= k && k <= l && (i + j + k + l) % 4 == 0)
			sol.pb(mp(i, j), mp(k, l));
*/
	int T = read();
	REP(i, 1, T){
		printf("Case #%d: ", i);
		solve();
	}	
	return 0;
}
