#include <iostream>
#include <algorithm>
#include <map>
#include <iterator>

using namespace std;

int main() {
    int testcase;
    cin >> testcase;
    for(int tc=1; tc<=testcase; ++tc) {
        long long N, K;
        long long ans_l, ans_r;
        map<long long, long long> ctr;
        cin >> N >> K;
        ctr[N] = 1LL;
        while(K > 0LL) {
            auto it = prev(ctr.end());
            long long cur = (it->first) - 1LL;
            long long cnt = (it->second);
            long long l = cur/2LL;
            long long r = l + (cur%2LL);
            if (cnt < K ) {
                ctr.erase(it);
                ctr[l] += cnt;
                ctr[r] += cnt;
                K-=cnt;
            } else {
                ans_l = l;
                ans_r = r;
                K -= cnt;
            }
        }
        cout << "Case #" << tc << ": " << max(ans_l, ans_r) << ' ' << min(ans_l, ans_r) << endl;
    }
    return 0;
}
