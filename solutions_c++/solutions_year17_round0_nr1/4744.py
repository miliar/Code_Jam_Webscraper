#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <string>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <set>
#include <utility>
#include <vector>
#include <queue>

using namespace std;

typedef pair<int,int> PII;
typedef pair<int,PII> PIII;

#define LL long long
#define ULL unsigned long long
#define m_p make_pair
#define l_b lower_bound
#define p_b push_back
#define w1 first
#define w2 second
#define maxlongint 2147483647
#define biglongint 2139062143

int tt, n, k, ans, flag;
int a[1005];
char st[1005];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);

	scanf("%d", &tt);
	for (int gb = 1; gb <= tt; gb++)
	{
		scanf("%s %d\n", st, &k);
		n = strlen(st);
		memset(a, 0, sizeof(a));
		for (int i = 0; i < n; i++)
			if (st[i] == '+') a[i] = 1; else a[i] = -1;
		ans = 0;
		for (int i = 0; i < n - k + 1; i++)
			if (a[i] == -1)
			{
				ans++;
				for (int j = i; j <= i + k - 1; j++)
					a[j] *= -1;
			}
		flag = 1;
		for (int i = 0; i < n; i++)
			if (a[i] == -1) flag = 0;
		printf("Case #%d: ", gb);
		if (flag == 0) printf("IMPOSSIBLE\n"); else printf("%d\n", ans);
	}

	return 0;
}
