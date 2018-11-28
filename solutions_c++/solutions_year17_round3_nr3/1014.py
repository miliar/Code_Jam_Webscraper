#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>
using namespace std;

double g[100];

int main() {
	ifstream ifs;
	ofstream ofs;
	ifs.open("c.in");
	ofs.open("c.out");

	int T;
	ifs >> T;
	for (int ca = 1; ca <= T; ++ca) {
		int N, K;
		ifs >> N >> K;
		double xx;
		ifs >> xx;
		for (int i = 0; i < N; ++i) {
			ifs >> g[i];
		}
		sort(g, g + N);
		double ans = 0.0;
		double sum = 0;
		for (int i = 0; i < N; ++i) {
			sum += g[i];
			double tmp = (sum + xx) / (i + 1);
			if (tmp < g[i])
				break;
			double tmpAns = 1.0;
			for (int j = 0; j <= i; ++j) {
				tmpAns *= tmp;
			}
			for (int j = i + 1; j < N; ++j) {
				tmpAns *= g[j];
			}
			ans = max(ans, tmpAns);

		}
		ofs << "Case #" << ca << ": " << ans << endl; 
	}
	return 0;
}
