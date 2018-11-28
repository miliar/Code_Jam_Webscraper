#include<stdio.h>
#include<string.h>
#include <algorithm>
#include<queue>
#include<string>
#include<math.h>
#include<vector>
#include <map>
#include <stack>
#include<set>

using namespace std;
pair<int, int> horse[1111];
int main() {
	int tc, t, i, j;
	FILE *fp1,*fp2;
	fp1= fopen("1.in", "r");
	fp2 = fopen("2.out","w");
	fscanf(fp1, "%d", &tc);
	for (t = 1; t <= tc; t++) {
		fprintf(fp2, "Case #%d: ", t);
		int l, n;
		fscanf(fp1, "%d %d", &l,&n);
		for (i = 0; i < n; i++)
			fscanf(fp1, "%d %d", &horse[i].first, &horse[i].second);
		sort(horse, horse + n);
		double dap = (double)(l-horse[n - 1].first)/horse[n-1].second;
		for (i = n - 2; i >= 0; i--) {
			dap = max(dap, (double)(l - horse[i].first) / horse[i].second);
		}
		fprintf(fp2, "%.6f\n", (double)l / dap);
	}
	fclose(fp1);
	fclose(fp2);
}


