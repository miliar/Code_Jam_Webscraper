/*
 * GCJ2017_QR_B.cpp
 *
 *  Created on: Apr 7, 2017
 *      Author: davidzhu
 */

#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

int T;
long long N;

bool adjust() {
	string s = to_string(N);
	int len = s.length();
	bool flag = false;
	for(int i = 0; i < len-1; i++) {
		if(s[i+1] < s[i]) {
			for(int j = i+1; j < len; j++) {
				s[j] = '9';
			}
			s[i]--;
			if(s[i] == '0' && i == 0) {
				s = s.substr(1);
			}
			flag = true;
//			cout << "i is " << i << " and s is " << s << endl;
			break;
		}
	}
	char conv[20];
	memset(conv, ' ', 20);
	for(int i = 0; i < s.length(); i++) {
		conv[i] = s[i];
	}
	N = atoll(conv);
	return flag;
}

void solve() {
	cin >> N;
	while(adjust()) {

	}
	cout << N << endl;
}

int main() {
	freopen("GCJ2017_QR_B.in", "r", stdin);
	freopen("GCJ2017_QR_B.out", "w", stdout);
	cin >> T;
	for(int i = 0; i < T; i++) {
		cout << "Case #" << (i+1) << ": ";
		solve();
	}
}
