#include <iostream>
#include <string>

using namespace std;

int countFlips(const string& s, int K) {
	bool pancakes[1001];
	int sLen = s.length();
	for (int i = 0; i < sLen; i++)
		if (s[i] == '-')
			pancakes[i] = false;
		else
			pancakes[i] = true;
	
	int flips = 0;
	for (int i = 0; i <= sLen - K; i++) {
		if (!pancakes[i]) {
			for (int j = 0; j < K; j++) {
				pancakes[i+j] = !pancakes[i+j];
			}
			flips++;
		}
	}
	int allFlipped = true;
	for (int i = sLen - K + 1; i < sLen; i++) {
		if (!pancakes[i]) {
			allFlipped = false;
			break;
		}
	}
	if (allFlipped)
		return flips;
	else
		return -1;
}

int main() {
	int T;
	cin >> T;
	for (int iCase = 1; iCase <= T; iCase++) {
		string s;
		int K;
		cin >> s >> K;
		cout << "Case #" << iCase << ": ";
		int flips = countFlips(s, K);
		if (flips == -1)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << flips << endl;
	}
}
