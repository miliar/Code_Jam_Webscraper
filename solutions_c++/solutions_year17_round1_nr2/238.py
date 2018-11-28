#include <bits/stdc++.h>

typedef long long Int64;

const Int64 N = 60;

Int64 n;
Int64 p;
std::vector<Int64> vec[N];
Int64 r[N];

void init() {
    std::cin >> n >> p;
    for (Int64 i = 1; i <= n; i++) {
        scanf("%lld", &r[i]);
    }
    for (int i = 1; i <= n; i++) {
        vec[i].clear();
    }
    for (Int64 i = 1; i <= n; i++) {
        for (Int64 j = 1; j <= p; j++) {
            Int64 t;
            scanf("%lld", &t);
            vec[i].push_back(t);
        }
        std::sort(vec[i].begin(), vec[i].end(), std::greater<Int64>());
    }
}

void work() {
    Int64 answer = 0;
    for (Int64 k = 1; ; k++) {
        bool isEmpty = false;
        for (Int64 i = 1; i <= n; i++) {
            while (vec[i].empty() == false && vec[i].back() * 10 < r[i] * k * 9) {
                vec[i].pop_back();
            }
            if (vec[i].empty()) {
                isEmpty = true;
                break;
            }
        }
        if (isEmpty) {
            break;
        }

        while (true) {
            bool tag = true;
            for (Int64 i = 1; i <= n; i++) {
                if (vec[i].empty() || vec[i].back() * 10 > r[i] * k * 11) {
                    tag = false;
                    break;
                }
            }
            if (tag == true) {
                answer++;
                for (Int64 i = 1; i <= n; i++) {
                    vec[i].pop_back();
                }
            } else {
                break;
            }
        }
    }
    std::cout << answer << std::endl;
}

int main() {
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);

    Int64 testCount;
    std::cin >> testCount;
    for (Int64 i = 1; i <= testCount; i++) {
        printf("Case #%lld: ", i);
        init();
        work();
    }

    return 0;
}
