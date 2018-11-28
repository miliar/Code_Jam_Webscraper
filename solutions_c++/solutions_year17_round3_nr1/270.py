#include <iostream>
#include <iomanip>
#include <cmath>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>

class amplesyrup {
	private:
		int n, k;
		std::vector<std::pair<int, int> > ds;

		double sol;

		double sqr(int x) const {
			return static_cast<double>(x) * static_cast<double>(x);
		}

	public:
		void input(std::istream &is) {
			is >> n >> k;
			ds.reserve(n);
			int r, h;
			for (int i = 0; i < n; ++i) {
				is >> r >> h;
				ds.push_back(std::make_pair(r, h));
			}
		}

		void solve() {
			std::sort(ds.begin(), ds.end());
			double ta = 0;
			std::priority_queue<double, std::vector<double>, std::greater<double> > mss;
			for (std::vector<std::pair<int, int> >::const_iterator it = ds.begin(); it < ds.begin() + k; ++it) {
				double hc = it->second * 2.0 * it->first * M_PI;
				ta += hc;
				mss.push(hc);
			}
			sol = ta + sqr((ds.begin() + k - 1)->first) * M_PI;
			for (std::vector<std::pair<int, int> >::const_iterator it = ds.begin() + k; it < ds.end(); ++it) {
				double hc = it->second * 2.0 * it->first * M_PI;
				ta -= mss.top();
				mss.pop();
				ta += hc;
				mss.push(hc);
				sol = std::max(sol, ta + sqr(it->first) * M_PI);
			}
		}

		void output(std::ostream &os) {
			os << std::fixed << std::setprecision(8) << sol;
		}
};

int main(void) {
	int znj;
	std::cin >> znj;
	for (int i = 0; i < znj; ++i) {
		amplesyrup task;
		task.input(std::cin);
		task.solve();
		std::cout << "Case #" << (i + 1) << ": ";
		task.output(std::cout);
		std::cout << std::endl;
	}
}
