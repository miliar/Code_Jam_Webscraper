#include <iostream>
#include <string>
#include <cstring>
#include <fstream>
using namespace std;

int main() {
	ifstream cin("B-large.in");
	ofstream cout("B-large.out");
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i){
		string s;
		cin >> s;
		bool checked = true;
		for (int i = 1; i < s.size(); ++i) {
			if (s[i] < s[i - 1] && checked) {
				int j = i - 1;
				while (j >= 1 && s[j] - 1 < s[j - 1]) {
					--j;
				}
				s[j] = s[j] - 1;
				i = j + 1;
				checked = false;
			}
			if (!checked) {
				s[i] = '9';
			}
		}
		for (int i = 0; i < s.size(); ++i) {
			if (s[i] != '0') {
				s = s.substr(i, s.size() - i);
				break;
			}
		}
		cout << "Case #" << i+1 << ": " << s << endl;
	}
	cin.close();
	cout.close();
	system("pause");
}
