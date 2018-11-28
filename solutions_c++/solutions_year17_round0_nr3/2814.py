#include <cstdio>
#include <map>

std::map<long long, long long> m;

void debug() {
    printf("###\n");
    for (auto& it : m) {
        printf("%lld %lld\n", it.first, it.second);
    }
}

int main() {
    int T;
    scanf("%d", &T);
    for (int w = 1; w <= T; w++) {
        m.clear();
        long long a, K;
        scanf("%lld %lld", &a, &K);
        m[a] = 1;
        while (true) {
            auto it = m.end();
            it--;
//            debug();
//            printf("!%lld %d!\n", it->first, it->second);
            if (it->second < K) {
                long long left = (it->first - 1) / 2;
                long long right = it->first / 2;
                m[left] += it->second;
                m[right] += it->second;
                K -= it->second;
                m.erase(it);
            } else {
                long long left = (it->first - 1) / 2;
                long long right = it->first / 2;
                printf("Case #%d: %lld %lld\n", w, right, left);
                break;
            }
        }
    }
    return 0;
}