#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<list>
#include<vector>
#include<queue>
#include<deque>
#include<stack>
#include<map>
#include<set>
#include<functional>
#include<cmath>
#include<string>

#define sd(a) scanf("%d", &a)
#define sld(a) scanf("%lld", &a)

using namespace std;

typedef long long int lli;
typedef pair<int, int> ii;

int xx[4] = { 0, 0, -1, 1 };
int yy[4] = { -1, 1, 0, 0 };

int cou[1010][1010]; // »ç¶÷ ÁÂ¼®

int main(void) {
	int TEST;
	scanf("%d", &TEST);
	for (int CASE = 1; CASE <= TEST; CASE++) {
		int N, M, P; // ÁÂ¼® = N, »ç¶÷ = M, Æ¼ÄÏ = P
		sd(N); sd(M); sd(P);
		int maxi = (P + N - 1) / N;
		for (int i = 0; i <= M; i++) {
			for (int j = 0; j <= N; j++) {
				cou[i][j] = 0;
			}
		}
		
		for (int i = 1; i <= P; i++) {
			int t1, t2; // t1 ÁÂ¼® t2 »ç¶÷
			sd(t1); sd(t2);
			cou[t2][t1]++;
			cou[0][t1]++;
			cou[t2][0]++;
			maxi = max(cou[t2][t1], maxi);
		}
		for (int i = 1; i <= M; i++) {
			maxi = max(cou[i][0], maxi);
		}
		int num_1 = 0;
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= M; j++) {
				num_1 += cou[j][i];
			}
			maxi = max(maxi, (num_1 + i - 1) / i);
		}

		int ans = 0;
		for (int i = 1; i <= N; i++) {
			ans += max(0, cou[0][i] - maxi);
		}

		printf("Case #%d: %d %d\n", CASE, maxi, ans);
	}

	return 0;
}