// q3.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <string>
#include <cstdint>
#include <vector>
#include <fstream>
#include <algorithm>
#include <iomanip>

using namespace std;

vector<double> solve(size_t N, size_t Q, vector<double>& distAble, vector<double>& speeds,
	vector<vector<double>>& D, vector<vector<size_t>>& P) {

	vector<vector<double>> shortestDist(N, vector<double>(N, DBL_MAX));
	for (size_t i = 0; i < N; i++) {
		for (size_t j = 0; j < N; j++) {
			if (i == j) {
				shortestDist[i][j] = 0;
			}
			else if (D[i][j] != -1) {
				shortestDist[i][j] = D[i][j];
			}
		}
	}

	for (size_t b = 0; b < N; b++) {
		for (size_t a = 0; a < N; a++) {
			for (size_t c = 0; c < N; c++) {
				// try to shorten from a to c through b
				if ((shortestDist[a][b] != DBL_MAX) && (shortestDist[b][c] != DBL_MAX)) {
					if (shortestDist[a][b] + shortestDist[b][c] < shortestDist[a][c]) {
						shortestDist[a][c] = shortestDist[a][b] + shortestDist[b][c];
					}
				}
			}
		}
	}

	vector<vector<double>> times(N, vector<double>(N, DBL_MAX));
	for (size_t i = 0; i < N; i++) {
		for (size_t j = 0; j < N; j++) {
			if (i == j) {
				times[i][j] = 0;
			}
			else if (shortestDist[i][j] != DBL_MAX && shortestDist[i][j] <= distAble[i]
				&& times[i][j] > shortestDist[i][j] / speeds[i]) {
				times[i][j] = shortestDist[i][j] / speeds[i];
			}
		}
	}

	for (size_t b = 0; b < N; b++) {
		for (size_t a = 0; a < N; a++) {
			for (size_t c = 0; c < N; c++) {
				// try to shorten from a to c through b
				if ((times[a][b] != DBL_MAX) && (times[b][c] != DBL_MAX)) {
					if (times[a][b] + times[b][c] < times[a][c]) {
						times[a][c] = times[a][b] + times[b][c];
					}
				}
			}
		}
	}

	vector<double> res;
	for (size_t i = 0; i < Q; i++) {
		res.push_back(times[P[i][0]][P[i][1]]);
	}
	return res;
}

int main()
{
	ifstream inFile;
	inFile.open("..\\..\\C-large.in");
	ofstream outFile;
	outFile.open("..\\..\\C-large.out");

	size_t T;
	inFile >> T;
	for (size_t i = 0; i < T; i++) {
		size_t N;
		size_t Q;
		inFile >> N;
		inFile >> Q;

		double Ei;
		double Si;
		vector<double> distAble;
		vector<double> speeds;
		for (size_t j = 0; j < N; j++) {
			inFile >> Ei; // distance horse can go
			inFile >> Si; // horse's speed
			distAble.push_back(Ei);
			speeds.push_back(Si);
		}

		vector<vector<double>> D; // distances
		double Djk;
		for (size_t j = 0; j < N; j++) {
			D.push_back(vector<double>());
			for (size_t k = 0; k < N; k++) {
				inFile >> Djk;
				D[j].push_back(Djk);
			}
		}

		vector<vector<size_t>> P; // delivaries
		size_t Uj;
		size_t Vj;
		for (size_t j = 0; j < Q; j++) {
			inFile >> Uj;
			inFile >> Vj;
			P.push_back(vector<size_t>());
			P[j].push_back(Uj - 1);
			P[j].push_back(Vj - 1);
		}

		vector<double> res = solve(N, Q, distAble, speeds, D, P);
		outFile << "Case #" << (i + 1) << ":";
		for (size_t j = 0; j < Q; j++) {
			outFile << std::fixed << std::setprecision(10) << " " << res[j];
		}
		outFile << endl;
	}

	outFile.close();
	inFile.close();
	return 0;
}