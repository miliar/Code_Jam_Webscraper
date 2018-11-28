#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <string>
#include <queue>
#include <sstream>
#include <cmath>
#include <random>
#include <cstring>
using namespace std;

#define CLR(a,b) memset(a,b,sizeof(a))
const int N = 19+5;
long long base[N];
long long base10[N];
long long n;

int getLen(long long n) {
    int len = 0;
    while (n) {
        n /= 10;
        len ++;
    }
    return len;
}

void pre()
{
    base[1] = 1;
    base10[1] = 1;
    for (int i = 2; i <= 19; ++i) {
        base[i] = base[i-1] * 10 + 1;
        base10[i] = base10[i-1] * 10;
    }
}

long long work(long long l) {
    long long cur = 0;
    for (int i = l; i > 0; --i) {
        int start = 9, end = 0;
        if (i == 19) start = 1;
        if (i == l) end = 1;
        bool found = false;
        for (int j = start; j >= end; --j) {
            if (cur + j * base[i] <= n) {
                cur += j * base10[i];
                found = true;
                break;
            }
        }
        if (!found) return -1;
    }
    return cur;
}

void solve()
{
    int l = getLen(n);
    long long ans = work(l);
    if (ans != -1) {
        cout << ans << endl;
    } else {
        for (int i = 0; i < l-1; ++i) {
            printf("9");
        }
        puts("");
    }
}

int main() {
    int cas = 0;
    pre();
    freopen("/Users/lizhen/Documents/Project/Cpp/cpp/cpp/input.txt", "r", stdin);
    freopen("/Users/lizhen/Documents/Project/Cpp/cpp/cpp/output.txt", "w", stdout);
    int T;
    cin >> T;
    while (T--) {
        printf("Case #%d: ", ++cas);
        cin >> n;
        solve();
    }
    return 0;
}
