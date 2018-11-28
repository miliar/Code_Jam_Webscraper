#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

class oversizedpancakeflipper {
	private:
		std::string s;
		int k;

		int sol;

	public:
		void input(std::istream &is) {
			is >> s >> k;
		}

		void solve() {
			sol = 0;
			for (unsigned int i = 0; i < s.size() - k + 1; ++i) {
				if (s.at(i) == '-') {
					++sol;
					for (int j = 0; j < k; ++j) {
						s.at(i + j) = (s.at(i + j) == '-') ? '+' : '-';
					}
				}
			}
			for (unsigned int i = 0; i < s.size(); ++i) {
				if (s.at(i) != '+') {
					sol = -1;
					break;
				}
			}
		}

		void output(std::ostream &os) {
			if (sol >= 0) {
				os << sol;
			} else {
				os << "IMPOSSIBLE";
			}
		}
};

int main(void) {
	oversizedpancakeflipper task;
	int znj;
	std::cin >> znj;
	for (int i = 0; i < znj; ++i) {
		task.input(std::cin);
		task.solve();
		std::cout << "Case #" << (i + 1) << ": ";
		task.output(std::cout);
		std::cout << std::endl;
	}
}
