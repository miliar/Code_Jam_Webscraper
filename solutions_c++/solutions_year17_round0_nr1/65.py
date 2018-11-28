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

char str[1010];

void change(int ind, int K) {
	for (int i = ind; i < ind + K; i++) {
		if (str[i] == '-') {
			str[i] = '+';
		}
		else {
			str[i] = '-';
		}
	}
}

int main(void) {
	int TEST;
	scanf("%d\n", &TEST);
	for (int CASE = 1; CASE <= TEST; CASE++) {
		int K;
		scanf("%s %d", str, &K);
		int len = strlen(str);
		int cou = 0;
		for (int i = 0; i <= len - K; i++) {
			if (str[i] == '-') {
				cou++;
				change(i, K);
			}
		}
		bool ans = true;
		for (int i = 0; i < len; i++) {
			if (str[i] == '-') {
				ans = false;
			}
		}

		if (ans) {
			printf("Case #%d: %d\n", CASE, cou);
		}
		else {
			printf("Case #%d: IMPOSSIBLE\n", CASE);
		}
	}

	return 0;
}