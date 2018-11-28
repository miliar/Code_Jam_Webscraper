#include <bits/stdc++.h>
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#ifdef _DEBUG_
	#define debug(...) printf(__VA_ARGS__)
#else
	#define debug(...) (void)0
#endif
using namespace std;
typedef long long ll;
typedef pair<int,int> PII;
typedef vector<int> VI;

const int MAXNP = 50 + 50;
const int UPBOUND = 2e6;

bool check(ll rt, int q) {
	return q >= (rt * 9 - 1) / 10 + 1 && q <= (rt * 11) / 10;
}

PII find_range(int r, int q) {
	debug("%d - %d\n", r, q);
	int base = q / r;
	PII res;
	do {
		int lb = 1, rb = base;
		while(lb <= rb) {
			int m = (lb + rb) / 2;
			if(check(1ll * r * m, q))
				rb = m - 1;
			else
				lb = m + 1;
		}
		res.F = lb;
	} while(0);
	do {
		int lb = base + 1, rb = UPBOUND;
		while(lb <= rb) {
			int m = (lb + rb) / 2;
			if(check(1ll * r * m, q))
				lb = m + 1;
			else
				rb = m - 1;
		}
		res.S = rb;
	} while(0);
	return res;
}

int N, P;
int R[MAXNP], Qin[MAXNP][MAXNP];
PII Q[MAXNP][MAXNP];
int id[MAXNP];
int main() {
	debug("~\n");
	int all_kase;
	scanf("%d", &all_kase);
	for(int num_kase = 1; num_kase <= all_kase; num_kase++) {
		scanf("%d%d", &N, &P);
		for(int i = 1; i <= N; i++)
			scanf("%d", &R[i]);
		for(int i = 1; i <= N; i++)
			for(int j = 1; j <= P; j++) {
				scanf("%d", &Qin[i][j]);
				Q[i][j] = find_range(R[i], Qin[i][j]);
			}
		for(int i = 1; i <= N; i++)
			sort(Q[i] + 1, Q[i] + P + 1);
		for(int i = 1; i <= N; i++)
			id[i] = 0;
		int ans = 0;
		while(1) {
			int num = 0;
			for(int i = 1; i <= N; i++) {
				if(id[i] == P) {
					num = -1;
					break;
				}
				num = max(num, Q[i][id[i] + 1].F);
			}
			if(num == -1) break;
			debug("line %d\n", __LINE__);
			bool good = true;
			for(int i = 1; i <= N; i++) {
				while(id[i] < P) {
					debug("line %d (%d)\n", __LINE__, id[i]);
					id[i]++;
					if(Q[i][id[i]].S < num) continue;
					if(Q[i][id[i]].F > num) good = false;
					id[i]--;
					break;
				}
				if(id[i] == P) good = false;
			}
			debug("line %d\n", __LINE__);
			if(good) {
				ans++;
				for(int i = 1; i <= N; i++)
					id[i]++;
			}
		}
		printf("Case #%d: %d\n", num_kase, ans);
	}
	return 0;
}
