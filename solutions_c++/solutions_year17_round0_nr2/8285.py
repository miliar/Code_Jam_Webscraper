#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;
typedef long long LL;
LL prev(LL x) {
    int n = 0;
    while (x%10 == x/10%10) {
        ++n;
        x/=10;
    }
    int d = x%10 - 1;
    --x;
    while(n--){
        x=x*10+9;
    }
    return x;
}
int main() {
    int T;
    scanf("%d", &T);
    for (int cs = 1; cs <= T; ++cs) {
        LL ans = 0, x;
        scanf("%lld", &x);
        vector<int> d;
        while (x>0) {
            d.push_back(x % 10);
            x/=10;
        }
        int curr = 0;
        bool less = 0;
        for (int i = d.size() - 1; i >= 0; --i) {
            if (less) {
                ans = ans * 10 + 9;
                continue;
            }
            if (d[i] >= curr) {
                ans = ans * 10 + d[i];
                curr = d[i];
            } else {
                //printf("%d %d\n", d[i], curr);
                ans = prev(ans);
                less = 1;
                ans = ans * 10 + 9;
            }
        }
        printf("Case #%d: %lld\n", cs, ans);
    }
}
