#include <stdio.h>
#include <string.h>
#include <stdlib.h>

FILE*fin, *fout;
int T;
char buffer[20];
int N[20];

int main(void) {
	fin = fopen("test.in", "r");
	fout = fopen("test.out", "w");

	fscanf(fin, "%d", &T);

	char enter;
	fscanf(fin, "%c", &enter);
	for (int i = 0; i < T; i++) {
		int digit = 0;
		fgets(buffer, 20, fin);

		while(buffer[digit]!='\n' &&buffer[digit]!='\0') {
			digit++;
		}

		for (int j = 0; j < digit; j++) {
			N[j] = buffer[j] - '0';
		}

		if (digit >1) {
			while(true) {
				bool adjust = false;
				for(int j = 0; j < digit; j++) {
					if (j+1 < digit && N[j] > N[j+1]) {
						adjust = true;
						N[j]--;
						for (int k = j+1; k< digit; k++) {
							N[k] = 9;
						}
						break;
					}
				}
				if (!adjust) break;
			}
		}

		fprintf(fout, "Case #%d: ", i+1);
		int startIndex = 0;
		for (startIndex = 0; startIndex< digit; startIndex++) {
			if (N[startIndex]!=0) {
				break;
			}
		}
		for (int j = startIndex; j < digit; j++) {
			fprintf(fout, "%d", N[j]);
		}

		fprintf(fout, "\n");
	}

}