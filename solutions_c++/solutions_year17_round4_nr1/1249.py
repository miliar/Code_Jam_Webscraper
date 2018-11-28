#include <string.h>
#include<math.h>
#include<stdio.h>
#include<algorithm>
#include<vector>
#include<map>
#include<string>
#include<iostream>
#include<set>
#include<stack>
#include<queue>
#include<functional>
using namespace std;

int a[111];
int p[6];
int main()
{
	int tc, t, i, j;
	FILE *fp1, *fp2;
	fp1 = fopen("1.in", "r");
	fp2 = fopen("2.out", "w");
	fscanf(fp1, "%d", &tc);
	for (t = 1; t <= tc; t++) {
		memset(p, 0, sizeof(p));
		fprintf(fp2, "Case #%d: ", t);
		int n, k; fscanf(fp1, "%d%d", &n, &k);
		for (i = 1; i <= n; i++) {
			fscanf(fp1, "%d", &a[i]);
			p[a[i] % k]++;
		}
		int dap = 0;
		if (k == 2) {
			dap = (p[1] + 1) / 2 + p[0];
		}
		else if (k == 3) {
			int mx = max(p[1], p[2]);
			int mn = min(p[1], p[2]);
			dap = mn + p[0]+(mx-mn+2)/3;
		}
		else if(k==4){
			int mx = max(p[1], p[3]);
			int mn = min(p[1], p[3]);
			
			dap = mn + p[0] + (mx - mn)/4+p[2]/2;
			if (p[2] % 2 == 0) {
				if ((mx - mn) % 4 != 0)
					dap++;
			}
			else {
				dap++;
				if ((mx - mn) % 4 == 3)
					dap++;
			}
			
		}
		fprintf(fp2, "%d\n", dap);
	}
	fclose(fp1);
	fclose(fp2);
}