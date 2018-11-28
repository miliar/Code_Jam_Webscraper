#include <cstdio>
#include <map>
#include <iostream>

int main() {
    int T = 0;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        long long n, k;
        //std::cin >> n >> k;
        scanf("%I64d%I64d", &n, &k);
        //printf("%I64d%I64d\n", n, k);
        std::map<long long, long long> pre;
        pre[n] = 1;
        long long ans = 0;
        while (true) {
           // printf("k=%I64d\n", k);
            long long tot = 0;
            for (auto it = pre.rbegin(); it != pre.rend(); it++) {
                tot += it->second;
                if (tot >= k) {
                    ans = it->first;
                    break;
                }
            }
            if (ans != 0) break;
            k -= tot;
            std::map<long long, long long> cur;
            for (auto it = pre.rbegin(); it != pre.rend(); it++) {
                cur[(it->first - 1)/ 2] += it->second;
                cur[it->first / 2] += it->second;
            }
            pre = cur;
        }
        printf("Case #%d: %I64d %I64d\n", cas, ans / 2, (ans - 1) / 2);
    }
    return 0;
}
