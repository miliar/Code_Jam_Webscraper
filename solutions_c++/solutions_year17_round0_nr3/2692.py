#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
long long o[2], tmp[2];
long long dfs(long long x, long long y, long long sum) {
    tmp[0] = o[0];
    tmp[1] = o[1];
    o[0] = o[1] = 0;
    long long k = tmp[0] + tmp[1];
    if(sum - k <= 0) {
        if(sum - tmp[1] <= 0) return y;
        else return x;
    }
    if(x & 1) {
        o[0] = tmp[0] * 2 + tmp[1];
        o[1] = tmp[1];
        return dfs(x/2, (x+1)/2, sum - k);
    }
    else {
        o[0] = tmp[0];
        o[1] = tmp[0] + tmp[1] * 2;
        return dfs((x-1)/2, x/2, sum - k);
    }
}
int main() {
    int t, tc;
    long long n, m;
    long long ans;
    //freopen("/Users/SeoByeongChan/Desktop/input.txt","rt",stdin);
    //freopen("/Users/SeoByeongChan/Desktop/output.txt","w",stdout);
    scanf("%d",&tc);
    for(t=1;t<=tc;t++) {
        scanf("%lld %lld",&n,&m);
        if(n & 1) {
            o[0] = 1;
            o[1] = 0;
            ans = dfs(n, n+1, m);
        }
        else {
            o[0] = 0;
            o[1] = 1;
            ans = dfs(n-1, n, m);
        }
        
        printf("Case #%d: %lld %lld\n",t, ans/2, (ans-1)/2);
    }
    return 0;
}
