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

int main() {
#ifdef zzblack
	freopen("C:\\Users\\zzblack\\Desktop\\case.in","r",stdin);
    freopen("C:\\Users\\zzblack\\Desktop\\case.out","w",stdout);
#endif
    int T, cas = 1; cin >> T;
    while (T--) {
    	printf("Case #%d: ", cas++);
    	double Time = 0;
    	int n, k;
    	cin >> k >> n;
    	for (int i = 1; i <= n; i++) {
    		int pos, speed;
    		cin >> pos >> speed;
    		Time = max(Time, (k - pos) * 1.0 / speed);
    	}
    	printf("%.6f\n", k / Time);
    }

    return 0;
}

    
