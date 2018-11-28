#include <bits/stdc++.h>
using namespace std;
#define REP(i, n) for (int i = 0; i < int(n); i++)
#define FOREACH(i, v) for (__typeof((v).begin()) i = (v).begin(); i != (v).end(); i++)
#define SIZE(v) ((int)(v).size())
#define pb push_back
#define mp make_pair
#define st first
#define nd second
#define ll long long
#define pii pair<int, int>
#define tipo pair<ll, int>

double dp[1010];
bitset<1010> visited;
ll K[1010], S[1010], D, N;

double inter(int i, int j) {
	return (double)(K[i] - K[j])/((double)(S[j] - S[i]));
}

void solve(int n) {
	if(visited[n]) return;
	else {
		visited[n] = true;
		if(n == N - 1) dp[n] =  ((double)(D - K[n]))/((double)S[n]);
		else {
			int idx = -1;
			double tidx = INFINITY;
			for(int i = n + 1; i < N; i++) {
				double t = inter(n, i);
				if(t > 0 && tidx > t) {
					tidx = t;
					idx = i;
				}
			}
			if(idx == -1) dp[n] =  ((double)(D - K[n]))/((double)S[n]);
			else {			
				solve(idx);
				dp[n] = dp[idx];
			}
		}
	}
}

int id[1010];
ll Kaux[1010], Saux[1010];


bool compare(int i, int j) {
	return Kaux[i] < Kaux[j];
}

int main() {
	int T;
	scanf("%d", &T);
	REP(t, T) {
		visited.reset();
		scanf("%lld %lld", &D, &N);
		REP(i, N) scanf("%lld %lld", &Kaux[i], &Saux[i]);
		REP(i, N) id[i] = i;
		sort(id, id + N, compare);
		REP(i, N) {
			K[i] = Kaux[id[i]];
			S[i] = Saux[id[i]];
		}
		double ttt = 0.0;
		REP(n, N) {
			ttt = max(ttt, ((double)(D - K[n]))/((double)S[n]));
		}
		//solve(0);
		//double tt = dp[0];
		//printf("dd %f\n", dp[0]);
		printf("Case #%d: %.8f\n", t + 1, (double)D/ttt);
	}
}
