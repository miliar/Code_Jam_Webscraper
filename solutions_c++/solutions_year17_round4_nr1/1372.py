#include <stdio.h>
#include <string>
#include <string.h>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

int g[110];
int N, P;

int b[10];
map<vector<int>, int> mp;

vector<int> v;
int s;

int gao()
{
	if (mp.count(v)) return mp[v];
	int bonus = (s % P == 0) ? 1 : 0;
	int ret = 0;
	for (int i = 1; i < P; i++)
	{
		if (v[i-1] > 0)
		{
			v[i-1] -= 1;
			s += i;
			int t = gao();
			v[i-1] += 1;
			s -= i;
			if (t > ret)
			{
				ret = t;
			}
		}
	}
	// for (int i = 1; i < P; i++)
	// {
	// 	printf("%d,", v[i-1]);
	// }
	//printf("%d\n", ret + bonus);
	return mp[v] = ret + bonus;
}


int main() {
	int cas;

	scanf("%d", &cas);
	for (int re = 1; re <= cas; re++)
	{	
		int ans = 0;
		scanf("%d%d", &N, &P);
		memset(b, 0, sizeof(b));
		for (int i = 0; i < N; i++)
		{
			scanf("%d", g + i);
			if (g[i] % P == 0)
			{
				ans++;
			}
			else
			{
				b[g[i] % P]++;
			}
		}
		mp.clear();
		vector<int> v0;

		for (int i = 1; i < P; i++)
		{
			v0.push_back(0);
		}
		mp[v0] = ans;

		v.clear();
		s = 0;
		for (int i = 1; i < P; i++)
		{
			v.push_back(b[i]);
		}

	// 		for (int i = 1; i < P; i++)
	// {
	// 	printf("%d,", v[i-1]);
	// }
	// puts("");

		ans = gao();
		printf("Case #%d: %d\n", re, ans);
	}
}