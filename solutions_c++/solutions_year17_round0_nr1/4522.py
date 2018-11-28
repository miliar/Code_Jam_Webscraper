#include <iostream>
#include <string>
using namespace std;

int checkValid(string& str, int& K);
char reverse(char ch);

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i) {
		string str;
		int K, num;
		cin >> str >> K;
		num = checkValid(str, K);
		cout << "Case #" << i + 1 << ": ";
		if (num == -1) {
			cout << "IMPOSSIBLE\n"; 
		} else {
			cout << num << endl;
		}
	}
}

char reverse(char ch) {
	return (ch == '-') ? '+' : '-';
}

int checkValid(string& str, int& K) {
	int i = 0, count = 0;
	while (i <= str.size() - K) {
		if (str[i] == '-') {
			for (int j = 0; j < K; ++j) {
				str[i + j] = reverse(str[i + j]);
			}
			++count;
		}
		++i;
	}
	bool isValid = true;
	while (i < str.size()) {
		if (str[i] == '-') return -1;
		++i;
	}
	return count;
}