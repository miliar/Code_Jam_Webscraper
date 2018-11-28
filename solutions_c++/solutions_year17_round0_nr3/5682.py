#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <queue>

FILE *fin, *fout;

int T;
unsigned long long N, K;

int main(void) {
	fin = fopen("test.in", "r");
	fout = fopen("test.out", "w");

	fscanf(fin, "%d", &T);

	for (int i = 0; i < T; i++) {
		fscanf(fin, "%llu", &N);
		fscanf(fin, "%llu", &K);
		unsigned long long ls = 0;
		unsigned long long rs = 0;
		std::vector<unsigned long long> avals;
		avals.push_back(N);
		for (int j = 0; j < K; j++) {
			if (avals.empty())break;
			unsigned long long selected = avals.at(avals.size()-1);
			avals.pop_back();
			if (selected == 0) {
				break;
			}
			unsigned long long pivot;
			if (selected%2) {
				pivot = selected/2+1;
			}
			else {
				pivot = selected/2;
			}

			unsigned long long tmpLs = pivot-1;
			unsigned long long tmpRs = selected-pivot;
			ls = tmpLs > tmpRs?tmpLs:tmpRs;
			rs = tmpLs < tmpRs?tmpLs:tmpRs;

			avals.push_back(ls);
			for (int k = avals.size()-1; k >= 0; k--) {
				if (k-1 >= 0 && avals.at(k) < avals.at(k-1)) {
					unsigned long long tmp = avals.at(k-1);
					avals.at(k-1) = avals.at(k);
					avals.at(k) = tmp;
				}
			}
			avals.push_back(rs);
			for (int k = avals.size()-1; k >= 0; k--) {
				if (k-1 >= 0 && avals.at(k) < avals.at(k-1)) {
					unsigned long long tmp = avals.at(k-1);
					avals.at(k-1) = avals.at(k);
					avals.at(k) = tmp;
				}
			}
		}

		fprintf(fout, "Case #%d: %llu %llu\n", i+1, ls, rs);
	}
}