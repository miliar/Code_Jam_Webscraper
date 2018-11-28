#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <map>
#include <algorithm>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int times = 1; times <= T; ++times) {
        long long N, K;
        cin >> N >> K;
        map<long long, long long> S;
        S[N] = 1;
        while (K) {
            map<long long, long long>::iterator iter = S.end();
            --iter;
            if (iter->second >= K) {
                cout << "Case #" << times << ": ";
                long long a = 1, b = iter->first;
                long long c = (a + b) / 2;
                cout << max(c - a, b - c) << " " << min(c - a, b - c) << endl;
                break;
            }
            long long a = 1, b = iter->first;
            long long c = (a + b) / 2;
            S[c - a] += iter->second;
            S[b - c] += iter->second;
            K -= iter->second;
            S.erase(iter);
        }
    }

    return 0;
}