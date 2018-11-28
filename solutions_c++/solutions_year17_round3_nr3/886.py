#include <iostream>
#include <fstream>
#include <algorithm>
#include <math.h>
#include <string>
#include <iomanip>
#include <vector>

using namespace std;

int main() {
	ofstream fout("probsmall.out");
	ifstream fin("probsmall.in");
	int T;
	fin >> T;
	for (int t = 0; t < T; t++) {
		int N, K;
		fin >> N >> K;
		double U;
		fin >> U;
		vector<double> prob;
		for (int n = 0; n < N; n++) {
			double temp;
			fin >> temp;
			prob.push_back(temp);
		}
		sort(prob.begin(), prob.end());
		prob.push_back(1);
		int i = 1;
		while (U > 0 && U > 0.00001L) {
			if (U < (prob[i] - prob[i - 1])*i){
				for (int j = 0; j < i; j++) {
					prob[j] += U / i;
				}
				U = 0;
			}
			else {
				U -= (prob[i] - prob[i - 1])*i;
				for (int j = 0; j < i; j++) {
					prob[j] = prob[i];
				}
			}
			i++;
		}
		double P = 1;
		for (int n = 0; n < N; n++) {
			P *= prob[n];
		}
		cout << "Case #" << t + 1 << ": " << setprecision(10) << fixed << P << endl;
		fout << "Case #" << t + 1 << ": " << setprecision(10) << fixed << P << endl;

	}
	system("pause");
}