#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main(void) {
	int test;
	cin >> test;

	for (int Case = 1; Case <= test; ++Case) {

		int n, c, m;
		cin >> n >> c >> m;

		vector<int> cntC(c+1, 0), cntP(n+1, 0);
		for (int i = 0; i < m; ++i) {
			int pos, id;
			cin >> pos >> id;
			++cntP[pos];
			++cntC[id];
		}

		int best = *max_element(cntC.begin(), cntC.end());
		int lo = best, hi = m;
		while (lo < hi) {
			int mid = (lo + hi) / 2;
			auto tmp = cntP;
			for (int i = tmp.size()-1; i > 1; --i) {
				tmp[i-1] += max(0, tmp[i] - mid);
			}

			if (tmp[1] > mid) {
				lo = mid + 1;
			} else {
				hi = mid;
			}
		}

		best = lo;
		int move = 0;
		auto tmp = cntP;
		for (int i = tmp.size()-1, j = 0; i > 1; --i) {
			move += max(0, tmp[i] - best);
		}

		cout << "Case #" << Case << ": " << best << " " << move << endl;
		cerr << Case << endl;
	}
}