#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;

const int MAX = 1024;
int activity[1445];

int Nc, Nj;

int memo[1445][725][3][3];

int solve(int minute, int jamie_time, int resp, int started) {
	//printf("%d %d %d\n", cur, jamie_time, resp);
	if (minute == 1440) {
		if (jamie_time == 720)
			return (started == resp) ? 0 : 1;
		return 1000000;
	}

	int &ret = memo[minute][jamie_time][resp][started];
	if (ret != -1) return ret;
	ret = 1000000;
	if (activity[minute] == 0) {
		if (jamie_time + 1 <= 720) {
			ret = min(ret, ((resp == 1) ? 1 : 0) + solve(minute + 1, jamie_time + 1, 2, started));
		}
		ret = min(ret, ((resp == 2) ? 1 : 0) + solve(minute + 1, jamie_time, 1, started));
	} else if (activity[minute] == 1) {
		if (jamie_time + 1 <= 720)
			ret = min(ret, ((resp == 1) ? 1 : 0) + solve(minute + 1, jamie_time + 1, 2, started));
	} else if (activity[minute] == 2) {
		ret = min(ret, ((resp == 2) ? 1 : 0) + solve(minute + 1, jamie_time, 1, started));
	}
	//printf("%d %d %d %d\n", minute, jamie_time, resp, ret);
	return ret;
}

int main() {
	int tests, R, H;
	scanf("%d", &tests);
	for (int case_no = 1; case_no <= tests; ++case_no) {
		scanf("%d %d", &Nc, &Nj);
		int S, E;
		memset(activity, 0, sizeof(activity));
		for (int i = 0; i < Nc; ++i) {
			scanf("%d %d", &S, &E);
			for (int x = S; x < E; ++x)
				activity[x] = 1;
		}

		for (int i = 0; i < Nj; ++i) {
			scanf("%d %d", &S, &E);
			for (int x = S; x < E; ++x)
				activity[x] = 2;
		}

		memset(memo, -1, sizeof(memo));
		int ret = 1000000;
		if (activity[0] == 0) {
			ret = min(ret, solve(1, 1, 2, 2));
			ret = min(ret, solve(1, 0, 1, 1));
		} else if (activity[0] == 1) {
				ret = min(ret, solve(1, 1, 2, 2));
		} else if (activity[0] == 2) {
			ret = min(ret, solve(1, 0, 1, 1));
		}

		printf("Case #%d: %d\n", case_no, ret);

	}
	return 0;
}