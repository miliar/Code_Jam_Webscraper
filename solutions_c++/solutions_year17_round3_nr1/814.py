#include <cstdio>
#include <vector>
#include <tuple>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	int N, K;
	int r, h, cnt;
	double area, ans;

	const double PI = 3.14159265358979;
	vector<pair<double, int>> pan;

	freopen("A-large.in", "r", stdin);
	freopen("output-A-large.txt", "w", stdout);

	scanf("%d", &T);

	
	for(int test_case=1;test_case<=T;test_case++)
	{
		pan.clear();
		scanf("%d %d", &N, &K);

		for(int i=0;i<N;i++)
		{
			scanf("%d %d", &r, &h);
			area = ((2*PI)*r)*h;
			pan.push_back({area, r});
		}
		sort(pan.begin(), pan.end());
		reverse(pan.begin(), pan.end());

		ans = 0;
		for(int i=0;i<N;i++)
		{
			area = (PI * pan[i].second) * pan[i].second + pan[i].first;
			cnt = 1;

			for(int j=0;j<N;j++)
			{
				if(i==j) continue;

				if(cnt<K && pan[j].second <= pan[i].second)
				{
					area += pan[j].first;
					cnt++;
				}
			}

			if(cnt<K) continue;

			ans = max(ans, area);
		}

		printf("Case #%d: %.9lf\n", test_case, ans);
	}


	return 0;
}