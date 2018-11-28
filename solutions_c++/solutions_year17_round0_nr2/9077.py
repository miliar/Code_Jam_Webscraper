#include<iostream>
#include<string>
using namespace std;

string tidy(string s) {
	int i = 0;
	for (; i < (int)s.length() - 1; ++i) {
		if (s[i + 1] < s[i]) {
			string tail = string(s.length() - i - 1, '9');
			int head = stoi(s.substr(0, i + 1)) - 1;
			s = to_string(head);
			return tidy(s) + tail;
			break;
		}
	}
	return s;
}

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		int N;
		cin >> N;
		string s = to_string(N);
		cout << "Case #" << i << ": " << stoi(tidy(s)) << endl;
	}
	return 0;
}
