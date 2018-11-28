#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>
#include <map>
#define eps 1e-9
using namespace std;
int a[1001] = {0};
int sta[1001] = {0};
int ena[1001] = {0};

class st
{
	public:
	//	bool operator < (const st& y);
	int st;
	int en;
}b[101][101];
bool operator<(const st &x, const st &y)
{
		if (x.en < y.en)
			return true;
		else
			if (x.en > y.en)
				return false;
			else
				if (x.st < y.st)
					return false;
				else
					return true;
}

int bl[101] = {0};
int main()
{
	int tt, tot;
	FILE *fp, *fo;
	fp = fopen("b.in", "r");
	fo = fopen("b.out", "w");
	fscanf(fp, "%d", &tot);
	for (tt = 1; tt <= tot; tt++)
	{
		int n, m;
		fscanf(fp, "%d%d", &n, &m);
		for (int i = 0; i < n; i++)
		{
			fscanf(fp, "%d", &a[i]);
		}
		memset(bl, 0, sizeof(bl));
		printf("%d %d\n", n, m);
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				int vk = 0;
				fscanf(fp, "%d", &vk);
				double svmax = (vk / (1.0 * a[i] * 0.9));
				double svmin = (vk / (1.0 * a[i] * 1.1));
				int vmax = (int)(eps+svmax), vmin = (int)(svmin+eps);
				int vst, ven;
			//	printf("%lf|%lf\n", svmax, svmin);
			//	getchar();
				if (1.0 * vmax * a[i] * 0.9 > vk+eps)
					vmax--;
				if (1.0 * vmin * a[i] * 1.1 < vk-eps)
					vmin++;
			//	printf("%d|%d\n", vmax, vmin);
			//	getchar();
				if (vmax >= vmin)
				{
					b[i][bl[i]].st = vmin;
					b[i][bl[i]].en = vmax;
					bl[i]++;
				}
			}
			sort(b[i], b[i]+bl[i]);
		//	for (int j = 0; j < bl[i]; j++)
		//		printf("%d %d, ", b[i][j].st, b[i][j].en);
		//	printf("\n");
		//	getchar();
		}
		int stx[101] = {0};
		int hash[101][101] = {0};
		int ans = 0;
		for (int i = 0; i < bl[0]; i++)
		{
			int flag = 0;
			for (int j = 1; j < n; j++)
			{
				for (int k = 0; k < bl[j]; k++)
					if (hash[j][k] == 0 && b[0][i].st <= b[j][k].en && b[0][i].en >= b[j][k].st)
					{
						 flag++;
						 break;
					}
			}
			if (flag == n-1)
			{
				ans++;
				for (int j = 1; j < n; j++) 
				for (int k = 0; k < bl[j]; k++)
					if (hash[j][k] == 0 && b[0][i].st <= b[j][k].en && b[0][i].en >= b[j][k].st)
					{
						 hash[j][k] = 1;
						 break;
					}
			}
		}
		fprintf(fo, "Case #%d: %d\n", tt, ans);
	}
	fclose(fp);
	fclose(fo);
	return 0;
} 
