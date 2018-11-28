#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <climits>

using namespace std;

int64_t solve(int64_t N, int64_t K) {
        map<int64_t, int64_t> m;
        m[N] = 1;
        while (true) {
                auto a = --m.end();
                K -= a->second;
                if (K <= 0)
                        return a->first;
                m[(a->first - 1) / 2] += a->second;
                m[a->first / 2] += a->second;
                m.erase(a);
        }
}

int main(int argc, char **argv)
{
        int T;
        cin >> T;
        for (int testcase = 0; testcase < T; testcase++) {
                int64_t N, K;
                cin >> N >> K;
                auto x = solve(N, K);
                cout << "Case #" << testcase+1 << ": ";
                cout << x / 2 << ' ' << (x - 1) / 2;
                cout << endl;
        }
        return 0;
}
