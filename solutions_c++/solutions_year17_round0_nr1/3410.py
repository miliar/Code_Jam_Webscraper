#include <iostream>
#include <string.h>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int c = 0; c < t; c++) {
		char s[1005];
		int k;
		int count = 0;
		cin >> s >> k;
		for (int i = 0; i <= strlen(s) - k; i++) {
			if (s[i] == '-') {
				for (int j = i; j < k+i; j++) {
					s[j] = (s[j] == '-')? '+' : '-';
				}
				count++;
			}
		}
		for (int i = 0; i < strlen(s); i++) {
			if (s[i] == '-') {
				count = -1;
				break;
			}
		}
		cout << "Case #" << c+1 << ": ";
		(count == -1)? cout << "IMPOSSIBLE" << '\n': cout << count << '\n';
	}
	return 0;
}
