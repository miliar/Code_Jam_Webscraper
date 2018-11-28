#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <map>
using namespace std;
typedef long long LL;
int T;
LL n,K;

int main(){
	//	freopen("c.txt", "r", stdin);
	//	freopen("ans.txt", "w", stdout);
	scanf("%d",&T);
	for (int tt = 1; tt <= T; tt++){
		scanf("%lld%lld\n", &n, &K);
		map<LL, LL> a;
		map<LL, LL> ::iterator it;
		a[n] = 1;
		LL ans = -1;
		while (K){
			it = a.end();
			it--;
			LL v = it->first; LL d = it->second;
			//cout << v << "  " << d << endl;
			if (d >= K) {ans = v;break;}
			a.erase(it);
			v--;
			K -= d;
			int flag = 0;
			if (v & 1) flag = 1;
			a[v / 2] += d;
			a[v / 2 + flag] += d;
		}
		//cout << ans << endl;
		ans--;
		int flag = 0;
		if (ans & 1) flag = 1;
		printf("Case #%d: %lld %lld\n",tt,ans / 2 + flag, ans / 2);
	}
	return 0;
}
