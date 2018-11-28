#include <iostream>
#include <map>
#include <cstdint>

using namespace std;

typedef std::uint64_t u64;

int main() {
    int T;
    cin >> T;
    for (int casen = 1; casen <= T; ++casen) {
        u64 n, k;
        cin >> n >> k;
        map<u64, u64> Q;
        Q.insert(make_pair(n, 1));
        u64 lastH, lastL;
        while (k > 0) {
            auto it = Q.end();
            --it;
            pair<u64, u64> top = *it;
            Q.erase(it);
            lastL = (top.first - 1) / 2;
            lastH = top.first - 1 - lastL;
            if (top.second >= k) break;
            k -= top.second;
            Q[lastL] += top.second;
            Q[lastH] += top.second;
        }
        cout << "Case #" << casen << ": " << lastH << ' ' << lastL << endl;
    }
}
