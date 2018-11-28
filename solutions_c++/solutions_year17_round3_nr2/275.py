#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

class parentingpartnering {
	private:
		int ac, aj;
		std::vector<std::pair<std::pair<int, int>, bool> > as;

		int sol;

		int wrap(int interval) const {
			if (interval < 0) {
				interval += 24 * 60;
			}
			return interval;
		}

	public:
		void input(std::istream &is) {
			is >> ac >> aj;
			int b, e;
			as.reserve(ac + aj);
			for (int i = 0; i < ac; ++i) {
				is >> b >> e;
				as.push_back(std::make_pair(std::make_pair(b, e), false));
			}
			for (int i = 0; i < aj; ++i) {
				is >> b >> e;
				as.push_back(std::make_pair(std::make_pair(b, e), true));
			}
		}

		void solve() {
			sol = 0;
			std::sort(as.begin(), as.end());
			int tc = 0, tj = 0;
			std::vector<int> cpi, jpi, npi;
			for (std::vector<std::pair<std::pair<int, int>, bool> >::const_iterator cit = as.begin(); cit < as.end(); ++cit) {
				std::vector<std::pair<std::pair<int, int>, bool> >::const_iterator nit = (((cit + 1) < as.end())? (cit + 1) : as.begin());
				int diff = cit->first.second - cit->first.first;
				int follow = wrap(nit->first.first - cit->first.second);
				if (cit->second) {
					tj += diff;
					if (nit->second) {
						jpi.push_back(follow);
					} else {
						npi.push_back(follow);
						++sol;
					}
				} else {
					tc += diff;
					if (nit->second) {
						npi.push_back(follow);
						++sol;
					} else {
						cpi.push_back(follow);
					}
				}
			}
			std::sort(cpi.begin(), cpi.end());
			std::sort(jpi.begin(), jpi.end());
			std::sort(npi.begin(), npi.end());
			for (std::vector<int>::const_iterator it = cpi.begin(); it < cpi.end(); ++it) {
				if (tc + (*it) <= 12 * 60) {
					tc += (*it);
				} else {
					sol += 2;
				}
			}
			for (std::vector<int>::const_iterator it = jpi.begin(); it < jpi.end(); ++it) {
				if (tj + (*it) <= 12 * 60) {
					tj += (*it);
				} else {
					sol += 2;
				}
			}
		}

		void output(std::ostream &os) {
			os << sol;
		}
};

int main(void) {
	int znj;
	std::cin >> znj;
	for (int i = 0; i < znj; ++i) {
		parentingpartnering task;
		task.input(std::cin);
		task.solve();
		std::cout << "Case #" << (i + 1) << ": ";
		task.output(std::cout);
		std::cout << std::endl;
	}
}
