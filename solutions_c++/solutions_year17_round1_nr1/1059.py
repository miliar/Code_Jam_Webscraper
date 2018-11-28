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
struct st
{
	int vx;
	int vy;
}a[10001] = {0};
char hash[1001] = {0};
int output[51][51] = {0};
int main()
{
	int tt, tot;
	FILE *fp, *fo;
	fp = fopen("a.in", "r");
	fo = fopen("a.out", "w");
	fscanf(fp, "%d", &tot);
	for (tt = 1; tt <= tot; tt++)
	{
		int n, m, k = 0;
		memset(output, 0, sizeof(output));
		memset(hash, 0, sizeof(hash));
		fscanf(fp, "%d%d\n", &n, &m);
		for (int i = 0; i < n; i++){
			for (int j = 0; j < m; j++){
				char ch;
				do{
					fscanf(fp, "%c", &ch);
				}while ((ch < 'A' || ch > 'Z') && ch != '?');
				if (ch != '?')
				{
					hash[k] = ch;
					a[k].vx = i;
					a[k].vy = j;
					k++;
				}
			}
		}
	//	printf("%c%c%c", hash[0], hash[1], hash[2]);
	//	getchar();
		int index = 0, stx = 0, enx;
		while (index < k){
			int to_index = index;
			while (a[to_index].vx == a[index].vx && to_index < k)
				to_index++;
			to_index--;
			if (to_index + 1< k)
				enx = a[to_index + 1].vx;
			else
				enx = n;
			int vp, vi;
			
			if (to_index == index){
				vp = m;
				vi = -1;
			}else{
				vp = a[index+1].vy;
				vi = index + 1;
			}
			int nowx = index;
			for (int j = 0; j < m; j++)
			{
				if (j >= vp)
				{
					nowx = vi;
					vi++;
					if (vi > to_index)
						vp = m;
					else
						vp = a[vi].vy;
				}
				for (int i = stx; i < enx; i++)
					output[i][j] = nowx;
			}
			stx = enx;
			index = to_index + 1;
		}
		fprintf(fo, "Case #%d:\n", tt);
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
				fprintf(fo, "%c", hash[output[i][j]]);
			fprintf(fo, "\n");
		}
	}
	fclose(fp);
	fclose(fo);
	return 0;
} 
