#include <bits/stdc++.h>
using namespace std;


void solve() {
	int n, k;
	cin >> n >> k;
	multiset<int>ms;
	ms.insert(n);
	int ansmx, ansmn;
	while(k--) {
		multiset<int>::iterator it = ms.end();
		it--;
		int top = *it;
		ms.erase(it);
		if(top <= 1) {
			ansmx = 0;
			ansmn = 0;
			break;
		}
		if(top&1) {
			ansmx = top/2;
			ansmn = top/2;
		}
		else {
			ansmx = top/2;
			ansmn = top/2 - 1;
		}
		ms.insert(ansmx);
		ms.insert(ansmn);
	}
	cout << ansmx << " " << ansmn << "\n";
}


int main() {
	int tc;
	cin >> tc;
	for(int i=1;i<=tc;i++) {
		cout << "Case #" << i << ": ";
		solve();
	}
}