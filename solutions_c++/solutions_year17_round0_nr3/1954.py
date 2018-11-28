#include <iostream>
#include <vector>

using namespace std;

struct A {
    long long num;
    long long cnt;
};

struct Pair {
    long long L;
    long long R;
};

Pair compute(long long n) {
    Pair a;
    if (n & 1) {
        a.L = n >> 1;
    } else {
        a.L = (n >> 1) - 1;
    }
    a.R = n - a.L - 1;
    return a;
}

void addNext(A *next, int &cnt, long long n, long long k) {
    int i;
    for (i = 0; i < cnt; i++) {
        if (next[i].num == n) {
            next[i].cnt += k;
            return;
        }
    }
    int idx = cnt++; 
    for (; idx > 0 && next[idx - 1].num < n; idx--) {
        next[idx] = next[idx - 1];
    }
    next[idx].num = n;
    next[idx].cnt = k;
}

int main() {
    int tc, nt, i;
    int curCnt, nextCnt;
    long long n, k;
    A cur[100], next[100];

    cin >> nt;
    for (tc = 1; tc <= nt; tc++) {
        cout << "Case #" << tc << ": ";

        cin >> n >> k;
        cur[0].num = n;
        cur[0].cnt = 1;
        curCnt = 1;
        int found = 0;
        Pair res;
        while (!found) {
            nextCnt = 0;
            memset(next, 0, sizeof(next));
            for (i = 0; i < curCnt; i++) {
                Pair div = compute(cur[i].num);
                if (cur[i].cnt >= k) {
                    res = div;
                    found = 1;
                    break;
                } else {
                    k -= cur[i].cnt;
                    addNext(next, nextCnt, div.L, cur[i].cnt);
                    addNext(next, nextCnt, div.R, cur[i].cnt);
                }
            }
            curCnt = nextCnt;
            memcpy(cur, next, sizeof(cur));
        }
        cout << res.R << ' ' << res.L << endl;
    }
    return 0;
}
