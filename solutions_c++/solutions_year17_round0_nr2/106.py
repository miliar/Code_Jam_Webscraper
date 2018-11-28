#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <queue>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

#define INF 1000000000
#define FOR(i, a, b) for(int i=int(a); i<int(b); i++)
#define FORC(cont, it) for(decltype((cont).begin()) it = (cont).begin(); it != (cont).end(); it++)
#define pb push_back

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;

int main() {
	int T, caso=1;
	cin >> T;
	string N;
	while (T--) {
		cin >> N;
		string ans = N;
		FOR(i, 1, N.length()) {
			if (N[i] < ans[i-1]) {
				int j = i - 1;
				while (j>=0 && ans[j] > ans[j + 1]) {
					ans[j--]--;
				}
				j += 2;
				while (j < ans.length()) ans[j++] = '9';
				break;
			}
			else ans[i] = N[i];
		}
		if (ans[0] == '0') ans = ans.substr(1);
		cout << "Case #" << caso++ << ": " << ans;
		cout << endl;
	}
	return 0;
}
