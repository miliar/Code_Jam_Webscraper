#include<iostream>
#include<fstream>

using namespace std;

int slength(char* s) {
	int cnt = 0;
	while (s[cnt] != '\0') {
		cnt++;
	}
	return cnt;
}

int main() {
	ifstream in("input.txt");
	ofstream out("output.txt");
	int N;
	in >> N;
	for (int T = 0; T < N; T++) {
		char* s;
		s = new char[20];
		in >> s;
		int len = slength(s);
		for (int i = len - 1; i > 0; i--) {
			if (s[i] < s[i - 1]) {
				s[i] = '9';
				s[i - 1] = s[i - 1] - 1;
			}
		}
		for (int i = 0; i < len-1; i++) {
			if (s[i] == '9') {
				s[i + 1] = '9';
			}
		}
		out << "Case #" << T + 1 << ": ";
		for (int i = 0; i < len; i++) {
			if (i == 0 && s[i] == '0')
				continue;
			out << s[i];
		}
		out << endl;
	}
	return 0;
}