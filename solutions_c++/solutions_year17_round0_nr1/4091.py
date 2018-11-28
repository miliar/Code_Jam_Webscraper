#include <cstring>
#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = 1005;

char s[MAXN];
int k;

void solve(int t) {
	printf("Case #%d: ", t);
	scanf("%s%d", s + 1, &k);
	int len = strlen(s + 1), tim = 0;
	for (int i = 1; i + k - 1 <= len; i ++) {
		if (s[i] == '+') continue;
		for (int j = 0; j < k; j ++)
			s[i + j] = (s[i + j] == '-') ? '+' : '-';
		tim ++;
	}
	for (int i = 1; i <= len; i ++)
		if (s[i] == '-') {
			printf("IMPOSSIBLE\n");
			return;
		}
	printf("%d\n", tim);
}

int main() {
	//freopen("A.in", "r", stdin), freopen("A.out", "w", stdout);
	
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i ++) solve(i);
}