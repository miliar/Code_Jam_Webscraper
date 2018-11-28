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

long double dp[55][55];

double calc(vector<double> a, int k) {
	int n = a.size();

	for (int i = 0; i <= n; i++) for (int j = 0; j <= k; j++) dp[i][j] = 0;

	dp[0][0] = 1;
	for (int i = 0; i < n; i++) for (int j = 0; j <= min(i, k); j++) {
		dp[i + 1][j] += dp[i][j] * (1 - a[i]);

		dp[i + 1][min(k, j + 1)] += dp[i][j] * a[i];
	}
	return dp[n][k];
}


int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		int n, k;
		cin >> n >> k;
		double s;
		cin >> s;
		vector<double> a(n);
		for (int i = 0; i < n; i++) cin >> a[i];

		while (s > 1e-9) {
			sort(a.begin(), a.end());

			double val = calc(a, k);

			double best = -1;
			vector<double> c;
			double ns;
			int l, r;

			for (int i = 0; i < 1; i++) for (int j = i; j < n; j++) {
				double to = 1;
				if (j < n - 1) to = a[j + 1];

				if (to - a[j] < 1e-7) continue;

				double us = min((to - a[j]) * (j - i + 1), s);
				double cha = us / (j - i + 1);

				vector<double> b = a;

				for (int k = i; k <= j; k++) b[k] += cha;

				double g = calc(b, k) - val;

				double prof = g / us;

				if (prof > best) {
					best = prof;
					c = b;
					ns = s - us;
				        l = i;
				        r = j;
				}
				break;
			}
			a = c;
			s = ns;
		}

		cout << "Case #" << tt << ": ";
		printf("%.10lf\n", calc(a, k));

		cerr << "test: " << tt << endl;

	}
	return 0;
}



