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

const int N_MAX = 1500;
const int mins = 1440;
const int INF = 1e6;
int dp[N_MAX][N_MAX>>1][2][2];

int tms[N_MAX];

int main() {
	int t;
	scanf("%d", &t);
	for(int kase=1; kase<=t; kase++) {
		printf("Case #%d: ", kase);
		int ac, aj;
		scanf("%d%d", &ac, &aj);
		memset(tms, -1, sizeof(tms));
		for(int i=0; i<ac; i++) {
			int st, ed;
			scanf("%d%d", &st, &ed);
			for(;st<ed; st++)
				tms[st] = 0;
		}
		for(int i=0; i<aj; i++) {
			int st, ed;
			scanf("%d%d", &st, &ed);
			for(;st<ed; st++)
				tms[st] = 1;
		}
		debug("||| %d\n", tms[900]);

		for(int i=0; i<N_MAX/2; i++) {
			dp[0][i][0][0] = INF;
			dp[0][i][0][1] = INF;
			dp[0][i][1][0] = INF;
			dp[0][i][1][1] = INF;
		}
		if(tms[0] != 1)
			dp[0][1][0][0] = 0;
		if(tms[0] != 0)
			dp[0][0][1][1] = 0;

		for(int i=1; i<mins; i++) {
			for(int j=0; j<=mins/2; j++) {
				for(int k=0; k<2; k++) {
					for(int m=0; m<2; m++) {
						if(tms[i] == 1-m || (j==0 && m==0))
							dp[i][j][k][m] = INF;
						else {
							if(m==0)
								dp[i][j][k][m] = min(dp[i-1][j-1][k][m], dp[i-1][j-1][k][1-m]+1);
							else
								dp[i][j][k][m] = min(dp[i-1][j][k][m], dp[i-1][j][k][1-m]+1);
						}
					}
				}
			}
		}
		debug("||| %d\n", dp[175][175][0][1]);
		int ans = INF;
		for(int i=0; i<2; i++)
			for(int j=0; j<2; j++)
				ans = min(ans, dp[mins-1][mins>>1][i][j] + (i^j));
		printf("%d\n", ans);
	}
	return 0;
}
