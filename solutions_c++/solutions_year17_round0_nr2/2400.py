#include<cstdio>
#include<cstring>

FILE *out = fopen("output.txt", "w");
FILE *in = fopen("input.txt", "r");



int main() {
	

	int tc;
	fscanf(in, "%d", &tc);

	for(int tt=1;tt<=tc;tt++){
		long long cnt = 0;
		char str[100];
		int maxnum[100];
		fscanf(in,"%s", str);
		int len = strlen(str);
	

		for (int i = len - 2; i >= 0; i--) {
			if (str[i] > str[i + 1]) {
				str[i] --;
				for (int j = i+1; j < len; j++) {
					str[j] = '9';
				}
			}
		}
		int flag = 0;
		fprintf(out , "Case #%d: ", tt);
		for (int i = 0; i < len; i++) {
			if (str[i] <= '0' && flag == 0) {
				continue;
			}
			else {
				flag = 1;
				fprintf(out,"%c", str[i]);
			}
		}
		fprintf(out,"\n");

	}
	return 0;
}