#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <string>
#include <fstream>

#define IN_FILE "A-large.in"
#define OUT_FILE "outL.txt"

using namespace std;

typedef long long ll;
typedef long double ld;

char str[1003];

int main() {
	ios::sync_with_stdio(0);
	ifstream xin(IN_FILE);
	ofstream xout(OUT_FILE);
	cin.rdbuf(xin.rdbuf());
	cout.rdbuf(xout.rdbuf());
	int t;
	int tc = 1;
	cin >> t;
	while (t--) {
		int k;
		cin >> str >> k;
		int n = strlen(str);
		ll ans = 0;
		for (int i = 0; i < n-k+1; i++) {
			if (str[i] == '-') {
				ans++;
				for (int j = i; j < i + k; j++) {
					if (str[j] == '-')
						str[j] = '+';
					else
						str[j] = '-';
				}
			}
		}
		bool failed = false;
		for (int i = 0; i < n; i++) {
			if (str[i] == '-') {
				failed = true;
				break;
			}
		}
		if (failed) 
			cout << "Case #" << tc << ": IMPOSSIBLE\n";
		else
			cout << "Case #" << tc << ": " << ans << "\n";
		tc++;
	}
	system("pause");
	return 0;
}
