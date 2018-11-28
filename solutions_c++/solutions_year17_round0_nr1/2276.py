#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;

int T, nCase;
string pancake;
int K;

void flip(int p)
{
	for (int i = p; i < p+K; ++i) {
		pancake[i] = '+' + '-' - pancake[i];
	}
}

int solv()
{
	int cnt = 0;
	for (int i = 0; i < pancake.size(); ++i) {
		if (pancake[i] == '-') {
			if (i + K <= pancake.size()) {
				flip(i);
				++ cnt;
			} else {
				return -1;
			}
		}
	}
	return cnt;
}

int main ()
{
	cin >> T;
	for (nCase = 1; nCase <= T; ++nCase) {
		cin >> pancake >> K;
		cout << "Case #" << nCase << ": ";
		int ans = solv();
		if (ans < 0)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << ans << endl;
	}
	return 0;
}