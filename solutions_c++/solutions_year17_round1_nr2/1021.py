#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <tuple>

using namespace std;

int N, P;
int R[52];
vector<pair<int,int>> Q;
int cnt[52], cc;
int used[52];

int main()
{
	int T;
	freopen("B-large.in", "r", stdin);
	freopen("output_B_large.txt", "w", stdout);

	scanf("%d", &T);

	for(int test_case=1;test_case<=T;test_case++)
	{
		scanf("%d %d", &N, &P);
		for(int i=1;i<=N;i++)
			scanf("%d", &R[i]);

		Q.clear();
		for(int i=1;i<=N;i++)
		{
			for(int j=1;j<=P;j++)
			{
				double t;
				scanf("%lf", &t);
				int in = (int)(ceil(t/(R[i]*1.1)));
				int out = (int)(floor(t/(R[i]*0.9)));

				if(in<=out)
				{
					Q.push_back({in, -i});
					Q.push_back({out, i});
				}
			}
		}

		sort(Q.begin(), Q.end());

		cc = 0;
		for(int i=1;i<=N;i++) cnt[i] = used[i] = 0;

		int ans = 0;
		for(auto pp : Q)
		{
			int a = pp.second;

			if(a<0)
			{
				if(cnt[-a]>=1) cnt[-a]++;
				else
				{
					cnt[-a]++;
					cc++;

					if(cc==N)
					{
						cc = 0;
						ans++;
						for(int i=1;i<=N;i++)
						{
							used[i]++;
							cnt[i]--;
							if(cnt[i]>0) cc++;
						}
					}
				}
			}
			else
			{
				if(used[a]>0) used[a]--;
				else
				{
					if(cnt[a]>=2) cnt[a]--;
					else
					{
						cnt[a]--;
						cc--;
					}
				}
			}
		}

		printf("Case #%d: %d\n", test_case, ans);
	}

	return 0;
}