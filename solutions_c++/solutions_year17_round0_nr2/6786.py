#include<iostream>
#include<string>
#include<fstream>
using namespace std;
int main() {
	ofstream output;
	output.open("OUT.in");
	string arr[100];
	int c = 0, T; cin >> T; int t = T;
	while (T) {
		string s; cin >> s;
		if (s.size() == 1) { arr[c] = s; }
		else {
			int f = 0, i = 0;
			for (i = 1; i < s.size(); i++) {
				if (s[i] < s[i - 1]) {
					f = 1; break;
				}
			}
			if (f) {
				int j = i - 1;
				while (j > 0) {
					if (s[j] == s[j - 1])j--;
					else break;
				}
				s[j]--;
				for (int k = j + 1; k < s.size(); k++)s[k] = '9';
				arr[c] = s;
			}
			else arr[c] = s;
		}
		T--;
		c++;
	}


	for (int i= 0;i < t;i++) {
		output << "Case #" << i+1 << ": ";
		if (arr[i][0] == '0') {
			int k = 0;
			while (arr[i][k]=='0') k++;
			for (; k < arr[i].size(); k++) {
				output << arr[i][k];
			}
			output << '\n';
		}
		else output << arr[i] << endl;
	}
	return 0;
}