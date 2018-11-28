#include <iostream>
#include <string>

int solve(std::string s, int k)
{
	int flipCount = 0;
	int start = 0;

	while (true) {
		int blankPos = -1;

		for (int i = start; i < s.length(); i++) {
			if (s[i] == '-') {
				blankPos = i;
				break;
			}
		}

		if (blankPos == -1) {
			break;
		}

		if (blankPos + k > s.length()) {
			flipCount = -1;
			break;
		}

		for (int i = 0, j = blankPos; i < k; i++, j++) {
			s[j] = (s[j] == '-' ? '+' : '-');
		}

		flipCount++;
		start = blankPos;
	}

	return flipCount;
}

int main()
{
	int caseCount;

	std::cin >> caseCount;

	for (int i = 1; i <= caseCount; i++) {
		std::string s;
		int k;

		std::cin >> s >> k;

		int flipCount = solve(s, k);

		if (flipCount < 0) {
			std::cout << "Case #" << i << ": IMPOSSIBLE" << std::endl;
		} else {
			std::cout << "Case #" << i << ": " << flipCount << std::endl;
		}
	}

	return 0;
}
