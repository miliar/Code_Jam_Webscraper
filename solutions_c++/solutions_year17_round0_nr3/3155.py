#include <iostream>
#include <algorithm>
#include <map>
using namespace std;
typedef long long LL;
int main()
{
    int T;
    cin >> T;
    for (int Ti = 1; Ti <= T; ++Ti) {
        LL n, k;
        cin >> n >> k;
        map<LL, LL> f;
        f[n] = 1;
        while (1) {
            pair<LL, LL> ed = *f.rbegin();
            LL l, r;
            if (ed.first % 2 == 0)
                l = ed.first / 2, r = ed.first / 2 - 1;
            else
                l = r = (ed.first - 1) / 2;
            if (ed.second >= k) {
                cout << "Case #" << Ti << ": " << max(l, r) << " " << min(l, r) << endl;
                break;
            }
            k -= ed.second;
            f.erase(--f.end());
            LL t1 = max(l, r);
            LL t2 = min(l, r);
            f[t1] += ed.second;
            f[t2] += ed.second;
        }
    }
    return 0;
}
