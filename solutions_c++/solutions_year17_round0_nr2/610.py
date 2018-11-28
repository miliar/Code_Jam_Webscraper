#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int main()
{
	int T; cin >> T;
	for (int t = 0; t < T; t++) {
		string s; cin >> s;

		for (int i = s.size() - 1; i > 0; i--) {
			if (s[i - 1] > s[i]) {
				s[i - 1]--;
				for (int j = i; j < s.size(); j++) {
					s[j] = '9';
				}
			}
		}

		cout << "CASE #" << t + 1 << ": ";
		cout << atoll(s.data()) << endl;
	}

    return 0;
}

