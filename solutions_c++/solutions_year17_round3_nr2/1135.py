#include <bits/stdc++.h>
using namespace std;

bool c_busy[1445], j_busy[1445], used_states[1445][2][725][2];
int dp[1445][2][725][2];

int solve(int minute, int turn, int minutes_j, int first_minute) {
	if(minute == 1440) {
		if(minutes_j == 720) {
			return (first_minute == turn ? 0 : 1);
		}
		else {
			return 2000;
		}
	}
	else if(minutes_j > 720) {
		return 2000;
	}
	else if(used_states[minute][turn][minutes_j][first_minute]) {
		return dp[minute][turn][minutes_j][first_minute];
	}

	int curr_ans = 2000;
	if(!j_busy[minute]) {
		curr_ans = min(curr_ans, solve(minute + 1, 1, minutes_j + 1, first_minute) + (turn == 1 ? 0 : 1));
		if(!c_busy[minute]) {
			curr_ans = min(curr_ans, solve(minute + 1, 0, minutes_j, first_minute) + (turn == 1 ? 1 : 0));
		}
	}
	else {
		curr_ans = min(curr_ans, solve(minute + 1, 0, minutes_j, first_minute) + (turn == 1 ? 1 : 0));
	}

	dp[minute][turn][minutes_j][first_minute] = curr_ans;
	used_states[minute][turn][minutes_j][first_minute] = true;

	return curr_ans;
}

int main() {
	int cnt_tests;
	scanf("%d", &cnt_tests);

	for(int cs = 1; cs <= cnt_tests; cs++) {
		int aj, ac;
		scanf("%d%d", &ac, &aj);

		memset(c_busy, 0, sizeof(c_busy));
		memset(j_busy, 0, sizeof(j_busy));
		for(int i = 0; i < ac; i++) {
			int c, d;
			scanf("%d%d", &c, &d);

			for(int j = c; j < d; j++) {
				c_busy[j] = true;
			}
		}
		for(int i = 0; i < aj; i++) {
			int c, d;
			scanf("%d%d", &c, &d);

			for(int j = c; j < d; j++) {
				j_busy[j] = true;
			}
		}

		memset(used_states, 0, sizeof(used_states));
		
		int ans = 2000;
		if(!j_busy[0]) {
			ans = min(ans, solve(1, 1, 1, 1));
		}
		if(!c_busy[0]) {
			ans = min(ans, solve(1, 0, 0, 0));
		}

		printf("Case #%d: %d\n", cs, ans);
	}

	return 0;
}
