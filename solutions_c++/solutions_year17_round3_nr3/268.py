#include <iostream>
#include <iomanip>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>

class coretraining {
	private:
		int n, k;
		int u;
		std::vector<int> ps;

		double sol;

		int readprec(std::istream &is, int prec) const {
			int m, e;
			char c;
			is >> m >> c >> e;
			return m * prec + e;
		}

	public:
		void input(std::istream &is) {
			is >> n >> k;
			u = readprec(is, 10000);
			ps.reserve(n);
			for (int i = 0; i < n; ++i) {
				ps.push_back(readprec(is, 10000));
			}
		}

		void solve() {
			if (n == k) {
				std::priority_queue<int, std::vector<int>, std::greater<int> > psq;
				for (std::vector<int>::iterator pi = ps.begin(); pi < ps.end(); ++pi) {
					psq.push(*pi);
				}
				for (int x = 0; x < u; ++x) {
					int mp = psq.top();
					psq.pop();
					psq.push(mp + 1);
				}
				sol = 1.;
				while (!(psq.empty())) {
					sol *= (static_cast<double>(psq.top()) / 10000);
					psq.pop();
				}
			} else {
				sol = -1.; // not implemented yet
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
		coretraining task;
		task.input(std::cin);
		task.solve();
		std::cout << "Case #" << (i + 1) << ": ";
		task.output(std::cout);
		std::cout << std::endl;
	}
}
