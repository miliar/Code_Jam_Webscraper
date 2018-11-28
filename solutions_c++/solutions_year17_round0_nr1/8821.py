#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
//------------------------------------------------------------------
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define max3(a,b,c) max((a),max((b),(c)))
#define min3(a,b,c) min((a),min((b),(c)))
//------------------------------------------------------------------
#define isInteger(x) ((fabs((x)-round((x)))<EPS) ? true : false)
#define roundAns(x,d) round((x)*pow(10,(d)))/pow(10,(d))
//------------------------------------------------------------------
#define EPS 1e-8
#define PI 3.14159265358979323846
#define MAX
#define INF
//==================================================================

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int testCases, k;
	cin >> testCases;
	string s;
	for (int tc = 1; tc <= testCases; tc++) {
		cin >> s >> k;
		int cnt = 0;
		bool possible = true;
		for (int i = 0; i < (int) s.length(); i++) {
			if (s[i] == '-') {
				if ((int) s.length() - i < k) {
					possible = false;
					break;
				}
				cnt++;
				for (int j = i; j < i + k; j++) {
					s[j] = (s[j] == '-') ? '+' : '-';
				}
			}
		}
		for (int i = 0; i < (int) s.length(); i++) {
			if (s[i] == '-') {
				possible = false;
				printf("Case #%d: IMPOSSIBLE\n", tc);
				break;
			}
		}
		if (possible) {
			printf("Case #%d: %d\n", tc, cnt);
		}
	}
	return 0;
}

