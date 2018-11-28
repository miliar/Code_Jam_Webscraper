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
		int K;
		s = new char[1001];
		in >> s >> K;
		int len = slength(s);
		int cnt = 0;
		bool isdone = true;
		for (int i = 0; i < len-(K-1); i++) {
			if (s[i] == '+')
				continue;
			else {
				cnt++;
				for (int j = 0; j < K; j++) {
					if (s[i + j] == '+') {
						s[i + j] = '-';
					}
					else {
						s[i + j] = '+';
					}
				}
			}
		}
		for (int i = len - (K-1); i < len; i++) {
			if (s[i] == '-')
				isdone = false;
		}
		if (isdone) {
			out << "Case #" << T + 1 << ": " << cnt << endl;
		}
		else {
			out << "Case #" << T + 1 << ": IMPOSSIBLE" << endl;
		}
	}
	return 0;
}