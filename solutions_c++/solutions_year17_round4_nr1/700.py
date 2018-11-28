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

int main(void) {
	int TEST;
	scanf("%d", &TEST);
	for (int CASE = 1; CASE <= TEST; CASE++) {
		int N, P;
		sd(N); sd(P);
		int num[4];
		for (int i = 0; i < 4; i++) {
			num[i] = 0;
		}
		for (int i = 1; i <= N; i++) {
			int temp;
			scanf("%d", &temp);
			num[temp % P]++;
		}

		int ans = num[0];
		if (P == 2) {
			ans += ((num[1] + 1) / 2);
		}
		if (P == 3) {
			if (num[1] > num[2]) {
				ans += num[2];
				num[1] -= num[2];
				ans += ((num[1] + 2) / 3);
			}
			else {
				ans += num[1];
				num[2] -= num[1];
				ans += ((num[2] + 2) / 3);
			}
		}
		if (P == 4) {
			ans += ((num[2] + 1) / 2);
			bool check = true;
			if (ans % 2 == 0) {
				check = false;
			}

			if (num[1] > num[3]) {
				ans += num[3];
				num[1] -= num[3];
				if (check) {
					num[1] -= 2;
				}
				if (num[1] > 0) {
					ans += ((num[1] + 3) / 4);
				}
			}
			else {
				ans += num[1];
				num[3] -= num[1];
				if (check) {
					num[3] -= 2;
				}
				if (num[3] > 0) {
					ans += ((num[3] + 3) / 4);
				}
			}
		}

		printf("Case #%d: %d\n", CASE, ans);
	}

	return 0;
}