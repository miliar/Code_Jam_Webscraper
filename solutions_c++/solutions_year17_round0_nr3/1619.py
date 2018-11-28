#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    for(int ca = 1; ca <= t; ++ca) {
        unsigned long long n, k;
        cin >> n >> k;
        map<unsigned long long, unsigned long long, greater<unsigned long long>> m;
        m[n] = 1;
        unsigned long long cnt = 0;
        unsigned long long ans;
        while(true) {
            auto cur = m.begin();
            cnt += cur->second;
            if(cnt >= k) {
                ans = cur->first;
                break;
            }
            auto tmp = cur->first / 2;
            m[tmp] += cur->second;
            m[cur->first - tmp - 1] += cur->second;
            m.erase(cur->first);
        }
        auto maxx = ans / 2;
        cout << "Case #" << ca << ": " << maxx << " " << ans - maxx - 1 << endl;
    }
    return 0;
}

