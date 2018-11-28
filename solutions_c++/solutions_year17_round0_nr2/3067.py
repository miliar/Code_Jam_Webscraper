#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

class tidynumbers {
	private:
		std::string n;

		std::string sol;

	public:
		void input(std::istream &is) {
			is >> n;
		}

		void solve() {
			sol = n;
			for (int i = static_cast<int>(sol.size()) - 2; i >= 0; --i) {
				if (sol.at(i) > sol.at(i + 1)) {
					for (int j = i + 1; j < static_cast<int>(sol.size()); ++j) {
						sol.at(j) = '9';
					}
					for (; sol.at(i) == '0'; --i) {
						sol.at(i) = '9';
					}
					sol.at(i) = sol.at(i) - 1;
				}
			}
			for (; sol.at(0) == '0'; sol = sol.substr(1));
		}

		void output(std::ostream &os) {
			os << sol;
		}
};

int main(void) {
	tidynumbers task;
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
