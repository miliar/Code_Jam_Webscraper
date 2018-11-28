#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <fstream>
using namespace std;
int main() {
	ifstream file("B-large.in");
	ofstream out("output.txt");
	int n;
	file >> n;
	for (int i = 1; i <= n; i++) {
		string tmp;
		vector<char> result;
		file >> tmp;
		char cur = tmp[0];
		for (int j = 0; j < tmp.length(); j++) {
			if (cur <= tmp[j]) {
				cur = tmp[j];
				continue;
			}
			else {
				int k = j - 1;
				while (tmp[k] == '0' && k > 0) {
					tmp[k] = '9';
					k--;
				}
				if (k != 0 && tmp[k] == '1') {
					tmp[k] = '0';
				}
				else {
					if (k == 0 && tmp[k] == '1') {
						tmp.erase(tmp.begin());
						j--;
					} else {
						tmp[k] -= 1;
					}
				}
				for (int m = j; m < tmp.length(); m++) {
					tmp[m] = '9';
				}
				j = 0;
				cur = tmp[0];
			}
		}
		out << "Case #" << i << ": " << tmp << endl;

	}
	return 0;
}