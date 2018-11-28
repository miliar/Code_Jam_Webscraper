#include<iostream>
#include<cstdio>
#include<set>
#include<map>

using namespace std;

int main() {
    int T; cin >> T;
    for (int tt = 1; tt <= T; tt++) {
        cerr << tt << endl;
        long long N, K; cin >> N >> K;
        map<long long, long long, greater<long long> > m;
        m[N] = 1LL;
        K -= 1;
        while (K > 0) {
            pair<long long, long long> top = *m.begin();
            long long mini = top.second;
            if (mini > K) {
                mini = K;
            }
            K -= mini;
            long long space = top.first;
            long long L = (space - 1) / 2;
            long long R = (space - 1) - L;
            m[space] -= mini;
            if (m[space] == 0) {
                m.erase(m.begin());
            }
            m[L] += mini;
            m[R] += mini;
        }

        printf("Case #%d: ", tt);

        pair<long long, long long> top = *m.begin();
        long long space = top.first;
        long long L = (space - 1) / 2;
        long long R = (space - 1) - L;
        if (L > R) {
            printf("%lld %lld\n", L, R);
        } else {
            printf("%lld %lld\n", R, L);
        }

        m.clear();

    }
    return 0;
}