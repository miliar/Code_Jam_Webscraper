#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

#define all(a) a.begin(),a.end()

using namespace std;

struct Solver {
	int D, N;
	vector<int> K;
	vector<int> S;
	double ans;
	void read() {
		cin >> D >> N;
		K.resize(N);
		S.resize(N);
		for(int i=0; i<N; i++){
			cin >> K[i];
			cin >> S[i];
		}
	}

	void solve() {
		vector<double> times;
		times.resize(N);
		for(int i=0; i<N; i++){
			times[i] = ((double)D - K[i]) / S[i];
		}
		ans = D /(*max_element(all(times)));
	}

	void print() {
		printf("%.6f",ans);
	}
};

int main(int argc, char** argv) {
	//std::ios_base::sync_with_stdio(false);
	//std::cin.tie(nullptr);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		Solver thisTestCase;
		thisTestCase.read();
		thisTestCase.solve();
		cout << "Case #" << t << ": ";
		thisTestCase.print();
		cout << endl;
	}
	return 0;
}
