#include <bits/stdc++.h>

long long n;
long long r;

void init() {
    std::cin >> n >> r;
}

void work() {
    std::map<long long, long long> cnt;

    cnt[n] = 1;
    while (true) {
        std::map<long long, long long>::iterator back = cnt.end();
        back--;

        if (back->second == 0LL) {
            cnt.erase(back);
            continue;
        }
        long long gapL, gapR;
        gapL = gapR = (back->first - 1LL) / 2LL;
        if (back->first % 2LL == 0) {
            gapR++;
        }
        if (r <= (back->second)) {
            std::cout << gapR << " " << gapL << std::endl;
            return ;
        } else {
            r -= back->second;
            cnt[gapL] += back->second;
            cnt[gapR] += back->second;
            cnt.erase(back);
        }

        // for (auto pair : cnt) {
        //     printf("cnt[%lld] = %lld, ", pair.first, pair.second);
        // }
        // printf("\n");
    }
}

int main() {
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);

    int testCount;
    std::cin >> testCount;
    for (int i = 1; i <= testCount; i++) {
        printf("Case #%d: ", i);
        init();
        work();
    }

    return 0;
}
