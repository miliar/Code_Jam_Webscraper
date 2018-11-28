// problemA.cpp : Defines the entry point for the console application.
//

#include <iostream> 
#include <vector>
#include <string>

using namespace std;

void main() {
	int t = 0;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		string s;
		int k = 0;
		cin >> s >> k;
		vector<bool> line;
		for (std::string::iterator it = s.begin(); it != s.end(); ++it) {
			line.push_back(*it == '+');
		}
		int result = 0;

		for (size_t pos = 0; pos <= line.size() - k; pos++) {
			if (line[pos]) {
				continue;
			}
			result++;
			for (int j = 0; j < k; j++) {
				line[pos + j] = !line[pos + j];
			}
		}
		bool isPossible = true;
		for (size_t j = 0; j < line.size(); j++) {
			isPossible &= line[j];
		}
		if (isPossible) {
			cout << "Case #" << i << ": " << result << endl;
		}
		else {
			cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
		}
	}
}