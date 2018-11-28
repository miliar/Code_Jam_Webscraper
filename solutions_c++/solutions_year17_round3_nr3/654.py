#include <iostream>
#include <string>
#include <vector>
#include <iomanip>
#include <utility>
#include <algorithm>

#define PI 3.1415926535

using namespace std;

int main() {
	int T;
	cin >> T;
	for(int z = 0; z < T; ++z) {
		int n, k;
		cin >> n >> k;
		double u;
		cin >> u;
		vector<double> prob;
		for(int i = 0; i < n; ++i) {
			double temp;
			cin >> temp;
			prob.push_back(temp);
		}
		sort(prob.begin(), prob.end());
		prob.push_back(1);

		for(int i = 0; i < n; ++i) {
			if((prob[i+1] - prob[i])*(i+1) <= u) {
				u -= (prob[i+1] - prob[i])*(i+1);
				for(int j = 0; j <= i; ++j) {
					prob[j] = prob[i+1];
				}
			}
			else {
				for(int j = 0; j <= i; ++j) {
					prob[j] += u/(i+1);
				}
				u = 0;
				break;
			}
		}

		double prod = 1;
		for(int i = 0; i < n; ++i) {
			prod *= prob[i];
		}

		cout << "Case #" << z+1 << ": " << setprecision(9) << prod << "\n";
	}
}