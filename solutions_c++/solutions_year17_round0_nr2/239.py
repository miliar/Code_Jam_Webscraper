#include <bits/stdc++.h>

using namespace std;

void doCase(int t) {
	string in;
	cin >> in;
	
	int lastInc = 0;
	char lastDigit = in[0];
	int i;
	for (i=1; i<in.length(); i++) {
		if (in[i] > lastDigit) {
			lastInc = i;
			lastDigit = in[i];
		}
		if (in[i] < lastDigit) break;
	}
	
	cout << "Case #" << t << ": ";
	if (i == in.length()) {
		// Simple, do nothing
		cout << in << endl;
		return;
	} else {
		in[lastInc]--;
		for (int i=lastInc+1; i<in.length(); i++) {
			in[i] = '9';
		}
		int so = 0;
		while (so != in.length() && in[so] == '0') so++;
		if (so == in.length()) {
			cout << 0 << endl;
			return;
		}
		cout << in.substr(so) << endl;
		return;
	}
}

int main() {
	int T;
	cin >> T;
	for (int i=0; i<T; i++)
		doCase(i+1);
	return 0;
}
