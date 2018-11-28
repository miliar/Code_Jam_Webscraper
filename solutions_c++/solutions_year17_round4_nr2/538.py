#include <bits/stdc++.h>

using namespace std;

typedef pair<int,int> pii;

int main(void)
{
	int T = 0;
	int TK = 0;
	scanf("%d", &T);
	while (T--) {
		// fprintf(stderr, "Case #%d\n", TK);

		int N, C, M;
		vector<int> seats[1111];
		vector<pii> ticketz;
		int seatcount[1111];
		int count[1111];
		memset(seatcount, 0, sizeof(seatcount));
		memset(count, 0, sizeof(count));
		scanf("%d %d %d", &N, &C, &M);
		for (int i = 0;i < M;i++) {
			int seat = 0;
			int buyer = 0;
			scanf("%d %d", &seat, &buyer);
			buyer--;
			seatcount[seat]++;
			count[buyer]++;
			seats[buyer].push_back(seat);
			ticketz.emplace_back(seat, buyer);
		}
		sort(ticketz.begin(), ticketz.end());
		for (int i = 0;i < C;i++) sort(seats[i].begin(), seats[i].end());

		// auto verify = [&](int limit) -> bool {
		// 	int ptr[1111] = {0};
		// 	bool done[1111] = {0};
		// 	for (int i = 0; i < limit; i++) {
		// 		bool haz[1111] = {0};
		// 		int cur = 1;
		// 		for (int j = 0;j < M;j++) {
		// 			if (done[j] || haz[ticketz[j].second]) continue;
		// 			if (ticketz[j].first >= cur) {
		// 				done[j] = true;
		// 				haz[ticketz[j].second] = true;
		// 				cur++;
		// 			}
		// 		}
		// 	}
		// 	bool okay = true;
		// 	for (int i = 0;i < M && okay;i++) okay &= done[i];
		// 	return okay;
		// };
		auto verify = [&] (int limit) -> bool {
			int remain = 0;
			for (int i = N;i > 0;i--) {
				remain += seatcount[i] - limit;
				if (remain < 0) remain = 0;
			}
			return remain == 0;
		};

		int l = *max_element(count, count+C);
		int r = M;
		while (l < r) {
			int mid = (l + r) / 2;
			if (verify(mid)) {
				r = mid;
			} else {
				l = mid + 1;
			}
		}

		int coaster = l;
		int promotion = 0;
		int remain = 0;
		for (int i = N;i > 0;i--) {
			remain += seatcount[i] - coaster;
			promotion += max(seatcount[i] - coaster, 0);
			if (remain < 0) remain = 0;
		}
		assert(remain == 0);
		printf("Case #%d: %d %d\n", ++TK, coaster, promotion);
	}
	return 0;
}