#include <algorithm>
#include <cmath>
#include <cassert>
#include <cstdio>
#include <utility>
#include <vector>

using namespace std;

#define REP(i,b) for (int i = 0; i < (b); i++)
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define FORD(i,a,b) for (int i = (a); i >= (b); i--)

struct Segment { int from, to, who; };
bool operator<(const Segment &a, const Segment &b) { return a.from < b.from; }

int main() {
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		int N, M;
		scanf("%d%d", &N, &M);
		vector<Segment> S(N+M+2);
		S[0] = (Segment) { -1, 0, -1 };
		S[N+M+1] = (Segment) { 1440, 1441, -1 };
		FOR(i, 1, N+M) {
			scanf("%d%d", &S[i].from, &S[i].to);
			S[i].who = (i <= N) ? 0 : 1;
		}
		sort(S.begin(), S.end());

		int ans = 1440;
		REP(left, 2) REP(right, 2) {
			int rem[2] = { 720, 720 };
			FOR(i, 1, N+M) rem[S[i].who] -= S[i].to - S[i].from;

			//printf("# left=%d\n", left);
			//printf("# right=%d\n", right);

			S[0].who = left;
			S[N+M+1].who = right;

			vector<pair<int, int>> eq;
			int swaps = (left != right) ? 1 : 0;

			REP(i, N+M+1) {
				Segment s = S[i];
				Segment ns = S[i+1];

				if (s.who == ns.who) {
					eq.push_back(make_pair(ns.from - s.to, s.who));
				} else {
					swaps++;
				}
			}
			sort(eq.begin(), eq.end());

			//printf("# swaps=%d\n", swaps);

			for (const pair<int, int> &p : eq) {
				int len = p.first;
				int who = p.second;
				//printf("# eq segment %d %d\n", len, who);

				if (rem[who] >= len) {
					rem[who] -= len;
					//printf("# rem %d = %d\n", who, rem[who]);
				} else {
					swaps += 2;
				}
			}

			//printf("# swaps=%d\n", swaps);
			//printf("\n");

			ans = min(ans, swaps);
		}

		printf("Case #%d: %d\n", tc, ans);
	}
	return 0;
}
