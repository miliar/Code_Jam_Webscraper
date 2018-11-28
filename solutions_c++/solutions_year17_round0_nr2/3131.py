#define _CRT_SECURE_NO_WARNINGS
#include <iostream>

#include <stdio.h>
#include <string.h>
int a[10000];



int main() {
	FILE *in = fopen("input.txt", "r");
	FILE *out = fopen("output.txt", "w");
	int t;
	long long int c = 0;
	long long int c1;
	long long int c2;
	int p = 0;
	int flag = 0;
	int number=0;
	fscanf(in, "%d", &t);
	for (int T = 1; T <= t; T++) {
		flag = 0;
		fscanf(in, "%lld", &c);
		if (c / 10 == 0) {
			fprintf(out, "Case #%d: %d\n", T, c);
		}
		else {
				c1 = c;
				
				p = 0;
				while ((c1) != 0) {
					a[p] = c1 % 10;
					c1 /= 10;
					p++;
				}
				while (flag == 0) {
					flag = 1;
					for (int i = p - 2; i >= 0; i--) {

						if (a[i] < a[i + 1]) {
							a[i + 1] -= 1;
							for (int j = 0; j < i + 1; j++) {
								a[j] = 9;
							}
							flag = 0;
							
						}

					}
				}
				fprintf(out, "Case #%d: ", T );
				
				for (int i = p - 1; i >= 0; i--) {
					if (a[p - 1] == 0 && i==p-1) {
						continue;
					}fprintf(out, "%d", a[i]);
				}
				fprintf(out,"\n");
				//99999999

				//-1 <- -1

			
		}
	}






	return 0;
}