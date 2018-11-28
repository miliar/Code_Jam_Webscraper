#include <bits/stdc++.h>

using namespace std;

const int INF = 100000000; // 1e8
const int MAXMINUTE = 24*60;
const int MAXN = 100;
const int MAXPARTITION = MAXN*4 + 2;
int pbusy[2][MAXMINUTE+2];

int dp[MAXMINUTE+2][MAXMINUTE+2][2][2];

const int CAMERON = 0;
const int JAMIE = 1;

int summy(int person, int m_st, int m_ed) {
	int sum = pbusy[person][m_ed];
	if (m_st > 0) sum -= pbusy[person][m_st-1];
	return sum;
}

bool isEmpty(int person, int minut) {
	return pbusy[person][minut] == 0;
}

int solve(int cur_minut, int cameron_tleft, int pfirst, int pprev) {
	if (cur_minut > MAXMINUTE) { // no more element left
		if (cameron_tleft == 0) {
			return pprev != pfirst ? 1 : 0;
		} else {
			return INF;
		}
	} else {
		int &ret = dp[cur_minut][cameron_tleft][pfirst][pprev];
		if (ret != -1) {
			return ret;
		}

		ret = INF;

		int duration = 1;

		// CAMERON
		if (cameron_tleft - duration >= 0 && 
			isEmpty(CAMERON, cur_minut)) {

			ret = min(ret, solve(cur_minut+1, cameron_tleft - duration, 
								pfirst, CAMERON) + (pprev != CAMERON ? 1 : 0));
		}

		// JAMIE
		if (isEmpty(JAMIE, cur_minut)) {
			ret = min(ret, solve(cur_minut+1, cameron_tleft, 
								pfirst, JAMIE) + (pprev != JAMIE ? 1 : 0));
		}

		return ret;
	}
}

int main() {
	int ntc; scanf("%d", &ntc);

	for (int tc = 0; tc < ntc; tc++) {
		int na, nb;
		scanf("%d%d", &na, &nb);

		for (int i = 0; i < MAXMINUTE; i++) {
			pbusy[CAMERON][i] = pbusy[JAMIE][i] = 0;
		}

		for (int i = 0; i < na; i++) {
			int m_st, m_ed;
			scanf("%d%d", &m_st, &m_ed);

			for (int minut = m_st; minut < m_ed; minut++) {
				assert(pbusy[CAMERON][minut] == 0);
				pbusy[CAMERON][minut] = 1;
			}
		}

		for (int i = 0; i < nb; i++) {
			int m_st, m_ed;
			scanf("%d%d", &m_st, &m_ed);

			for (int minut = m_st; minut < m_ed; minut++) {
				assert(pbusy[JAMIE][minut] == 0);
				pbusy[JAMIE][minut] = 1;
			}
		}

		memset(dp, -1, sizeof dp);

		// for (int i = 0; i <= MAXMINUTE; i++) printf("%c", isEmpty(CAMERON, i) ? '0' : '1'); puts("");
		// for (int i = 0; i <= MAXMINUTE; i++) printf("%c", isEmpty(JAMIE, i) ? '0' : '1'); puts("");

		int min_exchange = min(solve(1, MAXMINUTE/2, CAMERON, CAMERON), 
								solve(1, MAXMINUTE/2, JAMIE, JAMIE));

		printf("Case #%d: %d\n", tc+1, min_exchange);
		fflush(stdout);
	}

	return 0;
}