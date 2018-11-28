//g++ -std=c++0x your_file.cpp -o your_program
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <math.h>
#include <vector>
#include <cstring>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <set>
#define fname ""
#define mp make_pair
#define F first
#define pb push_back
#define S second
#define ub upper_bound
#define lb lower_bound
#define inf 2000000000
#define INF 2000000000000000000ll
using namespace std;

inline void solve() {
	string s;
	int k;
	cin >> s;
	cin >> k;
	int answer = 0;
	for (int i = 0; i + k <= (int)s.length(); i++) {
		if (s[i] == '-') {
			answer++;
			for (int j = 0; j < k; j++) {
				if (s[i + j] == '-') {
					s[i + j] = '+';
				}
				else {
					s[i + j] = '-';
				}
			}
		}
	}
	for (int i = 0; i < (int)s.length(); i++) {
		if (s[i] == '-') {
			answer = -1;
			break;
		}
	}
	if (answer == -1) {
		cout << "IMPOSSIBLE\n";
	}
	else {
		cout << answer << endl;
	}
}

int main() {
	freopen (fname"A-large.in.txt", "r", stdin);
	freopen (fname"out.txt", "w", stdout);
	ios_base::sync_with_stdio(0);
	int T;
	cin >> T;
	for (int Case = 1; Case <= T; Case++) {
		cout << "Case #" << Case << ": ";
		solve();
	}
	return 0;
}
