#include <iostream>
using namespace std;

char flip(char c) {
	if(c=='+') {return '-';}
	else {return '+';}
}

int main() {
	int t, k, len, times, tst;
	string s;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		times = 0;
		cin >> s >> k;
		len = s.size();
		for(int j=0; j< len-k+1; j++) {
			if(s[j]=='-') {
				for(int x=0; x<k; x++) {
					s[j+x] = flip(s[j+x]);
				}
				times++;
				//cout << "[" << j << "] ...... " << s << " ......" << endl;
			}
		}
		tst = 0;
		for(int y=1; y<k; y++) {
			if(s[len-y]=='-') {tst = 1;}
		}
		if(tst==1) {
			cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
		} else {
			cout << "Case #" << i << ": " << times << endl;
		}
	}
	return 0;
}
