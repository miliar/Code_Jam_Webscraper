#include <iostream>
#include <sstream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cstring>
#include <cmath>
using namespace std;

#define Rep(i,n) for(int i=0;i<(n);++i)
#define For(i,a,b) for(int i=(a);i<=(b);++i)
#define Ford(i,a,b) for(int i=(a);i>=(b);--i)
#define fi first
#define se second
#define pb push_back
#define MP make_pair

typedef pair<int,int> PII;
typedef vector<int> VI;


long long process(long long st, long long en, long long id) {
    if (id == 0) {
        return en - st;
    }

    long long mid = (en + st) / 2;

    long long len = en - st + 1;
    long long p2 = 1;
    long long total = 0;
    while (total + p2 <= len) {
        total += p2;
        p2 = 2 * p2;
    }
    long long remain = len - total;
    long long leftLeaves = remain / 2;
    long long rightLeaves = remain - remain / 2;

    if (id >= total) {
        if (id >= total + leftLeaves) {
            long long newId = id - leftLeaves - p2 / 2;
            return process(mid + 1, en, newId);
        } else {
            long long newId = id - p2 / 2;
            return process(st, mid - 1, newId);
        }
    } else {
        p2 = 1;
        total = 0;
        while (total + p2 <= id) {
            total += p2;
            p2 *= 2;
        }
        // cout << p2 << " " << remain << endl;
        remain = (remain % p2);
        long long leftBefore = remain / 2;
        long long rightBefore = remain - leftBefore;
        long long leftAfter = p2 / 2 - leftBefore;
        long long rightAfter = p2 / 2 - rightBefore;
        // cout << leftBefore << " " << rightBefore << " " << leftAfter << " " << rightAfter << endl;
        long long rid = id - total;
        if (rid < leftBefore) {
            // cout << "go left" << endl;
            return process(st, mid - 1, id - p2 / 2);
        } else if (rid < leftBefore + rightBefore) {
            // cout << "go right" << endl;
            return process(mid + 1, en, id - p2 / 2 - leftBefore);
        } else if (rid < leftBefore + rightBefore + leftAfter) {
            // cout << "go left" << endl;
            return process(st, mid - 1, id - p2 / 2 - rightBefore);
        } else {
            // cout << "go right" << endl;
            return process(mid + 1, en, id - p2 / 2 - leftBefore - leftAfter);
        }
    }
}

int main() {
    int nt;
    cin >> nt;
    Rep(t, nt) {
        long long n, k;
        cin >> n >> k;
        long long res = process(0, n - 1, k - 1);
        cout << "Case #" << (t + 1) << ": " << (res - res / 2) << " " << (res / 2) << endl;
    }
    return 0;
}
