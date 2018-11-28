#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <map>
#include <stack>
#include <cassert>

using namespace std;

struct Solver {
	int n[4];
	int P;

	Solver() { 
		std::fill(n, n+4, 0);
	}

	int solve() {
		if (P == 2)
			return n[0] + std::ceil(n[1] / 2.);
		if (P == 3) {
			int sol = n[0];
			int min12 = std::min(n[1], n[2]);
			sol += min12;
			n[1] -= min12;
			n[2] -= min12;
			sol += std::ceil(n[1] / 3.);
			sol += std::ceil(n[2] / 3.);
			return sol;
		}
		int sol = n[0];
		int min13 = std::min(n[1], n[3]);
		sol += min13;
		n[1] -= min13;
		n[3] -= min13;
		sol += n[2] / 2;
		n[2] %= 2;
		if (n[2] == 1) {
			sol += 1;
			n[2] = 0;
			if (n[1] > 0) {
				n[1] = std::max(0, n[1] - 2);
			} else {
				n[3] = std::max(0, n[3] - 2);
			}
		}
		sol += std::ceil(n[1] / 4.);
		sol += std::ceil(n[3] / 4.);
		return sol;
	}
};


int main(){
	int tcase;
	cin >> tcase;
	
	for(size_t casen = 0; casen < tcase; ++casen)
	{
		int N, P;
		cin >> N >> P;
		Solver solver;
		solver.P = P;
		for(int i = 0 ; i < N ; ++i) {
			int g;
			cin >> g;
			solver.n[g % P]++;
		}
		
		cout << "Case #" << casen + 1 << ": ";
		cout << solver.solve() << endl;
		
	}
	

	return 0;
}
