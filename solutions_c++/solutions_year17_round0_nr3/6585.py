#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <string>
#include <queue>
#include <iostream>
#include <algorithm>
using namespace std;

int T, n, K;
priority_queue <int> P;

int main()
{
	freopen("C-small-2-attempt0.in", "r", stdin);
	freopen("C-small-2-attempt0.out", "w", stdout);
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		scanf("%d%d", &n, &K);
		while (!P.empty()) P.pop();
		P.push(n);
		for (int i = 1; i <= K - 1; i++) {
			int t = P.top(); P.pop();
			P.push((t - 1) / 2);
			P.push(t / 2);
		}
		printf("Case #%d: %d %d\n", cas, P.top() / 2, (P.top() - 1) / 2);
	}
	fclose(stdin);
	fclose(stdout);
}
