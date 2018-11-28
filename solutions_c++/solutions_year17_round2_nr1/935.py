#include <bits/stdc++.h>
/*
TASK: hidden
LANG: C++11
*/
using namespace std;
typedef long long ll;
typedef pair<int, int> pair2;
typedef pair<int, pair<int, int> > pair3;
typedef pair<int, pair<int, pair<int, int> > > pair4;
#define MAXN 100000
#define MAXK 10
//#define INFINITY 1000000000000000LL
#define mp make_pair
#define add push_back
#define remove pop

int d, n, start[MAXN], speed[MAXN];
int main() {
	//freopen("cbs.in", "r", stdin);
	//freopen("cbs.out", "w", stdout);
	ios_base::sync_with_stdio(false); 
	cin.tie(NULL);

	int T;
	cin >> T;

	for (int asdf = 0; asdf < T; asdf++) {
		cin >> d >> n;

		 double longestTime = 0;
		for (int i = 0; i < n; i++) {
			cin >> start[i];
			cin >> speed[i];

			//cout << "success " << i << endl;
			longestTime = max(longestTime, (( double) d - start[i]) / speed[i]);
		}

		cout << setprecision(10) << "Case #" << asdf + 1 << ": " << ( double) d / longestTime << '\n';
	}
}