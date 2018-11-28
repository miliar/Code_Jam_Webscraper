#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <queue>

using namespace std;

int main(int argc, char* argv[])
{
	srand(13);
	ios_base::sync_with_stdio(false);

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	for (int test = 1; test <= T; ++test) {
		string s;
		int k;
		cin >> s >> k;

		int flipsCount = 0;
		queue<int> ends;
		int answer = 0;
		for (int i = 0; i < s.size(); ++i) {
			while (ends.size() && ends.front() <= i) {
				--flipsCount;
				ends.pop();
			}
			if ((s[i] == '+' && flipsCount % 2 != 0) || s[i] == '-' && flipsCount % 2 == 0) {
				if (i + k <= s.size()) {
					++flipsCount;
					ends.push(i + k);
					++answer;
				}
				else {
					answer = -1;
					break;
				}
			}
		}

		cout << "Case #" << test << ": ";
		if (answer >= 0) {
			cout << answer;
		}
		else {
			cout << "IMPOSSIBLE";
		}
		cout  << '\n';
		
	}

	return 0;
}

