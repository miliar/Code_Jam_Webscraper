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

int tt, n, tc, a[105];
char st[105];

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);

	scanf("%d", &tt);
	for (int gb = 1; gb <= tt; gb++)
	{
		scanf("%s", st);
		n = strlen(st);
		for (int i = 0; i < n; i++) a[i] = st[i] - 48;
		for (int i = 1; i < n; i++)
			if (a[i] < a[i - 1])
			{
				int ic = i - 1;
				while ((ic > 0) && (a[ic - 1] == a[ic])) --ic;
				a[ic]--;
				for (int j = ic + 1; j < n; j++) a[j] = 9;
				break;
			}
		tc = 0;
		if (a[0] == 0) ++tc;
		printf("Case #%d: ", gb);
		for (int i = tc; i < n; i++) printf("%d", a[i]);
		printf("\n");
	}

	return 0;
}
