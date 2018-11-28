#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>
#include <map>
int a[100001] = {0};
int s[100001] = {0};
using namespace std;
int main()
{
	int tt, tot;
	FILE *fp, *fo;
	fp = fopen("a.in", "r");
	fo = fopen("a.out", "w");
	fscanf(fp, "%d", &tot);
	for (tt = 1; tt <= tot; tt++)
	{
		int n, d;
		fscanf(fp, "%d%d", &d, &n);
		double maxtime = 0;
		for (int i = 1; i <= n; i++)
		{
			fscanf(fp,"%d%d", &a[i], &s[i]);
			maxtime = max(maxtime, (d-a[i])*1.0/(s[i]*1.0));
		}
		double ans = d*1.0/maxtime;
		
		fprintf(fo, "Case #%d: %.6lf\n", tt, ans);
	}
	fclose(fp);
	fclose(fo);
	return 0;
} 
