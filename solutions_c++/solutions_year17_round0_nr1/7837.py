#include <iostream>
#include <string>

using namespace std;

int main() {
	int t, i, k, j, l, count = 0;
	cin >> t;
	string str;
	for(i = 0; i < t; i++) {
		cin >> str >> k;
		for(j = 0, count = 0; j < str.length() - k + 1; j++) {
			if(str[j] == '-') {
				for(l = j; l < j + k; l++) {
					if(str[l] == '-')
						str[l] = '+';
					else
						str[l] = '-';
				}
				count++;
			} else {
				continue;
			}
		}
		int flag = 1;
		for(j = str.length() - k; j < str.length(); j++) {
			if(str[j] == '-') {
				flag = 0;
				cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
				break;
			}
		}
		if(flag)
			cout << "Case #" << i+1 << ": " << count << endl;
	}
	return 0;
}
