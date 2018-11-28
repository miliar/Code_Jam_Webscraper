#include <iostream>

using namespace std;

int flip(string &start, int k) {
	int length = start.length();
	int res = 0;
	for (int i=0; i<length; ++i) {
		if (start[i] == '-') {
			if (i > length-k) return -1;
			for (int j=i; j<i+k; ++j) {
				if (start[j] == '-') start[j] = '+';
				else start[j] = '-';
			}
			res++;
		}
	}
	return res;
}

int main() {
	int numCases;
	cin >> numCases;
	string line;
	getline(cin, line);
	for (int i=0; i<numCases; ++i) {
		getline(cin, line);
		int pos = line.find(' ');
		string start = line.substr(0, pos);
		int k = stoi(line.substr(pos+1));
		int cnt = flip(start, k);
		cout << "Case #" << i+1 << ": ";
		if (cnt == -1) cout << "IMPOSSIBLE" << endl;
		else cout << cnt << endl;
	}
	return 0;
}