#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	string str;
	cin >> T;
	getline(cin, str);
	for (int t = 1; t <= T; ++t) {
		getline(cin, str);
		int pos = 1;
		int last_good = 0;
		int N = int(str.size());
		while (pos < N && str[pos] >= str[pos - 1]) {
			if (str[pos] > str[pos - 1])
				last_good = pos;
			++pos;
		}
		cout << "Case #" << t << ": ";
		if (pos < N) {
			str[last_good] = str[last_good] - 1;
			++last_good;
			fill(str.begin() + last_good, str.end(), '9');
			istringstream iss(str);
			long long num;
			iss >> num;
			cout << num << endl;
		}
		else {
			cout << str << endl;
		}

	}
	return 0;
}