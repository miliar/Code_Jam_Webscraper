#include <bits/stdc++.h>

#define eb emplace_back
#define fi first
#define se second
#define mp make_pair
#define INF 0x3f3f3f3f

using namespace std;

typedef pair<int, int> pii;
typedef long long ll;
typedef vector<int> vi;
const int N = 100010;

bool valid (string &s) {
	for (auto c : s) if (c == '-') return false;
	return true;
}
int main (void) {
	int t; cin >> t;
	for (int cases = 1; cases <= t; cases++) {
		printf("Case #%d: ", cases);
		int n;
		string s; 
		cin >> s >> n;
		//---->
		string s1 = s;
		int cnt = 0;
		for (int i = 0; i + n - 1 < s1.size(); i++) {
			if (s1[i] == '+') continue;
			for (int j = i; j < i + n; j++) s1[j] = s1[j] == '+' ? '-' : '+';
			cnt++;
		}
		//<-----
		string s2 = s;
		int cnt2 = 0;
		for (int i = s1.size()-1; i - n + 1 >= 0; i--) {
			if (s2[i] == '+') continue;
			for (int j = i-n+1; j <= i; j++) s2[j] = s2[j] == '+' ? '-' : '+';
			cnt2++;
		}

		if (valid(s1) and valid(s2)) cout << min(cnt, cnt2) << endl;
		else if (valid(s1)) cout << cnt << endl;
		else if (valid(s2)) cout << cnt2 << endl;
		else cout << "IMPOSSIBLE\n";
	}
	return 0;
}
