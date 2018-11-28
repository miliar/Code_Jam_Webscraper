#include <cstdio>
#include <vector>
#include <tuple>
#include <queue>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	int Ac, Aj, st, ed;
	int Xc, Xj, ans;
	vector<pair<pair<int, int>, int>> vec;

	freopen("B-small-attempt0.in", "r", stdin);
	freopen("output-B-small.txt", "w", stdout);

	scanf("%d", &T);
	
	for(int test_case=1;test_case<=T;test_case++)
	{
		vec.clear();
		scanf("%d %d", &Ac, &Aj);

		if(Ac==0 && Aj==0)
		{
			printf("Case #%d: 2\n", test_case);
			continue;
		}

		ans = 1500;
		Xc = 720;
		for(int i=0;i<Ac;i++)
		{
			scanf("%d %d", &st, &ed);
			vec.push_back({{st, ed}, 1});
			Xc -= (ed-st);
		}

		Xj = 720;
		for(int i=0;i<Aj;i++)
		{
			scanf("%d %d", &st, &ed);
			vec.push_back({{st, ed}, 2});
			Xj -= (ed-st);
		}

		sort(vec.begin(), vec.end());

		if(vec[0].second == vec[Ac+Aj-1].second) // overnight possible
		{
			int Yc, Yj;
			vector<pair<pair<int, int>, int>> vec2;
			vec2.clear();
			vec2.assign(vec.begin(), vec.end());

			Yc = Xc; Yj = Xj;
			if(vec2[0].second==1)// 1 should work
			{
				if(Yc >= vec2[0].first.first + (1440 - vec2[Ac+Aj-1].first.second))
				{
					Yc -= vec2[0].first.first + (1440 - vec2[Ac+Aj-1].first.second);
					vec2[0].first.first = 0;
					vec2[Ac+Aj-1].first.second = 1440;
				}
			}
			else // 2 should work
			{
				if(Yj >= vec2[0].first.first + (1440 - vec2[Ac+Aj-1].first.second))
				{
					Yj -= vec2[0].first.first + (1440 - vec2[Ac+Aj-1].first.second);
					vec2[0].first.first = 0;
					vec2[Ac+Aj-1].first.second = 1440;
				}
			}
			while(Yc > 0)
			{
				int mini = 1441;
				int minIdx = -1;

				for(int i=0;i<Ac+Aj-1;i++)
				{
					if(vec2[i].second==1 && vec2[i].second == vec2[i+1].second)
					{
						if(vec2[i+1].first.first - vec2[i].first.second == 0)
							continue;

						if(vec2[i+1].first.first - vec2[i].first.second < mini)
						{
							mini = vec2[i+1].first.first - vec2[i].first.second;
							minIdx = i;
						}
					}
				}

				if(minIdx==-1 || mini > Yc) break;

				Yc -= mini;
				vec2[minIdx].first.second = vec2[minIdx+1].first.first;
			}

			while(Yj > 0)
			{
				int mini = 1441;
				int minIdx = -1;

				for(int i=0;i<Ac+Aj-1;i++)
				{
					if(vec2[i].second==2 && vec2[i].second == vec2[i+1].second)
					{
						if(vec2[i+1].first.first - vec2[i].first.second == 0)
							continue;

						if(vec2[i+1].first.first - vec2[i].first.second < mini)
						{
							mini = vec2[i+1].first.first - vec2[i].first.second;
							minIdx = i;
						}
					}
				}

				if(minIdx==-1 || mini > Yj) break;

				Yj -= mini;
				vec2[minIdx].first.second = vec2[minIdx+1].first.first;
			}

			int cnt = 0;
			for(int i=0;i<Ac+Aj-1;i++)
			{
				if(vec2[i].second != vec2[i+1].second)
					cnt += 1;
				else if(vec2[i].first.second < vec2[i+1].first.first)
					cnt += 2;
			}

			if(vec2[Ac+Aj-1].second != vec2[0].second)
				cnt += 1;
			else if(vec2[Ac+Aj-1].first.second != 1440 || vec2[0].first.first!=0)
				cnt += 2;

			ans = min(ans, cnt);
		}
		else
		{
			while(Xc > 0)
			{
				int mini = 1441;
				int minIdx = -1;

				for(int i=0;i<Ac+Aj-1;i++)
				{
					if(vec[i].second==1 && vec[i].second == vec[i+1].second)
					{
						if(vec[i+1].first.first - vec[i].first.second == 0)
							continue;

						if(vec[i+1].first.first - vec[i].first.second < mini)
						{
							mini = vec[i+1].first.first - vec[i].first.second;
							minIdx = i;
						}
					}
				}

				if(minIdx==-1 || mini > Xc) break;

				Xc -= mini;
				vec[minIdx].first.second = vec[minIdx+1].first.first;
			}

			while(Xj > 0)
			{
				int mini = 1441;
				int minIdx = -1;

				for(int i=0;i<Ac+Aj-1;i++)
				{
					if(vec[i].second==2 && vec[i].second == vec[i+1].second)
					{
						if(vec[i+1].first.first - vec[i].first.second == 0)
							continue;

						if(vec[i+1].first.first - vec[i].first.second < mini)
						{
							mini = vec[i+1].first.first - vec[i].first.second;
							minIdx = i;
						}
					}
				}

				if(minIdx==-1 || mini > Xj) break;

				Xj -= mini;
				vec[minIdx].first.second = vec[minIdx+1].first.first;
			}

			int cnt = 0;
			for(int i=0;i<Ac+Aj-1;i++)
			{
				if(vec[i].second != vec[i+1].second)
					cnt += 1;
				else if(vec[i].first.second < vec[i+1].first.first)
					cnt += 2;
			}

			if(vec[Ac+Aj-1].second != vec[0].second)
				cnt += 1;
			else if(vec[Ac+Aj-1].first.second != 1440 || vec[0].first.first!=0)
				cnt += 2;

			ans = min(ans, cnt);
		}

		printf("Case #%d: %d\n", test_case, ans);
	}


	return 0;
}