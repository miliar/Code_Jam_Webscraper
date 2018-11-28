
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <functional>

#define MIN(X,Y) ((X) < (Y) ? (X) : (Y))  
#define MAX(X,Y) ((X) > (Y) ? (X) : (Y))  

using namespace std;

int N, P;
int G[110] = { 0, };
int Cal(int n, int p) {
	pair<int, int> ans;

	if (n%p != 0) {
		ans.first = n / p + 1;
		ans.second = ans.first * p - n;
	}
	else {
		ans.first = n / p;
		ans.second = 0;
	}

	return ans.second;
}

int V[1010][1010] = { 0, };
int Check[1010] = { 0, };
int Peo[1010] = { 0, };
int Sheet[1010] = { 0, };

int __main()
{
	int N, M, C;
	int ans = 0, i, j;
	pair<int, int> T[1010];
	scanf("%d%d%d", &N, &C, &M);

	for (i = 0; i <= M; i++) {
		for (j = 0; j <= C; j++) {
			V[i][j] = 0;
		}
		Check[i] = 0;
	}
	for (i = 0; i <= N; i++) {
		Sheet[i] = 0;
	}


	for (i = 0; i < M; i++) {
		int x, y;
		scanf("%d%d", &x, &y);

		T[i].first = x;
		T[i].second = y;
	}

	std::sort(T, T + M);
	int u = 0, cnt = 0, last =0;
	

	for (ans = 1;; ans++) {
		u = 0; last = 0;

		for (i = 1; i <= C; i++) {
			Peo[i] = 0;
		}

		for (i = 0; i < M; i++) {
			if (Check[i] != 0) continue;
			if (Peo[T[i].second] != 0) continue;

			
			u += MAX(T[i].first - last - 1, 0);

			if (last == T[i].first) {
				if (u == 0) continue;
				u--;
			}

			Peo[T[i].second] = 1;
			last = T[i].first;
			cnt++;

			Check[i] = 1;
		}

		if (cnt == M) break;
	}

	cnt = 0;
	for (i = 0; i < M; i++) {
		Sheet[T[i].first]++;
	}

	for (i = 0; i <= N; i++) {
		if (Sheet[i] > ans) cnt += Sheet[i] - ans;
	}

	printf("%d %d", ans, cnt);

	return 0;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, ct;

	cin >> ct;
	for (t = 1; t <= ct; t++)
	{
		printf("Case #%d: ", t);

		__main();

		printf("\n");
	}

	return 0;
}
