#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
using namespace std;

typedef long long LL;

struct stall {
    LL len, num;
    stall(LL len, LL num) : len(len), num(num) {}
    bool operator < (const stall &rhs) const {
        return len < rhs.len;
    }
};

int second, cas = 1;
LL N, K;
int main() {
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);
    scanf("%d", &second);
    while (cas <= second) {
        scanf("%lld %lld", &N, &K);
        LL ans;
        map<LL, LL, greater<LL> > q;
        q[N] = 1LL;
        LL cnt = 0LL;
        for(;;) {
            map<LL, LL, greater<LL> >::iterator cur = q.begin();
            LL len = cur->first, num = cur->second;
            q.erase(cur);
            cnt += num;
            if (cnt >= K) {
                ans = len;
                break;
            }
            if ((len - 1LL) & 1LL) {
                if (q.find((len - 1LL) / 2LL) == q.end())
                    q[(len - 1LL) / 2LL] = num;
                else
                    q[(len - 1LL) / 2LL] += num;
                if (q.find((len - 1LL) - (len - 1LL) / 2LL) == q.end())
                    q[(len - 1LL) - (len - 1LL) / 2LL] = num;
                else
                    q[(len - 1LL) - (len - 1LL) / 2LL] += num;
            }
            else {
                if (q.find((len - 1LL) / 2LL) == q.end())
                    q[(len - 1LL) / 2LL] = num * 2LL;
                else
                    q[(len - 1LL) / 2LL] += num * 2LL;
            }
        }
        --ans;
        printf("Case #%d: %lld %lld\n", cas, ans - ans / 2LL, ans / 2LL);
        cas++;
    }
    return 0;
}