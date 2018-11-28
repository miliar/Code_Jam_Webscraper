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

int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		int n, c, m;
		cin >> n >> c >> m;


		int e1 = 0, e2 = 0;
		vector<int> a, b;

		map<int, int> aa, bb;

		for (int i = 0; i < m; i++) {
			int p, f;
			cin >> p >> f;
			if (p == 1) {
				if (f == 1) e1++; else e2++;
			} else {
				if (f == 1) a.pb(p); else b.pb(p);
			}
		}

		int cnt1 = 0, cnt2 = 0;
		int g1, g2;
		for (int i = 0; i < a.size(); i++) {
			aa[a[i]]++;
			if (aa[a[i]] > cnt1) {
				cnt1 = aa[a[i]];
				g1 = a[i];
			}
		}
		for (int i = 0; i < b.size(); i++) {
			bb[b[i]]++;
			if (bb[b[i]] > cnt2) {
				cnt2 = bb[b[i]];
				g2 = b[i];
			}
		}
		int tot1 = a.size();
		int tot2 = b.size();

		int ans1 = 0, ans2 = 0;
		for (int i = 0; i < e1; i++) {
			if (tot2 > 0) tot2--;
			if (cnt2 > 0) cnt2--;
		}
		for (int i = 0; i < e2; i++) {
			if (tot1 > 0) tot1--;
			if (cnt1 > 0) cnt1--;
		}
		ans1 += e1 + e2;

		int k = max(tot1, tot2);
		ans1 += k;

		if (g1 == g2) ans2 += max(0, cnt1 + cnt2 - k);

		cout << "Case #" << tt << ": " << ans1 << " " << ans2 << endl;

	}
	return 0;
}