#include <iostream>
#include <vector>
#include <string>

#define REP(i,a,b) for(int i=int(a);i<int(b);i++)

using namespace std;

typedef long long int lli;

const int inf = 1 << 30;

bool check(lli n) {
    while (n) {
        int t = n % 10;
        n /= 10;
        if (n % 10 > t) return false;
    }
    return true;
}

lli calc(string num, int lastn, lli n, bool flags) {
    if (num.size() == 0) return n;
    if (flags) num[0] = '9';
    if (num[0] - '0' < lastn) return -1;
    for (int i = num[0] - '0'; i >= 0; i--) {
        if (i < lastn) break;
        lli res = calc(num.substr(1), i, 10 * n + i, flags);
        if (res != -1) return res;
        flags = true;
    }
    return -1;
}

int main () {
    int T;
    cin >> T;
    REP (_, 0, T) {
        string N;
        cin >> N;
        lli ans = calc(N, 0, 0, false);
        cout << "Case #" << _ + 1 << ": " << ans << endl;
    }
    return 0;
}
