#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <iomanip>


using namespace std;

int main() {
#ifdef _DEBUG
	std::ifstream in("C:\\Users\\silvio.lazzeretti\\Downloads\\a-example.txt");
	std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
	std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!
#endif
	int T;
	cin >> T;
	int t = 0;
	while (++t <= T) {
		int D;
		int N;
		cin >> D >> N;

		vector<pair<double, double>> h(N);
		for (int i = 0; i < N; ++i) {
			int k, s;
			cin >> k >> s;
			h[i] = make_pair(k, s);
		}

		double slowest = 0;
		for (auto p : h) {
			double tmp = (D - p.first) / p.second;
			if (tmp > slowest) {
				slowest = tmp;
			}
		}



		cout << "Case #" << t << ": ";
		cout << fixed << setprecision(6) << D / slowest;
		cout << endl;
	}
	return 0;
}