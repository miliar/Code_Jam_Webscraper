#include <iostream>
#include <string> 

using namespace std;
int main() {
	int T; cin >> T;

	string s;
	int K;

	int cnt = 0;

	for(int i = 0; i < T; i++) {
		cin >> s >> K;
		cnt = 0;
		
		for (int j = 0; j <= s.length()-K; j++) {
			if (s[j] == '-') {
				cnt++;
				for(int k = 0; k < K; k++) {

					if (s[j+k]=='-') s[j+k]='+';
					else s[j+k]='-';
				}
			}
		}

		cout << "Case #" << i + 1 << ": ";
		bool f = true;
		for (int j = s.length() - K + 1; j < s.length(); j++) {
			if (s[j] == '-')
			{
				cout << "IMPOSSIBLE" << endl;
				f = false;
				break;
			}
		}
		if (f) {
			cout << cnt << endl;
		}
	}

	return 0;
}