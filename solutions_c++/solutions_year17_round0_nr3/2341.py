#include <iostream>
#include <map>

using namespace std;

bool split(map<long long, long long>& m, long long& k) {
    long long segment = m.rbegin()->first;
    long long amount = m.rbegin()->second;
    long long x, y;
    if (segment % 2 == 1) {
        x = y = segment / 2;
    } else {
        x = segment / 2;
        y = x - 1;
    }
    if (amount < k) {
        k -= amount;
        m.erase(segment);
        m[x] += amount;
        m[y] += amount;
        return true;
    }
    return false;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        long long n, k;
        cin >> n >> k;
        map<long long, long long> m;
        m[n] = 1;
        while (split(m, k)) {
            //cout << k << "->";
        };
        // cout << "\n";
        long long segment = m.rbegin()->first;
        long long x, y;
        if (segment % 2 == 1) {
            x = y = segment / 2;
        } else {
            x = segment / 2;
            y = x - 1;
        }
        cout << "Case #" << i + 1 << ": " << x << " " << y << "\n";
    }
    return 0;
}
