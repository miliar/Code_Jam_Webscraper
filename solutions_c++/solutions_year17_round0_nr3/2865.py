#include "stdafx.h"
#include "Qual_C.h"

void Qual_C::Solve() {
    long long n, k, factor = 1, cnt = 0;
    cin >> n >> k;
    map<long long, long long> h;
    set<long long> s;
    h[n] = 1;
    s.insert(n);

    while (!s.empty()) {
        long long cur = *s.rbegin();
        s.erase(cur);
        cnt += h[cur];
        if (cnt >= k) {
            cout << cur / 2 << " " << (cur - 1) / 2 << endl;
            return;
        }
        h[cur / 2] += h[cur];
        h[(cur - 1) / 2] += h[cur];
        s.insert(cur / 2);
        s.insert((cur - 1) / 2);
    }
}

Qual_C::Qual_C()
{
}


Qual_C::~Qual_C()
{
}
