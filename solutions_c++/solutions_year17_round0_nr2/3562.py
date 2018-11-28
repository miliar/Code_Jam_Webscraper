#include <iostream>
#include <string>
#include <algorithm>
#include <cstring>

std::string solve(std::string s)
{
	for (int i = s.length() - 1; i > 0; i--) {
		if (s[i] < s[i - 1]) {
			int nineCount = s.length() - i;

			memset(&s[i], '9', nineCount);
			s[i - 1]--;
		}
	}

	if (s[0] == '0') {
		s = s.substr(1);
	}

	return s;
}

int main()
{
	int caseCount;

	std::cin >> caseCount;

	for (int i = 1; i <= caseCount; i++) {
		std::string s;

		std::cin >> s;
		std::cout << "Case #" << i << ": " << solve(s) << std::endl;
	}

	return 0;
}
