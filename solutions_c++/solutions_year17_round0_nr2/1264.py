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
char a[22];

int same[22];
int big[22];
int small[22];
int l;

int main() {
	int tc, t, i, j;
	FILE *fp1,*fp2;
	fp1= fopen("1.in", "r");
	fp2 = fopen("2.out","w");
	fscanf(fp1, "%d", &tc);
	for (t = 1; t <= tc; t++) {
		memset(same, 0, sizeof(same));
		memset(big, 0, sizeof(big));
		memset(small, 0, sizeof(small));
		fscanf(fp1,"%s", a);
		fprintf(fp2,"Case #%d: ", t);
		l = strlen(a);

		for (i = 1; i < l; i++) {
			if (a[i - 1] == a[i])
				same[i] = 1;
			else if (a[i - 1] < a[i])
				big[i] = 1;
			else
				small[i] = 1;
		}

		if (l == 1) {
			fprintf(fp2,"%c", a[0]);
		}
		else {
			for (i = 1; i < l; i++) {
				if (small[i])
					break;
			}
			if (i == l)
				fprintf(fp2,"%s", a);
			else {
				if (a[0] == '1') {
					int check = 0, place = 0;
					for (i = 1; i < l; i++) {
						if (same[i]) {
							continue;
						}
						else if (big[i]) {
							check = 1;
							break;
						}
						else {
							check = -1;
							break;
						}
					}
					if (check == 0) {
						fprintf(fp2,"%s", a);
					}
					else if (check == -1) {
						for (i = 0; i < l - 1; i++)
							fprintf(fp2,"9");
					}
					else {
						int cur = 1;
						while (!small[cur] && cur < l) {
							cur++;
						}
						int when = cur;
						while (!big[when] && when >= 0) {
							when--;
						}
						for (i = 0; i < when; i++)
							fprintf(fp2,"%c", a[i]);
						fprintf(fp2,"%c", a[when] - 1);
						for (i = when + 1; i < l; i++)
							fprintf(fp2,"9");
					}
				}
				else {
					int check = 0, place = 0;
					for (i = 1; i < l; i++) {
						if (same[i]) {
							continue;
						}
						else if (big[i]) {
							check = 1;
							break;
						}
						else {
							check = -1;
							break;
						}
					}
					if (check == 0) {
						fprintf(fp2,"%s", a);
					}
					else if (check == -1) {
						fprintf(fp2,"%c", a[0] - 1);
						for (i = 0; i < l - 1; i++)
							fprintf(fp2,"9");
					}
					else {
						int cur = 1;
						while (!small[cur] && cur < l) {
							cur++;
						}
						int when = cur;
						while (!big[when] && when >= 0) {
							when--;
						}
						for (i = 0; i < when; i++)
							fprintf(fp2,"%c", a[i]);
						fprintf(fp2,"%c", a[when] - 1);
						for (i = when + 1; i < l; i++)
							fprintf(fp2,"9");
					}
				}
			}
		}
		fprintf(fp2,"\n");
	}
	fclose(fp1);
	fclose(fp2);
}


