#include <iostream>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>

using namespace std;
#define lli long long int
const int N = 1e3 + 10;

const int MAXN = 2e4; // число вершин
const int INF = 1000000000; // константа-бесконечность
 
int main() {
    ios_base::sync_with_stdio();
	int T;
	cin >> T;
	for (int qq = 0; qq < T; ++qq) {
		cout << "Case #" << (qq + 1) << ": ";
		string s;
		cin >> s;
		vector<bool> ok(s.size());
		ok[0] = 1;
		for (int i = 1; i < s.size(); ++i) ok[i] = ok[i - 1] && s[i] >= s[i - 1];
		if (ok.back()) {
			cout << s << endl;
			continue;
		}
		bool done = false;
		for (int i = (int)s.size() - 2; i >= 0; i--) {
			if (ok[i] && s[i] - 1 >= (i > 0 ? s[i - 1]: '1')) {
				for (int j = 0; j < i; ++j) cout << s[j];
				cout << (char)(s[i] - 1);
				for (int j = i + 1; j < s.size(); ++j) cout << 9;
				cout << endl;
				done = 1;
				break;
			}
		}
		if (!done) {
			for (int i = 0; i < s.size() - 1; ++i) cout << 9;
			cout << endl;
		}
	}
    return 0;
}