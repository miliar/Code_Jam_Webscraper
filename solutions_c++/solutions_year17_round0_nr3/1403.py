#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>

using namespace std;

void print(const vector<int>& o) {
    for (auto it : o) {
        cout << it << ' ';
    }
    cout << endl;
}

vector<int> decompose(int o, int lv) {
    if (!lv) return vector<int>{o};
    auto a = decompose(o/2, lv-1);
    auto b = decompose(o/2-(!(o&1)), lv-1);
    for (auto it : b) a.push_back(it);
    cout << o << ": ";
    print(a);
    return a;
}

long long solve(long long l, long long n) {
    long long ca, cb, a, b, cnt;
    a = l, b = a-1, ca = 1, cb = 0;
    cnt = 0;
    for (long long t = 1; 1;t *= 2) {
        cnt += t;
        if (cnt >= n) {
            cnt -= t; break;
        }
        long long nca = 0, ncb = 0;
        if (a & 1) {
            nca = 2*ca + cb, ncb = cb;
        } else {
            nca = ca, ncb = ca + 2*cb;
        }
        a /= 2;
        b = a-1;
        ca = nca, cb = ncb;
    }
    long long rest = n - cnt;
    if (rest <= ca) return a;
    else return b;
}

int main() {
#ifdef D
    // freopen("C.in", "r", stdin);
#endif
    int T; cin >> T;
    for (int kase = 1; kase <= T; kase++) {
        long long n, l; cin >> l >> n;
        long long v = solve(l, n);
        printf("Case #%d: ", kase);
        printf("%lld %lld\n", v/2, (v-1)/2);
    }
    return 0;
}