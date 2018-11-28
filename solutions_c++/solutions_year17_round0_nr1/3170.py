#define _CRT_SECURE_NO_WARNINGS
#include <iostream>

#include <stdio.h>
#include <string.h>
char a[10000];



int main(){
	FILE *in = fopen("input.txt", "r");
	FILE *out = fopen("output.txt", "w");
	int t;
	fscanf(in,"%d", &t);

	for (int T = 1; T <= t; T++) {
		int k;
		fscanf(in,"%s %d", a,&k);
		
		int count=0;
		int l = strlen(a);
		for (int i = 0; i <= l-k; i++) {
			if (a[i] == '-') {
				for (int j = i; j < i + k; j++) {
					if (a[j] == '+') {
						a[j] = '-';
					}
					else {
						a[j] = '+';
					}
				}
				count++;
			}
		}
		int flag=0;
		for (int i = 0; i < l; i++) {
			if (a[i] == '-') {
				fprintf(out,"Case #%d: IMPOSSIBLE", T);
				flag = 1;
				break;

			}
		}
		if (flag == 0) {
			fprintf(out, "Case #%d: %d", T, count);
		}
		fprintf(out, "\n");
	}
	return 0;
}