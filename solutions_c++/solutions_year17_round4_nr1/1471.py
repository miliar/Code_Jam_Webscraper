#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

class freshchocolate {
	private:
		int n, p;
		std::vector<int> gss;

		std::vector<int> memo;

		int sol;

		bool try_sub(std::vector<int> &p, const std::vector<int> &s) {
			for (unsigned i = 0; i < p.size(); ++i) {
				if (p.at(i) < s.at(i)) {
					return false;
				}
			}
			for (unsigned i = 0; i < p.size(); ++i) {
				p.at(i) -= s.at(i);
			}
			return true;
		}

	public:
		void input(std::istream &is) {
			is >> n >> p;
			gss.reserve(n);
			int x;
			for (int i = 0; i < n; ++i) {
				is >> x;
				gss.push_back(x);
			}
		}

		void solve() {
			sol = 0;
			std::vector<int> mods(p, 0);
			for (std::vector<int>::const_iterator gi = gss.begin(); gi < gss.end(); ++gi) {
				++(mods.at((*gi) % p));
			}
			sol += mods.at(0);
			mods.at(0) = 0;
			if (p == 2) {
				while (try_sub(mods, std::vector<int>({0, 2}))) {
					++sol;
				}
				if (mods.at(1) > 0) {
					++sol;
				}
			} else if (p == 3) {
				while (try_sub(mods, std::vector<int>({0, 1, 1}))) {
					++sol;
				}
				while (try_sub(mods, std::vector<int>({0, 0, 3}))) {
					++sol;
				}
				while (try_sub(mods, std::vector<int>({0, 3, 0}))) {
					++sol;
				}
				if (mods.at(2) > 0 || mods.at(1) > 0) {
					++sol;
				}
			} else if (p == 4) {
				while (try_sub(mods, std::vector<int>({0, 1, 0, 1}))) {
					++sol;
				}
				while (try_sub(mods, std::vector<int>({0, 0, 2, 0}))) {
					++sol;
				}
				while (try_sub(mods, std::vector<int>({0, 2, 1, 0}))) {
					++sol;
				}
				while (try_sub(mods, std::vector<int>({0, 0, 0, 4}))) {
					++sol;
				}
				while (try_sub(mods, std::vector<int>({0, 4, 0, 0}))) {
					++sol;
				}
				if (mods.at(3) > 0 || mods.at(2) > 0 || mods.at(1) > 0) {
					++sol;
				}
			} else {
				throw "invalid p";
			}
		}

		void output(std::ostream &os) {
			os << sol;
		}
};

/*
2:
0
11

3:
0
21
111
222

4:
0
31
22
211
3333
1111
*/

int main(void) {
	int znj;
	std::cin >> znj;
	for (int i = 0; i < znj; ++i) {
		freshchocolate task;
		task.input(std::cin);
		task.solve();
		std::cout << "Case #" << (i + 1) << ": ";
		task.output(std::cout);
		std::cout << std::endl;
	}
}
