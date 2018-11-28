#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <vector>
#include <stack>
#include <algorithm>
#define MOD 1000000007
#define forn(a, n) for(int a = 0; a<(int) (n); ++a)
#define dforn(a, n) for(int a = (n)-1; a>=0; --a)
#define forall(a, all) for(__typeof(all.begin()) a = all.begin(); a != all.end(); ++a)
#define EPS 0.000000000001
typedef long long tint;
using namespace std;

tint hd;
tint play(tint rhd, tint ad, tint hk, tint ak, tint b, tint d, tint rb, tint rd, tint t) {
	//cout << rhd << " " << ad << " " << hk << " " << ak << " " << b << " " << d << " " << rb << " " << rd << " " << t << endl;
	if(t >= 1000 || rhd<=0) return 100000;
	if(hk<=0) return 0;
	if(hk<=ad) return 1;
	
	if(rd > 0) {
		if(rhd-max(0LL,ak-d)<=0) {
			return 1+play(hd-ak,ad,hk,ak,b,d,rb,rd,t+1);
		}
		else {
			return 1+play(rhd-max(0LL,ak-d),ad,hk,ak-d,b,d,rb,rd-1,t+1);
		}
	}
	
	if(rb > 0) {
		if(rhd-ak<=0) {
			return 1+play(hd-ak,ad,hk,ak,b,d,rb,rd,t+1);
		}
		else {
			return 1+play(rhd-ak,ad+b,hk,ak,b,d,rb-1,rd,t+1);
		}
	}
	if(rhd-ak<=0) {
		return 1+play(hd-ak,ad,hk,ak,b,d,rb,rd,t+1);
	}
	return 1+play(rhd-ak,ad,hk-ad,ak,b,d,rb,rd,t+1);
}

int main()
{
#ifdef ACMTUYO
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
#endif
	int C;
	cin >> C;
	vector<vector<int> > DP;
	forn(tc, C) {
		tint ad, hk, ak, b, d;
		tint ans = 10000;
		cin >> hd >> ad >> hk >> ak >> b >> d;
		
		forn(cd, ak+1) {
			forn(cb, hk+1) {
				ans = min(ans, play(hd, ad, hk, ak, b, d, cb, cd, 0));
			}
		}
		cout << "Case #" << tc+1 << ": "; 
		if(ans<1000){
			cout << ans << endl;
		}
		else
		{
			cout << "IMPOSSIBLE" << endl;
		}
	}
}
