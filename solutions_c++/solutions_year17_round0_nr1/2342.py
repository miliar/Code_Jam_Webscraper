#include <string>
#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);

	int tests, caseNumber = 0;
	cin >> tests;
	std::string s;
	size_t k;
	while (++caseNumber <= tests) {
		cin >> s >> k;
		int answer = 0;
		size_t i = 0;
		for (; i <= s.size() - k; ++i) {
			if (s[i] == '-') {
				++answer;
				for (size_t j = 0; j < k; ++j) {
					s[i + j] = (s[i + j] == '-' ? '+' : '-');
				}
			}
		}
		for (; i < s.size(); ++i) {
			if (s[i] == '-') {
				answer = -1;
				break;
			}
		}
		if (answer == -1) {
			cout << "Case #" << caseNumber << ": IMPOSSIBLE" << endl;
			continue;
		}
		cout << "Case #" << caseNumber << ": " << answer << endl;
	}
	return 0;
}
