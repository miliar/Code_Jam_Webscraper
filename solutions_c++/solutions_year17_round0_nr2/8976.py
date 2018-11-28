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

bool isTidy(int n) {
	string original = to_string(n);
	string sorted = to_string(n);
	sort(sorted.begin(), sorted.end());
	return sorted == original;
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("/home/mahmoud/Desktop/O1", "w", stdout);

	int testCases;
	cin >> testCases;
	for (int tc = 1; tc <= testCases; tc++) {
		int n;
		cin >> n;
		while (n) {
			if (isTidy(n)) {
				printf("Case #%d: %d\n", tc, n);
				break;
			}
			n--;
		}
	}
	return 0;
}

