#include<cstdio>
#include<cstring>

FILE *in = fopen("input.txt", "r");
FILE *out = fopen("output.txt", "w");




int main() {
	int tc;
	fscanf(in, "%d", &tc);

	for(int tt=1;tt<=tc;tt++){
		char str[2005];
		int K;
		fscanf(in, "%s %d", str, &K);

		int len = strlen(str);
		int cnt = 0;
		
		for (int i = 0; i < len; i++) {
			if (i + K > len)break;
			if (str[i] == '-') {
				for (int j = 0; j < K; j++) {
					if (str[i + j] == '-')str[i+j] = '+';
					else str[i+j] = '-';
				}
				cnt++;

			}
		}
		int flag = 0;
		for (int i = 0; i < len; i++) {
			if (str[i] == '-')flag = 1;
		}

		if (flag == 0)fprintf(out,"Case #%d: %d\n", tt, cnt);
		else fprintf(out,"Case #%d: IMPOSSIBLE\n", tt);



	}
	return 0;
}