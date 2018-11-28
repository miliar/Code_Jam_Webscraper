#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::endl;

int main()
{
	unsigned T;
	cin >> T;
	for (unsigned case_num = 1; case_num <= T; ++case_num) {
		std::vector<int> states;
		size_t length;
		char tmp;
		for (;;) {
			tmp = cin.get();
			if (tmp == ' ') break;
			if (tmp == '+' || tmp == '-')
			states.push_back(tmp == '+' ? true : false);
		}
		cin >> length;

		size_t steps = 0;

		auto iter = states.begin();
		for (auto end = states.end() - (length - 1);
			iter != end; ++iter) {
			if (!*iter) {
				for (auto fliping = iter, end = iter + length;
					fliping != end; ++fliping)
					*fliping = *fliping ? false : true;
				++steps;
			}
		}

		bool possible = true;
		for (; iter != states.end(); ++iter) {
			if (!*iter) {
				possible = false;
			}
		}

		cout << "Case #" << case_num << ": ";
		if (possible) {
			cout << steps;
		}
		else {
			cout << "IMPOSSIBLE";
		}
		cout << endl;
	}
	return 0;
}
