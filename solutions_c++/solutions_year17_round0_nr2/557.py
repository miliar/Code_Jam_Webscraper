#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstdio>
#include <cmath>
#include <queue>
#include <map>
#include <cstdio>
#include <set>
#include <cstring>
using namespace std;

int a[2000];

void solve() {
	string s;
	int n;
	cin >> s;
	n = s.length();
	if (n==1) {
		cout << s;
		return;
	}
	for (int i = 0; i < n; ++i )
		a[i] = s[i] - '0';
	for (int i = n-1; i >= 1; --i ) {
		if (a[i-1]>a[i]) {
			a[i-1] -=1;
			for (int j = i; j < n; ++j )
				a[j] = 9;
		}
	}
	int i = 0;
	if (a[i]==0) ++i;
	for (; i < n; ++i )
		cout << a[i];
}

int main(int argc, char *argv[]) {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int testNum;
	cin >> testNum;
	for (int testid = 0; testid < testNum; ++testid ) {
		cout << "Case #" << testid+1 << ": ";
		solve();
		cout << endl;
	}
}