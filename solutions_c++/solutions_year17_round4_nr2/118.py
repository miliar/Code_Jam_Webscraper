#include<stdio.h>
#include<vector>
#include<algorithm>
#include<queue>
using namespace std;
int deg[1000];
int dat[1000];
int get(int med, int num)
{
	int now = 0, ans = num;
	for (int i = 999; i >= 0; i--)
	{
		now += dat[i];
		ans -= min(dat[i], med);
		now = max(0, dat[i] - med);
	}
	if (now != 0)return -1;
	else return ans;
}
int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("outs.txt", "wb", stdout);
	int data;
	scanf("%d", &data);
	for (int p = 1; p <= data; p++)
	{
		int len, css, num;
		scanf("%d%d%d", &len, &css, &num);
		fill(deg, deg + 1000, 0);
		fill(dat, dat + 1000, 0);
		for (int i = 0; i < num; i++)
		{
			int za, zb;
			scanf("%d%d", &za, &zb);
			za--, zb--;
			deg[zb]++;
			dat[za]++;
		}
		int maxi = 0;
		for (int i = 0; i < css; i++)maxi = max(maxi, deg[i]);
		int beg = maxi, end = 2000;
		for (;;)
		{
			if (beg == end)break;
			int med = (beg + end) / 2;
			if (get(med, num) == -1)beg = med + 1;
			else end = med;
		}
		printf("Case #%d: %d %d\n", p, beg, get(beg, num));
	}
}