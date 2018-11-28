#include <iostream>
#include <cstdio>

using namespace std;

int main() {
	int testCnt;
	cin >> testCnt;
	for (int testNum = 1; testNum <= testCnt; testNum++) {
		cout << "Case #" << testNum <<": ";
		string str;
		cin >> str;
		bool isGood = false; 
		while (!isGood) {
			isGood = true;
			for (int i = 0; i < str.length() - 1; i++) {
				if (str[i] > str[i + 1]) {
					isGood = false;
					str[i] = str[i] - 1;
					for (int j = i + 1; j < str.length(); j++)
						str[j] = '9';
					break;
				}
			}
		}
		for (int i = 0; i < str.length(); i++) {
			if (str[i] == '0')
				continue;
			else {
				for (int j = i; j < str.length(); j++)
					cout << str[j];
				cout << endl;
				break;
			}
		}
	}
	return 0;
}