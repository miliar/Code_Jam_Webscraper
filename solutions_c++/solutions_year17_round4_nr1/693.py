#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>
#include <map>
using namespace std;
int a[100001] = {0};
int hash[101] = {0};
int main()
{
	int tt, tot;
	FILE *fp, *fo;
	fp = fopen("a1.in", "r");
	fo = fopen("a.out", "w");
	fscanf(fp, "%d", &tot);
	for (tt = 1; tt <= tot; tt++)
	{
		int n, m, ans = 0;
		fprintf(fo, "Case #%d: ", tt);
		fscanf(fp, "%d%d", &n, &m);

		for (int j = 0; j < 50; j++)
			hash[j] = 0;
		for (int i = 1; i <= n; i++)
		{
			fscanf(fp, "%d", &a[i]);
			a[i]%=m;
			hash[a[i]]++;
		}
		if (m == 4)
		{
		ans += hash[0];
		hash[0] = 0;
		
		ans += (hash[2]/2);
		int k = hash[2]/2;
		hash[2] -= k;
		
		int vmin = min(hash[1], hash[3]);
		ans += vmin;
		hash[1] -= vmin;
		hash[3] -= vmin;
		
		int remain = 0;
		if (hash[2])
		{
			ans += 1;
			hash[2] = 0;
			remain = 2;
		}
		
		while (hash[1] || hash[3])
		{
			int v;
			if (hash[1])
			{
				hash[1]--;
				v = 1;
			} else
			{
				hash[3]--;
				v = 3;
			}
			if (remain == 0)
				ans++;
			remain += v;
			remain %= m;
		}
		
		} else
		{
			ans += hash[0];
			hash[0] = 0;
			int vmin = min(hash[1], hash[2]);
			ans += vmin;
			hash[1] -= vmin;
			hash[2] -= vmin;
			int remain = 0;
			while (hash[1] || hash[2])
			{
				int v;
				if (hash[1]) v = 1;
				else v = 2;
				hash[v]--;
				if (remain == 0)
					ans++;
				remain += v;
				remain %= m;
			}
		}
		fprintf(fo, "%d\n", ans);
	}
	fclose(fp);
	fclose(fo);
	return 0;
} 
