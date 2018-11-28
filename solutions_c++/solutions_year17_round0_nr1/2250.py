#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("g_output_large.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t)
	{
		char str[1002];
		vector<int> v;
		vector<int> v2;
		int K;
		scanf("%s %d", str, &K);

		for (int i = 0; str[i]; ++i)
		{
			if (str[i] == '+')
			{
				v.push_back(1);
				v2.push_back(1);
			}
			else
			{
				v.push_back(0);
				v2.push_back(0);
			}
		}
		reverse(v2.begin(), v2.end());
		int cnt = 0;
		int cnt2 = 0;
		for (int i = 0; i <= v.size() - K; ++i)
		{
			if (v[i] == 0)
			{
				for (int j = 0; j < K; ++j)
					v[i + j] ^= 1;
				cnt++;
			}
			if (v2[i] == 0)
			{
				for (int j = 0; j < K; ++j)
					v2[i + j] ^= 1;
				cnt2++;
			}
		}
		bool isPossible = true;
		for (int i = 0; i < v.size(); ++i)
			if (v[i] == 0)
				isPossible = false;

		for (int i = 0; i < v.size(); ++i)
			if (v2[i] == 0)
				isPossible = false;
		if(isPossible)
			printf("Case #%d: %d\n", t, min(cnt, cnt2));
		else
			printf("Case #%d: IMPOSSIBLE\n", t);
	}
}