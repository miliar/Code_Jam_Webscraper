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

#define sd(a) scanf("%d", &a);
#define sld(a) scanf("%lld", &a);

using namespace std;

typedef long long int lli;
typedef pair<int, int> ii;

int xx[4] = { 0, 0, -1, 1 };
int yy[4] = { -1, 1, 0, 0 };

int main(void) {
	int TEST;
	scanf("%d", &TEST);
	for (int CASE = 1; CASE <= TEST; CASE++) {
		lli N;
		scanf("%lld", &N);
		char str[30];
		sprintf(str, "%lld", N);

		int cur = 0;
		int st_ind = 0;

		for (int i = 0; str[i] != 0; i++) {
			if (str[i] > cur) {
				cur = str[i];
				st_ind = i;
			}
			else if (str[i] < cur) {
				str[st_ind]--;
				for (int j = st_ind + 1; str[j] != 0; j++) {
					str[j] = '9';
				}
				break;
			}
		}

		lli ans = atoll(str);

		printf("Case #%d: %lld\n", CASE, ans);
	}

	return 0;
}