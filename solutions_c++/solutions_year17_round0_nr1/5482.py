#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>

int T;
int K;

FILE *fin, *fout;

int main(void) {
	fin = fopen("test.in", "r");
	fout = fopen("test.out", "w");

	fscanf(fin, "%d", &T);
	for (int i = 0; i < T; i++) {
		std::string seq = "";
		while(true) {
			char ch;
			fscanf(fin, "%c", &ch);
			if (ch == ' ') break;
			if (ch == '+') {
				seq+="+";
			}
			else if (ch == '-') {
				seq+="-";
			}
		}

		fscanf(fin, "%d", &K);

		int times = 0;
		bool complete = true;
		while(true) {
			printf("%s\n", seq.c_str());
			int startIndex = 0;
			for (startIndex = 0; startIndex < seq.length(); startIndex++) {
				if (seq[startIndex] == '-') {
					break;
				}
			}

			seq = seq.substr(startIndex,seq.length());
			if(seq.length() == 0) {
				break;
			}

			if (seq.length() > 0 && seq.length() < K){
				complete = false;
				break;
			}

			for (int j = 0; j < K; j++) {
				if (seq[j] == '-') {
					seq[j] = '+';
				}
				else {
					seq[j] = '-';
				}
			}
			times++;

		}

		if(complete) {
			fprintf(fout, "Case #%d: %d\n", i+1, times);
		}
		else {
			fprintf(fout, "Case #%d: IMPOSSIBLE\n", i+1);
		}
	}
}