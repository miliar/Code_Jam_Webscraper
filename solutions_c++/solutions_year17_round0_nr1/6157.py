#include <bits/stdc++.h>
#define DEBUG(x) cout << #x << " :" << x << endl;
using namespace std;

char s[1001];
int K;

void flip(int be, int en, int len){
	while(en <= len && be < en){
		if (s[be] == '+') s[be] = '-';
		else if (s[be] == '-') s[be] = '+';
		++be;
	}
}

bool verify(){
	int i = 0;
	while(s[i]){
		if (s[i] == '-') return false;
		++i;
	}
	return true;
}

int sol(){
	int i = 0;
	int len = strlen(s);
	int n = 0;
	while(i < len && s[i]){
		if (s[i] == '+') {
			++i;
			continue;
		}

		flip(i, i + K, len);
		++n;
		++i;
	}

	bool passed = verify();
	if (!passed) return -1;
	return n;
}

int main(){
	int T;
	cin >> T;
	int cnt = 0;
	while(T--){
		cin >> s >> K;
		++cnt;
		int ans = sol();
		if (ans == -1) cout << "Case #" << cnt << ": " << "IMPOSSIBLE" << endl;
		else cout << "Case #" << cnt << ": " << ans << endl;
	}

	return 0;
}