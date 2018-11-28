#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <algorithm>
using namespace std;

#define rep(i,n) for (int i=1;i<=(n);++i)
#define rep2(i,x,y) for (int i=(x);i<=(y);++i)
#define repr(i,x,y) for (int i=(y);i>=(x);++i)
#define pb push_back
#define mp make_pair
typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef pair<LL,LL> PLL;
typedef vector<PII> VII;

LL n, k;

PLL solve(LL n, LL k){
    if (k==1)
        return mp((n-1)/2+1-n%2, (n-1)/2);
    else 
        if ((k-1)%2 == 1)
            return solve((n-1)/2+1-n%2, (k-1)/2+1);
        else
            return solve((n-1)/2, (k-1)/2);
}

void MAIN(){
    cin >> n >> k;
    PLL ans = solve(n, k);
    cout << ans.first << ' ' << ans.second << endl;
}

int main() {
    // freopen("d:\\oi\\gcjr3\\A-large (1).in","r",stdin);
    // freopen("d:\\oi\\gcjr3\\A-large (1).out","w",stdout);
    int tt;
    cin >> tt;
    rep(i,tt)
    {
        printf("Case #%d: ",i);
        MAIN();
    }    
    return 0;
}