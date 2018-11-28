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

int N, P;
int R[100];
map<PII, int> T[100];

int run() {
	scanf("%d %d", &N, &P);
	for(int i=0;i<N;++i) scanf("%d",&R[i]);
	vector<int> X;
	for(int i=0;i<N;++i) {
		T[i].clear();
		//cerr << ">> Group#"<<i<<" ..." << endl;
		for(int j=0;j<P;++j) {
			int x;
			scanf("%d", &x);
			if (x * 10 < 9 * R[i]) continue;
			int r = x * 10 / (9 * R[i]);
			int l = max((x * 10 + 11 * R[i] - 1) / (11 * R[i]), 1);
			if (l > r) continue;
			T[i][mkp(r,l)] ++ ;
			X.push_back(l);
			X.push_back(r);
			//cerr << "("<<l<<","<<r<<") ";
		}
		cerr << endl;
	}
	sort(X.begin(),X.end());
	X.erase(unique(X.begin(), X.end()), X.end());
	int ans = 0;
	for(auto k: X) {
		while(true) {
			int inc = N * P;
			for(int i=0;i<N && inc > 0;++i) {
				while(T[i].size() > 0 && T[i].begin()->first.x < k)
					T[i].erase(T[i].begin()->first);
				if (T[i].size() == 0) {
					return ans;
				}
				if (T[i].begin()->first.y > k) inc = 0;
				else {
					inc = min(inc, T[i].begin()->second);
				}
			}
			if(! inc) break;
			ans += inc;
			for(int i=0;i<N;++i) {
				T[i].begin()->second -= inc;
				if (!T[i].begin()->second) {
					T[i].erase(T[i].begin()->first);
				}
			}
		}
	}
	return ans;
}

int main() {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;
	cin >>T;
	for (int i=1;i<=T;++i) {
		int ans = run();
		printf("Case #%d: %d\n", i, ans);
		//cerr << "ok!  ans = "<<ans << endl;
		
	}
}
