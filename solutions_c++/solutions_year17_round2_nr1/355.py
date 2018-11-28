#include <cstdlib>
#include <cstring>

#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>

using namespace std;
typedef long long LL;

void work() {
    LL d, n;
    cin >> d >> n;
    double ans = 0;
    for (int i = 0; i < n; i ++) {
        LL k, s;
        cin >> k >> s;
        ans = max(ans, double(d - k) / s);
    }
    double sp = d / ans;
    printf(" %.9lf\n", sp);
}

int main() {
    int tot; cin >> tot;
    for (int cas = 1; cas <= tot; cas ++) {
        cout << "Case #" << cas << ":";
        work();
    }
    return 0;
}
