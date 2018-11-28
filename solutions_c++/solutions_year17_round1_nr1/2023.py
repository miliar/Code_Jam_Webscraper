#include<stdio.h>
#include<string>
#define max 26
int main(void) {
	int T, R, C, flag;
	char hold, flag_first_row, flag_first_col;
	char hold_row[max];
	char arr[max][max];
	int frr[max];
	FILE *in = fopen("A-large.in","rb");
	FILE *out = fopen("result.txt", "wt");

	//scanf("%d", &T);
	fscanf(in, "%d", &T);

	for(int i = 0; i < T; i++) {
		//scanf("%d", &R);
		fscanf(in, "%d", &R);
		//scanf("%d", &C);
		fscanf(in, "%d", &C);

		for(int j = 0; j < R; j++) {
			flag = 0;
			//scanf("%s", arr[j]);
			fscanf(in, "%s", arr[j]);
			for(int k = 0; k < C; k++) {
				if(arr[j][k] != '?') {
					flag = 1;
				}
			}
			flag == 0 ? frr[j] = 0 : frr[j] = 1;
		}

		hold = '?';
		flag_first_row = 1;
		for(int j = 0; j < R; j++) {
			if(frr[j] == 0) {
				if(flag_first_row == 0) {
					strcpy(arr[j], hold_row);
				}
			}
			else {
				flag_first_col = 1;
				for(int k = 0; k < C; k++) {
					if(arr[j][k] == '?') {
						if(flag_first_col == 0) {
							arr[j][k] = hold;
						}
					}
					else {
						hold = arr[j][k];
						if(flag_first_col == 1) {
							for(int l = k-1; l >= 0; l--) {
								arr[j][l] = hold;
							}
							flag_first_col = 0;
						}
					}
				}
				strcpy(hold_row, arr[j]);
				if(flag_first_row == 1) {
					for(int k = j-1; k >= 0; k--) {
						strcpy(arr[k], hold_row);
					}
				}
				flag_first_row = 0;
			}
		}

		printf("Case #%d:\n", i+1);
		fprintf(out, "Case #%d:\n", i+1);

		for(int j = 0; j < R; j++) {
			printf("%s\n", arr[j]);
			fprintf(out, "%s\n", arr[j]);
		}
	}

	return 0;
}