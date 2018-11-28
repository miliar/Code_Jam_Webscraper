#include <iostream>
#include <map>
using namespace std;

typedef long long int64;

pair<int64, int64> Answer(int64 v) {
    v -= 1;
    int64 x = v / 2;
    return {v - x, x};
}

pair<int64, int64> Solve(int64 n, int64 k) {
    map<int64, int64> mp;
    mp[n] = 1;
    while (1) {
        auto b = mp.rbegin();
        int64 v = b->first;
        int64 num = b->second;
        mp.erase(v);

        if (k <= num) {
            return Answer(v);
        }

        k -= num;

        v -= 1;
        int64 x = v / 2;
        mp[v - x] += num;
        mp[x] += num;
    }
}


int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t += 1) {
        int64 n, k;
        cin >> n >> k;
        auto ans = Solve(n, k);
        cout << "Case #" << t << ": " << ans.first << ' ' << ans.second << '\n';
    }
}
