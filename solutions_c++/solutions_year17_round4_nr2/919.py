#define _CRT_SECURE_NO_WARNINGS

#include <set>
#include <map>
#include <cmath>
#include <ctime>
#include <queue>
#include <string>
#include <cstdio>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>


using namespace std;


bool edge[1001][1001];
int match[2000];
int check[2000];

bool find(int u, int M)
{
	for (int i = 0; i < M; i++)
	{
		if (edge[u][i] && !check[i])
		{
			check[i] = 1;
			if (match[i] == -1 || find(match[i], M))
			{
				match[i] = u;
				return true;
			}
		}
	}
	return false;
}

void Solve()
{
	int N, C, M;
	scanf("%d %d %d", &N, &C, &M);

	int a[2000][2];
	int z[2] = { 0 };
	int cnt[2] = { 0 };
	for (int m = 0; m < M; ++m){
		scanf("%d %d", a[m], a[m] + 1);
		if (a[m][0] == 1){
			z[a[m][1] - 1]++;
		}
		cnt[a[m][1] - 1]++;
	}



	int min_cart = z[0] + z[1] + max(max(0, (cnt[0] - z[1] - z[0])), max(0, (cnt[1] - z[1] - z[0])));


	for (int i = 0; i < M; ++i){
		for (int j = 0; j < M; ++j){
			
			if (a[i][0] != a[j][0] && a[i][1] == 1 && a[j][1] == 2){
				edge[i][j] = true;
			}
			else{
				edge[i][j] = false;
			}
		}
	}

	memset(match, 255, sizeof(match));

	printf("%d ", min_cart);

	int total_match = 0;
	for (int i = 0; i < M; i++)
	{
		memset(check, 0, sizeof(check));
		if (find(i, M))
			total_match++;
	}

	printf("%d\n", cnt[0] + cnt[1] - total_match - min_cart);
}

int main()
{
	int T;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d\n", &T);
	for (int i = 0; i < T; i++)
	{
		printf("Case #%d: ", i + 1);
		Solve();
	}
}