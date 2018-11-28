#include <string>
#include <iostream>
#include <cmath>
#include <cstdio>
using namespace std;


int main()
{
	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);

	int tests, caseNumber = 0;
	cin >> tests;
	while (++caseNumber <= tests) {
		std::string answer;
		std::string n;
		cin >> n;
		for (size_t i = n.size() - 1; i > 0; --i) {
			if (n[i] < n[i - 1]) {
				--n[i - 1];
				for (size_t j = i; j < n.size(); ++j)
					n[j] = '9';
			}
		}
		cout << "Case #" << caseNumber << ": " << n.substr(n.find_first_not_of('0')) << endl;
	}
	return 0;
}

/*
4
132
1000
7
111111111111111110
*/