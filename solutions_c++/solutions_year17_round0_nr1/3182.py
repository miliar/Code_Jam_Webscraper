#include <fstream>

using namespace std;

ifstream cin("input.txt");
ofstream cout("output.txt");

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		string s;
		int k, j = 0, cnt = 0;
		cin >> s >> k;
		while (j < s.length())
			if (s[j] == '+')
				++j;
			else {
				if (j + k > s.length())
					break;
				for (int z = j; z < j + k; ++z)
					s[z] = (s[z] == '-') ? '+' : '-';
				++cnt;
			}
		cout << "Case #" << i + 1 << ": ";
		if (j == s.length())
			cout << cnt << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}