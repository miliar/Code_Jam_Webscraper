#include <bits/stdc++.h>

#define debug(x) cout << #x << " = " << x << endl
#define fori(i, ini, lim) for(int i = int(ini); i < int(lim); i++)
#define ford(i, ini, lim) for(int i = int(ini); i >= int(lim); i--)

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef tuple<int, int, int, int> state;

const int MAX = 1e2 + 5;
const int UPPER_BOUND = 100;
const int INF = 1 << 30;
int dis[MAX][MAX][MAX][MAX];
int HD, AD, HK, AK, B, D;

int bfs() {
	memset(dis, -1, sizeof dis);
	queue<state> q;
	dis[HD][AD][HK][AK] = 0;
	q.emplace(HD, AD, HK, AK);
	int ans = INF;
	while(!q.empty()) {
		auto cur = q.front(); q.pop();
		int hd, ad, hk, ak;
		tie(hd, ad, hk, ak) = cur;
		int cur_dis = dis[hd][ad][hk][ak];
		if(hk == 0) {
			ans = dis[hd][ad][hk][ak];
			break;
		}
		else if(hd == 0) {
			continue;
		}
		// attack
		if(dis[max(0, hd - ak)][ad][max(0, hk - ad)][ak] == -1) {
			dis[max(0, hd - ak)][ad][max(0, hk - ad)][ak] = cur_dis + 1;
			q.emplace(max(0, hd - ak), ad, max(0, hk - ad), ak);
		}
		// buff
		if(dis[max(0, hd - ak)][min(UPPER_BOUND, ad + B)][hk][ak] == -1) {
			dis[max(0, hd - ak)][min(UPPER_BOUND, ad + B)][hk][ak] = cur_dis + 1;
			q.emplace(max(0, hd - ak), min(UPPER_BOUND, ad + B), hk, ak);
		}
		// cure
		if(dis[max(0, HD - ak)][ad][hk][ak] == -1) {
			dis[max(0, HD - ak)][ad][hk][ak] = cur_dis + 1;
			q.emplace(max(0, HD - ak), ad, hk, ak);
		}
		// debuff
		if(dis[max(0, hd - max(0, (ak - D)))][ad][hk][max(0, ak - D)] == -1) {
			dis[max(0, hd - max(0, (ak - D)))][ad][hk][max(0, ak - D)] = cur_dis + 1;
			q.emplace(max(0, hd - max(0, (ak - D))), ad, hk, max(0, ak - D));
		}
	}
	return ans;
}

int main() {
	int t;
	scanf("%d", &t);
	int kase = 1;
	while(t--) {
		scanf("%d %d %d %d %d %d", &HD, &AD, &HK, &AK, &B, &D);
		int ans = bfs();
		printf("Case #%d: ", kase++);
		if(ans == INF) {
			puts("IMPOSSIBLE");
		}
		else {
			printf("%d\n", ans);
		}
	}

	return 0;
}

