#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B_large_out.txt", "w", stdout);
	int T; 
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t)
	{
		long long N;
		scanf("%lld", &N);
		vector<int> v;
		long long tmp = N;
		while (tmp)
		{
			v.push_back(tmp % 10);
			tmp /= 10;
		}
		reverse(v.begin(), v.end());
		bool isascending = true;
		int idx = 0;
		for (int i = 0; i < v.size() - 1; ++i)
			if (v[i] > v[i + 1])
			{
				isascending = false;
				idx = i;
				break;
			}
		if (isascending == false)
		{
			int idx2 = 0;
			for (int i = 0; i < v.size(); ++i)
				if (v[i] == v[idx])
				{
					idx2 = i;
					break;
				}
			v[idx2] -= 1;
			for (int i = idx2 + 1; i < v.size(); ++i)
				v[i] = 9;
			long long ans = v[0];
			for (int i = 1; i < v.size(); ++i)
			{
				ans *= 10;
				ans += v[i];
			}
			printf("Case #%d: %lld\n", t, ans);
		}
		else
			printf("Case #%d: %lld\n", t, N);
	}
}