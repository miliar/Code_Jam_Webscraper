#include <iostream>
using namespace std;

void setNine(string &s, int startIndex, int endIndex) {
	for (int i=startIndex; i<=endIndex; i++) {
		s[i] = '9';
	}
}

void update(string &s, int len) {
	int curr, next;
	for (int i=0; i<len-1; i++) {
		curr = s[i] - '0';
		next = s[i+1] - '0';
		if (curr > next) {
			curr--;
			s[i] = curr + '0';
			setNine(s, i+1, len-1);
		}
	}
}

string removeTrailingZeros(string s, int len) {
	string res;
	for (int i=0; i<len; i++) {
		if (s[i] != '0')
			res += s[i];
	}
	return res;
}

int main() {
	int n, len;
	string s;
	cin >> n;
	for (int t=0; t<n; t++) {
		cin >> s;
		len = s.size();
		for (int i=0; i<len; i++)
			update(s, len);
		s = removeTrailingZeros(s, len);
		cout << "Case #" << t+1 << ": " << s << endl;
	}
	return 0;
}