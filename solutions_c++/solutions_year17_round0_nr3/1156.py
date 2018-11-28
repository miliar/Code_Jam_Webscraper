#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <bitset>
#include <string>
#include <cctype>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
#define ls id<<1,l,mid
#define rs id<<1|1,mid+1,r
#define OFF(x) memset(x,-1,sizeof x)
#define CLR(x) memset(x,0,sizeof x)
#define MEM(x) memset(x,0x3f,sizeof x)
typedef long long ll ;
typedef pair<ll,ll> pii ;
const int maxn = 150 ;
const int maxm = 1e6 + 50;
const double eps = 1e-10;
const int max_Index = 62;
const int inf = 0x3f3f3f3f ;
const int MOD = 1e9+7 ;

struct sta
{
	ll len;
	ll num;
	sta(){}
	sta(ll num, ll len) :num(num), len(len) {}
	bool operator < (const sta &rhs) const {
		if (len == rhs.len) return num < rhs.num;
		return len > rhs.len;
	}

};

void Insert(set<sta> &S, ll num, ll len) {
	if (len == 0) return;
	set<sta>::iterator it = S.lower_bound(sta(0, len));
	if (it != S.end() && it->len == len) {
		sta u = *it; S.erase(it);
		u.num += num;
		S.insert(u);
	} else S.insert(sta(num, len));
}


int main() {
#ifdef zzblack
	freopen("C:\\Users\\zzblack\\Desktop\\case.in","r",stdin);
    freopen("C:\\Users\\zzblack\\Desktop\\case1.out","w",stdout);
#endif
    int T, cas = 1; cin >> T;
    while (T--) {
    	printf("Case #%d: ", cas++);
    	ll n, k; cin >> n >> k;
    	// n *= 100000;
    	set<sta> S;
    	S.insert(sta(1, n));
    	k--;
    	while (k) {
    		sta u = *S.begin(); S.erase(S.begin());
    		ll x = min(k, u.num);
    		k -= x;
			u.num -= x;
			if (u.num) S.insert(u);
    		if (u.len & 1) Insert(S, x << 1, u.len >> 1);
    		else if (u.len) {
    			Insert(S, x, u.len >> 1);
    			Insert(S, x, u.len - 1 >> 1);
    		}
    	}
    	ll ansl = S.begin()->len / 2;
    	ll ansr = S.begin()->len - ansl - 1;
    	if (ansr < 0) ansr = 0;
    	cout << max(ansl, ansr) << ' ' << min(ansl, ansr) << '\n';

    }


    return 0;
}

    
