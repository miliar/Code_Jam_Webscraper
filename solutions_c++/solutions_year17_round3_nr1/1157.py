#include <iostream>
#include <tuple>
#include <sstream>
#include <vector>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <numeric>
#include <utility>
#include <complex>
#include <array>
#include <list>
#include <stack>
#include <valarray>

using namespace std;

const double PI = 3.1415926535;

typedef pair<int, int> pii;
typedef long long i64;
typedef vector<i64> vi64;
typedef pair<i64, i64> pi64;
typedef vector<int> vi;
typedef vector<char> vc;
typedef vector<vc> vvc;
typedef vector<pii> vpi;
typedef vector<pi64> vpi64;
typedef vector<vi> vvi;
typedef vector<double> vd;
typedef vector<vi64> vvi64;
typedef double ld;

int main() {
	FILE * pIn; FILE * pOut;
	pIn = fopen("A-large.in", "r");
	pOut = fopen("Results.txt", "w");


	if (!pIn) {
		cerr << "Error reading input file." << endl;
		return -1;
	}
	else if (!pOut) {
		cerr << "Error reading output file." << endl;
		return -1;
	}
	else {
		int t;
		fscanf(pIn, "%d", &t);
		for (int T = 0; T < t; T++) {
			fprintf(pOut, "Case #%d: ", T + 1);
			int N; int K;
			fscanf(pIn, "%d %d", &N, &K);
			vi64 R; vi64 H; vd A; vd A2; vd A3;
			R.assign(N, 0); H.assign(N, 0); A.assign(N, 0); A.assign(N, 0); A2.assign(N, 0); A3.assign(N, 0);
			for (int i = 0; i < N; i++) {
				fscanf(pIn, "%d %d", &R[i], &H[i]);
				A[i] = PI*pow(R[i],2) + 2 * PI*R[i] * H[i];
				A2[i] = PI*pow(R[i], 2);
				A3[i] = 2 * PI*R[i] * H[i];
			}
			i64 rmax = 0;
			ld Amax = 0;
			vi index;
			index.assign(K, -1);
			for (int i = 0; i < N; i++) {
				if (A[i] > Amax) {
					Amax = A[i];
					index[0] = i;
					rmax = R[i];
				}
			}
			ld Atotal = Amax; ld Anow = Amax;
			bool skip = false;
			i64 rnmax = rmax;
			for (int j = 1; j < K; j++) {
				for (int c = 0; c < N; c++) {
					for (int k = 0; k < j; k++) {
						if (c == index[k]) {
							skip = true;
						}
					}
					if (skip) {
						skip = false;
						continue;
					}
					else {
						if (R[c] > rmax) {
							Anow = Atotal + A3[c] + PI*pow(R[c], 2) - PI*pow(rmax, 2);
							if (Anow > Amax) {
								Amax = Anow;
								index[j] = c;
								rnmax = R[c];
							}
						}
						else {
							Anow = Atotal + A3[c];
							if (Anow > Amax) {
								Amax = Anow;
								index[j] = c;
								rnmax = rmax;
							}
						}
					}
				}
				rmax = rnmax;
				Atotal = Amax;
			}
			fprintf(pOut, "%6f\n", Atotal);
		}
	}

	fclose(pIn);
	fclose(pOut);

	return 0;
}