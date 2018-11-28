#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;
typedef long long ll;
typedef vector<int> vi;

#define pb push_back
#define eb emplace_back
#define mp make_pair
#define fi first
#define se second
#define rep(i,n) rep2(i,0,n)
#define rep2(i,m,n) for(int i=m;i<(n);i++)
#define ALL(c) (c).begin(),(c).end()

inline void chmax(int &x, int y)
{
	if (x < y) x = y;
}

int TC;
int N, P;
int c[5];
int dp[2000010];
int num[5];
int md[2000010];

int getid()
{
	int x = 0;
	for (int j = P-1; j >= 1; --j) {
		x = x * 110 + num[j];
	}
	return x;
}

int main() {
	scanf("%d", &TC);

	rep(tc, TC) {
		printf("Case #%d: ", tc + 1);

		scanf("%d %d", &N, &P);
		rep(i, P) c[i] = 0;

		rep(i, N) {
			int x;
			scanf("%d", &x);
			c[x % P]++;
		}

		memset(dp, -1, sizeof(dp));	
		dp[0] = 0;

		rep(i, 2000010) {
			int ii = i;
			int r = 0;

			for (int j = 1; j < P; ++j) {
				num[j] = ii % 110;
				r = (r + j * num[j]) % P;
				ii /= 110;
			}		

			md[i] = r;
		}
		int ret = 0;

		rep(i, 2000010) {
			ret = max(ret, dp[i]);
			if (dp[i] != -1) {
				int ii = i;
				for (int j = 1; j < P; ++j) {
					num[j] = ii % 110;
					ii /= 110;
				}
				for (int j = 1; j < P; ++j) {
					if (num[j] + 1 <= c[j]) {
						++num[j];
						int ni = getid();
						--num[j];
						chmax(dp[ni], dp[i] + (md[i] == 0));
					}
				}
			}
		}

		printf("%d\n", ret + c[0]);

	}

	return 0;
}