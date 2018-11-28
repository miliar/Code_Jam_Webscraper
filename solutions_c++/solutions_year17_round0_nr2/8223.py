#include <iostream>
#include <string>
using namespace std;

int main() {
	string s;
	int N;
	freopen("B-large.IN", "rt", stdin);
	freopen("B-OUT.TXT", "w", stdout);
	cin >> N;
	for (int T = 1; T <= N; T++) {
		cin >> s;
		for (int i = 0; i < s.length() - 1; i++) {
			if (s[i] > s[i + 1]) {
				s[i]--;
				for (int j = i + 1; j < s.length(); j++) {
					s[j] = '9';
				}
				i-=2;
			}
		}
		cout << "Case #" << T << ": ";
		for (int i = 0; i < s.length(); i++) {
			if (s[i] == '0')
				continue;
			cout << s[i];
		}
		cout << endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}