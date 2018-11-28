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


int __main()
{
	scanf("%d%d", &N, &P);

	int i, ans = 0, j;
	int Pnum[10] = { 0, };

	for (i = 0; i < N; i++) {
		scanf("%d", &G[i]);
		Pnum[Cal(G[i], P)]++;
	}

	ans += Pnum[0];

	if (P == 2) {
		ans += Pnum[1] / 2;
		if (Pnum[1] % 2 != 0) ans++;
	}
	else if (P == 3) {
		int tmp = MIN(Pnum[1], Pnum[2]);
		ans += tmp;
		Pnum[1] -= tmp;
		Pnum[2] -= tmp;
		if (Pnum[2] == 0) {
			ans += Pnum[1] / 3 + 1;
			if (Pnum[1] % 3 == 0) ans--;
		}
		else {
			ans += Pnum[2] / 3 + 1;
			if (Pnum[2] % 3 == 0) ans--;
		}
	}
	else {
		int tmp = MIN(Pnum[1], Pnum[3]);
		ans += tmp;
		Pnum[1] -= tmp;
		Pnum[3] -= tmp;
		ans += Pnum[2] / 2;
		Pnum[2] %= 2;

		if (Pnum[2] == 1) {
			if (Pnum[1] != 0) {
				if (Pnum[1] >= 2) {
					ans += 1;
					Pnum[2] = 0;
					Pnum[1] -= 2;
				}
			}
			else if (Pnum[3] != 0) {
				if (Pnum[3] >= 2) {
					ans += 1;
					Pnum[2] = 0;
					Pnum[3] -= 2;
				}
			}
		}

		ans += 1;
		ans += MAX(Pnum[1], Pnum[3]) / 3;
		if (MAX(Pnum[1], Pnum[3]) % 3 == 0) ans--;


	}

	printf("%d", ans);
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