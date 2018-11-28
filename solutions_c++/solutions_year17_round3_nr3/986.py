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
typedef vector<double> vf;
typedef vector<vi64> vvi64;
typedef double ld;

int factorial(int n)
{
	if (n == 0)
		return 1;
	return n * factorial(n - 1);
}

int main() {
	FILE * pIn; FILE * pOut;
	pIn = fopen("C-small-1-attempt2.in", "r");
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
			double U;
			fscanf(pIn, "%lf", &U);
			vf P;
			P.assign(N, 0);
			for (int i = 0; i < N; i++) {
				fscanf(pIn, "%lf", &P[i]);
			}

			sort(P.begin(), P.begin() + N);
			int count = 0;
			for (int i = (N - K); i < (N-1); i++) {
				count++;
				double diff = P[i + 1] - P[i];
				if (diff*count <= U) {
					for (int j = (N - K); j < (i + 1); j++) {
						U = U - diff;
						P[j] = P[j] + diff;
					}
				}
				else {
					U = U / count;
					for (int j = (N - K); j < (i + 1); j++) {
						P[j] = P[j] + U;
					}
					U = 0;
					break;
				}
			}
			double out = 1;
			if (U > 0) {
				double part = U / K;
				for (int i = (N - K); i < N; i++) {
					P[i] = P[i] + part;
					if (P[i] > 1) {
						P[i] = 1;
					}
					out = out * P[i];
				}
			}
			else {
				for (int i = (N - K); i < N; i++) {
					out = out * P[i];
				}
			}
			if (out == 1) {
				fprintf(pOut, "%6f\n", out);
			}
			else {
				out = 1;
				vf Pinv; Pinv.assign(P.size(), 0);
				for (int i = 0; i < N; i++) {
					Pinv[i] = 1 - P[i];
				}
				if (K >= (N / 2)) {
					if (K == N) {
						for (int i = 0; i < N; i++) {
							out = out * P[i];
						}
						fprintf(pOut, "%6f\n", out);
					}
					else {
						for (int i = K; i < N; i++) {
							int fails = N - i;
							int multiplier = factorial(N) / (factorial(i)*factorial(N - i));
						}
					}
				}
				else {

				}
			}
		}
	}

	fclose(pIn);
	fclose(pOut);

	return 0;
}