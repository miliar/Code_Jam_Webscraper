#include<iostream>
#include<string>
#include<vector>
using namespace std;
int main() {
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		string str;
		cin >> str;
		for (int j = (int)str.size() -1; j > 0; j--) {
			int cur = str[j] - '0';
			int bef = str[j - 1] - '0';
			if (cur < bef) {
				str[j-1]--;
				for (int k = j; k < (int)str.size(); k++) {
					str[k] = '9';
				}
			}
		}

		
		if (str[0] == '0' && (int)str.size() != 1) {
			int elast = 1;
			while (1) {
				if (str[elast + 1] == '0') {
					elast++;
				}
				else
					break;
			}
			str.erase(0, elast);
		}
		cout <<"Case #" << i+1 << ": " << str << endl;
	}
}