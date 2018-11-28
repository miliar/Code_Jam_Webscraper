#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<cassert>
using namespace std;

#define LL long long
#define PII pair<int,int>
#define x first
#define y second
#define mkp(a,b) make_pair(a,b)

int solve(int o_h1,int a1,int o_h2,int a2, int b,int d,int k_b, int k_d) {
	int ret =0;
	int h1=o_h1, h2=o_h2;
	// run k_d debuf
	for(int i=1;i<=k_d;++i) {
		if (h1 - max(0, a2-d) <= 0) {
			++ ret; // cure
			h1 = o_h1 - a2; // be attacked
			if(h1 <= 0) return -1;
		}
		a2 = max(0, a2 - d); // debuf
		++ ret;
		// attack you
		h1 -= a2;
		if(h1 <= 0) return -1;
	}
	// run k_b buff
	for(int i=1;i<=k_b;++i) {
		if (h1 - a2 <= 0) {
			++ ret; // cure
			h1 = o_h1 - a2; // be attacked
			if(h1 <= 0) return -1;
		}
		a1 += b; // buff
		++ ret;
		// attack you
		h1 -= a2;
		if(h1 <= 0) return -1;
	}
	// keep attack each other
	if (a1 == 0) return -1;
	while(h2 > 0) {
		if (h2 <= a1) return ++ ret; // killed
		if (h1 - a2 <= 0) {
			++ ret; // cure
			h1 = o_h1 - a2;
			if(h1 <= 0) return -1;
		}
		h2 -= a1; // attack
		++ ret;
		h1 -= a2; // be attacked
		if (h1 <= 0) return -1;
	}
	return ret;
}

int run() {
	int h1,a1,h2,a2,b,d;
	cin >> h1 >> a1 >> h2 >> a2 >> b >> d;
	if (a1 >= h2) {
		cout << 1 << endl;
		return 0;
	}
	int n_buff = 0, n_debuf = 0;
	if (b > 0) n_buff = h2 - a1;
	if (d > 0) n_debuf = a2;
	int ans = -1;
	for(int k_buf = 0; k_buf <= n_buff; ++k_buf) 
		for(int k_deb = 0; k_deb <= n_debuf; ++ k_deb) {
			//cerr << "buf = "<<k_buf<<"  debuf = "<<k_deb<<endl;
			int c = solve(h1,a1,h2,a2,b,d,k_buf,k_deb);
			//cerr << "   -> c = "<<c<<endl;
			if (c > -1) {
				if(ans < 0 || c < ans)
					ans = c;
			}
		}
	if(ans < 0) puts("IMPOSSIBLE");
	else printf("%d\n", ans);
}

int main() {
	freopen("C-small.in","r",stdin);
	freopen("C-small.out","w",stdout);
	int T;
	cin >>T;
	for (int i=1;i<=T;++i) {
		printf("Case #%d: ", i);
		run();
	}
}
