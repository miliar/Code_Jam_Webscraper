#include<stdio.h>
#include<algorithm>
using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
	int t, T;
	int n, m, i, j, k, p, q, bloop;
	int A[3], B[3], C, ans;
	pair<int, pair<int, int> > a[404];
	pair<int, int> b[404];
	while (~scanf("%d", &T))
	{
		for (t = 1; t <= T; ++t)
		{
			scanf("%d %d", &n, &m);
			A[1] = 0; A[2] = 0; B[1] = 0; B[2] = 0; C = 0; ans = 0;
			for (i = 0, j = 0; i<n; ++i)
			{
				scanf("%d %d", &p, &q);
				a[j].first = p;
				a[j].second.first = q;
				a[j++].second.second = 1;
				A[1] += q - p;
			}
			for (i = 0; i<m; ++i)
			{
				scanf("%d %d", &p, &q);
				a[j].first = p;
				a[j].second.first = q;
				a[j++].second.second = 2;
				A[2] += q - p;
			}
			sort(a, a + n + m);

			for (i = 0, bloop = 0, k = 0; k<1; i = (i + 1) % (n + m))
			{
				int M = 1440;
				j = (i + 1) % (n + m);
				if (a[i].second.second == a[j].second.second)
				{
					b[bloop].first = a[i].second.second;
					b[bloop++].second = (a[j].first - a[i].second.first + M) % M;
					B[a[i].second.second] += (a[j].first - a[i].second.first + M) % M;
				}
				else
				{
					C += (a[j].first - a[i].second.first + M) % M;
					ans++;
				}
				if (i == n + m-1) { k++; }
			}

			sort(b, b + bloop);

			if ((A[1] + B[1]>A[2] + B[2] + C) || (A[1] + B[1] + C<A[2] + B[2]))
			{
				if ((A[1] + B[1]>A[2] + B[2] + C))
				{
					for (i = 0; i<bloop&&b[i].first == 1; ++i); --i;
					for (j = i; j>=0; --j)
					{
						if (A[1] + B[1] > A[2] + B[2] + C)
						{
							C += b[j].second;
							B[1] -= b[j].second;
							ans += 2;
							if (A[1] + B[1] <= A[2] + B[2] + C)break;
						}
					}
				}
				else
				{
					i = bloop - 1;
					for (j = i; j>=0 && b[j].first == 2; --j)
					{
						if (A[1] + B[1] + C < A[2] + B[2])
						{
							C += b[j].second;
							B[2] -= b[j].second;
							ans += 2;
							if (A[1] + B[1] + C >= A[2] + B[2])break;
						}
					}
				}
			}
			printf("Case #%d: %d\n", t, ans);
		}
	}
	return 0;
}
