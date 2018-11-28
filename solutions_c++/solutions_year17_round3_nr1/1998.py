#include <iostream>
#include <fstream>
#include <string>
#include <array>
#include <forward_list>
#include <list>
#include <vector>
#include <bitset>
#include <chrono>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <deque>
#include <stack>
#include <limits>
#include <algorithm>
#include <numeric>
#include <utility>
#include <random>
#include <complex>
#include <tuple>
#include <functional>
#include <iomanip>

using namespace std;

const double PI = 3.141592653589793;

struct pc_t {
	double r;
	double h;
};

void find_max_surface(vector<pc_t> & pcs, int level, int c_k, int k,
		double c_surface, double & max_surface) {
	
	if (c_k == k) {
		if (c_surface > max_surface) max_surface = c_surface;
		return;
	}

	if (level >= pcs.size()) return;
	
	for (int i = level; i < pcs.size(); i++) {
		double area_top = PI * pcs[i].r * pcs[i].r;
		double area_side = 2.0 * PI * pcs[i].r * pcs[i].h;
		if (level == 0) {
			c_surface = area_top;	
		}
		find_max_surface(pcs, i + 1, c_k + 1, k,
			c_surface + area_side, max_surface);
	}

}

void solve(int ti) {
	int n, k; cin >> n >> k;
	vector<pc_t> pcs(n);
	
	for (auto & pc : pcs) cin >> pc.r >> pc.h;
	
	sort(pcs.begin(),pcs.end(), [](auto & pc1, auto & pc2) {
		if (pc1.r == pc2.r)
			return pc2.h < pc1.h;
		else return pc2.r < pc1.r;
	});

	double max_surface = 0.0;
	find_max_surface(pcs, 0, 0, k, 0, max_surface);
	
	cout << fixed << setprecision(6) << max_surface;
}

int main() {
	int t; cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		solve(i);
		cout << endl;
	}
}
