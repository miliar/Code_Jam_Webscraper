#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<algorithm>
#include<bitset>
#include<vector>
#include<deque>
#include<queue>
#include<map>
#include<set>
#include<stack>
#include<cmath>
#include<iomanip>
#include <functional>
using namespace std;
typedef long long ll;
const int mod = 1000000007;
const int INF = 1 << 28;
const double EPS = 1e-10;
//cout << fixed << std::setprecision(9)
//memset(a, 0, sizeof(a));
//--------------------------


int t,k;
string s;

void parse(string s, int k)
{
	int ans = 0;
	int n = s.size();

	for (int i = 0;i < n - k;i++) {
		if (s[i] == '-') {
			for (int j = i;j < i + k;j++) {
				if (s[j] == '-') s[j] = '+';
				else s[j] = '-';
			}
			ans++;
		}
	}

	int subcount = 0;
	for (int i = n - k;i < n;i++) {
		if (s[i] == '-') subcount++;
	}

	if (subcount == 0) {
		cout << ans << endl;
		return;
	}

	if (subcount < k) {
		cout << "IMPOSSIBLE" << endl;
		return;
	}
	else {
		cout << ans+1 << endl;
	}
}

int main()
{
	cin >> t;

	for (int i = 0;i < t;i++) {
		cin >> s >> k;
		cout << "Case #" << i+1 << ": ";
		parse(s, k);
	}
	return 0;
}






