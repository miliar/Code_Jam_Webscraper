#include <cstdio>
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <map>
#include <set>
#define fi first
#define se second
using namespace std;
typedef long long LL;
typedef pair<LL,LL> Pair;
const int MOD = 1e9+7;
const int maxn = 1e3+10;
Pair solve(LL n,LL k){

    if(k==1)return Pair((n-1)/2,n/2);
    if(k&1)return solve((n-1)/2,k/2);
    else return solve(n/2,k/2);
}

int main(int argc, char const *argv[]) {
    int kase =0;
    int T;cin>>T;
    while (T--) {
        LL n,k;
        cin>>n>>k;
        Pair ans = solve(n,k);
        printf("Case #%d: %lld %lld\n",++kase,max(ans.fi,ans.se),min(ans.fi,ans.se) );
    }
    return 0;
}
