#include <iostream>
#include <string>
using namespace std;

int main() {
	int N;
	string s;
	
	int count = 0;
	int T;
	int check = 0;
	freopen("AA.in", "rt", stdin);
	freopen("output.txt","w", stdout);
	cin >> T;
	for (int t = 1; t <= T; t++) {
		check = 0;
		count = 0;
		cin >> s;
		cin >> N;
		for (int i = 0; i < s.length(); i++) {
			if (s[i] == '-') {
				if (i + N <= s.length()) {
					count++;
					for (int j = i; j < i + N; j++) {
						if (s[j] == '-') s[j] = '+';
						else s[j] = '-';
					}
				}
			}
		}
		for (int i = 0; i < s.length(); i++) {
			if (s[i] == '-') {
				check = 1;
				break;
			}
		}
		if (check == 1) {
			cout << "Case #" << t << ": " << "IMPOSSIBLE"<<endl;
		}
		else {
			cout << "Case #" << t << ": " << count<<endl;
		}
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}