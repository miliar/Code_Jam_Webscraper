#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstdlib>
#include <ctime>
#include <deque>
using namespace std;

char S[11000];
int k;
int a[11000];

void doit() {
	scanf("%s", S + 1);
	scanf("%d", &k);
	int n = strlen(S + 1);
	for (int i = 1; i <= n; i++)
		a[i] = (S[i] == '-');
	int ans = 0;
	for (int i = 1; i + k - 1 <= n; i++)
		if (a[i]) {
			for (int j = i; j <= i + k - 1; j++)
				a[j] ^= 1;
			ans += 1;
		}
	for (int i = 1; i <= n; i++)
		if (a[i]) {
			printf("IMPOSSIBLE\n");
			return ;
		}
	printf("%d\n", ans);
}

int main() {
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		printf("Case #%d: ", i);
		doit();
	}
}