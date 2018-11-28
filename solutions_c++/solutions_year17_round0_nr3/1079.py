#include <cstdio>
#include <cstring>
#include <map>
#include <utility>

using namespace std;

typedef unsigned long long ull;

map<ull, ull> m;
ull n, q;

void debug() {
    printf("q = %llu\n", q);
    for (map<ull, ull>::iterator it = m.begin(); it != m.end(); it++) {
        printf("%llu --- %llu\n", it->first, it->second);
    }
    printf("==================\n");
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        m.clear();
        scanf("%llu%llu", &n, &q);
        m[n] = 1;
        ull block = 0ULL;
        while (true) {
            map<ull, ull>::iterator it = --m.end();
            ull len = it->first;
            ull cnt = it->second;
            m.erase(it);

            if (q <= cnt) {
                q = 0ULL;
                block = len;
                break;
            }
            q -= cnt;

            ull l = (len-1)/2;
            ull r = len/2;

            it = m.find(l);
            if (it == m.end()) {
                m.insert(make_pair(l, cnt));
            } else {
                it->second += cnt;
            }

            it = m.find(r);
            if (it == m.end()) {
                m.insert(make_pair(r, cnt));
            } else {
                it->second += cnt;
            }

            // debug();
        }
        printf("Case #%d: %llu %llu\n", t, block/2, (block-1)/2);
    }
    return 0;
}

