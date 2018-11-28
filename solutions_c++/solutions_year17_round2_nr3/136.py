#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cassert>
#include <iomanip>
#include <algorithm>
using namespace std;

using ll = long long int;
ifstream fin("3.in");
ofstream fout("3.out");

int E[100], S[100], U[100], V[100], N, Q;
double D[100][100];
const double inf = numeric_limits<double>::infinity();

void fw() {
	for (int i = 0; i < N; i++)
		D[i][i] = 0;
	for (int k = 0; k < N; k++)
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
				D[i][j] = min(D[i][j], D[i][k] + D[k][j]);
}

int main() {
	int T;
	fin >> T;
	for (int t = 1; t <= T; t++) {
		fout << "Case #" << t << ": ";
		fin >> N >> Q;
		for (int i = 0; i < N; i++)
			fin >> E[i] >> S[i];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				fin >> D[i][j];
				if (D[i][j] == -1)
					D[i][j] = inf;
			}
		}
		for (int i = 0; i < Q; i++) {
			fin >> U[i] >> V[i];
			U[i]--; V[i]--;
		}

		fw();

		for (int src = 0; src < N; src++) {
			for (int dst = 0; dst < N; dst++) {
				if (E[src] >= D[src][dst])
					D[src][dst] = D[src][dst] / S[src];
				else
					D[src][dst] = inf;
			}
		}

		fw();

		for (int i = 0; i < Q; i++)
			fout << std::setprecision(9) << D[U[i]][V[i]] << ' ';
		fout << endl;
	}
}
