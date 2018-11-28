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

int n;
int a[22];
int b[22];
bool found;
long long res;

void get(int pos, int last_digit, bool smaller) {
    if (found) return;
    if (pos == -1) {
        found = true;
        res = 0;
        Ford(i, n - 1, 0) res = res * 10 + b[i];
        return;
    }
    Ford(digit, 9, 0) {
        if (digit >= last_digit && (smaller || a[pos] >= digit)) {
            b[pos] = digit;
            get(pos - 1, digit, smaller || a[pos] > digit);
        }
    }
}

int main() {
    int nt;
    cin >> nt;
    Rep(t, nt) {
        long long k;
        cin >> k;
        n = 0;
        while(k > 0) {
            a[n++] = k % 10;
            k = k / 10;
        }
        found = false;
        get(n - 1, 0, false);
        cout << "Case #" << (t + 1) << ": " << res << endl;
    }
    return 0;
}
