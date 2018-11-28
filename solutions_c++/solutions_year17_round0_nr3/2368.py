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
		long long n, k;
		cin >> n >> k;
		map<long long, long long> Q;
		Q[n] += 1;

		pair<long long, long long> ans = mp(-1, -1);

		while (k > 0) {
			auto g = (Q.end());
			g--;	

			auto e = *g;
			Q.erase(e.F);
			if (e.S == 0) continue;

			if (k <= e.S) {
				ans = mp(e.F / 2, (e.F - 1) / 2);
				break;
			}
			Q[e.F / 2] += e.S;
			Q[(e.F - 1) / 2] += e.S;
			k -= e.S;
		}

		cout << "Case #" << tt << ": " << ans.F << " " << ans.S << endl;

	}
	return 0;
}