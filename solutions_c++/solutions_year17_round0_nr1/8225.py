#include <iostream>
#include <map>
#include <vector>
#include <set>
#include <algorithm>
#include <functional>
#include <cstdio>
#include <string>
#include <cmath>
using namespace std;

#define FOR(i,a,b)	for(int i=(a);i<(b);++i)
#define mp make_pair
#define pb push_back

typedef long long ll, int64;

map<char, char> flip;// = {{'-', '+'}, {'+', '-'}};

int main(void) {
	flip['-'] = '+';
	flip['+'] = '-';
	int nc, K;
	string s;
	cin >> nc;
	FOR (cs, 1, nc+1) {
		cin >> s >> K;
		int n = s.size();
		int cnt = 0;
		FOR (i, 0, n - K + 1) {
			if (s[i] == '-') {
				FOR (j, i, i + K) {
					s[j] = flip[s[j]];
				}
				cnt++;
			}
		}
		FOR (i, n - K + 1, n) {
			if (s[i] == '-') {
				cnt = -1;
			}
		}

		cout << "Case #" << cs << ": ";
		if (cnt == -1) {
			cout << "IMPOSSIBLE";
		}
		else {
			cout << cnt;
		}
		cout << endl;
	}	
}