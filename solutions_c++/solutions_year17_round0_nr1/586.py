#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;

void flip(char &c) {
	if(c == '-') c = '+';
	else c = '-';
}

int getMinimumFlip(string s, int k) {
	int ret = 0;
	for(int i = 0 ; i+k-1 < s.length() ; i++)
		if(s[i] == '-') {
			ret++;
			for(int j = 0 ; j < k ; j++)
				flip(s[i+j]);
		}

	for(int i = 0 ; i < s.length() ; i++)
		if(s[i] == '-') {
			return INF;
		}

	return ret;
}

int main() {
	int t; cin >> t;
	for(int tc = 1 ; tc <= t ; tc++) {
		string s;
		int k;
		cin >> s >> k;

		string revS = s; reverse(revS.begin(), revS.end());

		int ret = min(getMinimumFlip(s, k), getMinimumFlip(revS, k));

		printf("Case #%d: ", tc);
		if(ret == INF) {
			printf("IMPOSSIBLE\n");
		} else {
			printf("%d\n", ret);
		}
	}
	return 0;
}