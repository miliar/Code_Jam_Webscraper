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
int vc[2001] = {0};
int vp[2001] = {0};
int n, c, m;
int calc(int vmid)
{
	int ans = 0;
	int vis[2001] = {0};
	int vz[2001] = {0};
	for (int i = 1; i <= n; i++)
		vz[i] = vmid;
	for (int i = 1; i <= m; i++)
		if (vz[vp[i]])
		{
			vz[vp[i]]--;
			vis[i] = 1;
		}
	for (int i = 1; i <= m; i++)
		if (vis[i] == 0)
		{
		//	if (vmid == 2)
		//	{
		//		printf("%d %d\n", vp[i], vc[i]);
		//		getchar();
		//	}
			int j = vp[i];
			while (vz[j] == 0 && j > 0) j--;
			if (j == 0)
				return -1;
			vz[j]--;
			ans++;
		}
	return ans;
}
int main()
{
	int tt, tot;
	FILE *fp, *fo;
	fp = fopen("b2.in", "r");
	fo = fopen("b2.out", "w");
	fscanf(fp, "%d", &tot);
	for (tt = 1; tt <= tot; tt++)
	{
		int vmax = 0;
		int num[2001] = {0};
		fprintf(fo, "Case #%d:", tt);
		fscanf(fp, "%d%d%d", &n, &c, &m);
		for (int i = 1; i <= m; i++)
		{
			fscanf(fp, "%d%d", &vp[i], &vc[i]);
			num[vc[i]]++;
			vmax = max(vmax, num[vc[i]]);
		}
	//	printf("%d\n", vmax);
	//	getchar();
		int ans1, ans2;
		int left = vmax, right = m;
		while (left < right)
		{
			int mid = (left+right)/2;
			if (calc(mid) >= 0)
				right = mid;
			else
				left = mid+1;
		}
		int ans = calc(left);
		fprintf(fo, " %d %d", left, ans);
		fprintf(fo, "\n");
	}
	fclose(fp);
	fclose(fo);
	return 0;
} 
