#include<stdio.h>
#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<memory.h>
#include<map>
#include<set>
#include<queue>
#include<list>
#include<sstream>
#define mp make_pair
#define pb push_back      
#define F first
#define S second
#define SS stringstream
#define sqr(x) ((x)*(x))
#define m0(x) memset(x,0,sizeof(x))
#define m1(x) memset(x,63,sizeof(x))
#define CC(x) cout << (x) << endl
#define pw(x) (1ll<<(x))
#define M 1000000007
#define N 111111
using namespace std;
typedef pair<int,int> pt;

int r[N], h[N];

int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		int n, k;
		cin >> n >> k;

		for (int i = 0; i < n; i++) cin >> r[i] >> h[i];

		double ans = 0;

		for (int i = 0; i < n; i++) {
			vector<double> e;

			double val = acos(-1) * r[i] * r[i] + acos(-1) * r[i] * 2 * h[i];

			for (int j = 0; j < n; j++) if (i != j && r[j] <= r[i]) e.pb(acos(-1) * r[j] * 2 * h[j]);

			if (e.size() < k - 1) continue;

			sort(e.rbegin(), e.rend());

			for (int j = 0; j < k - 1; j++) val += e[j];

			ans = max(ans, val);
		}

		cout << "Case #" << tt << ": ";
		printf("%.10lf\n", ans);

	}
	return 0;
}