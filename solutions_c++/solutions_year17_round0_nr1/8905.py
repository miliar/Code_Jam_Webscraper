#include <iostream>
#include <string>

using namespace std;

int main() {
	int t;
	cin >> t;
	for(int j = 0; j < t; j++) {
		string s;
		int k;
		cin >> s >> k;
		int flips = 0;
		for(int i = 0; i <= s.length()-k; i++) {
			if (s[i] == '-') {
				flips++;
				for (int q = 0; q < k; q++) {
					if(s[i+q] == '-') {
						s[i+q] = '+';
					} else {
						s[i+q] = '-';
					}
				}
			}
			//cout << flips << endl;
		}
		bool possible = true;
		for(int w = 0; w < k; w++) {
			if(s[s.length()-k+w] == '-') {
				possible = false;
				//cout << s[s.length()-k+w] << endl;
			}
		}
		cout << "Case #" << (j+1) << ": ";
		if(possible) {
			cout << flips;
		} else {
			cout << "IMPOSSIBLE";
		}
		cout << endl;
	}
}
