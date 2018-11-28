#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

int T;
long long N, K;
map<long long, long long> M;
map<long long, long long>::reverse_iterator it;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> T;
    for (int TT = 1; TT <= T; ++TT) {
        cin >> N >> K;
        M[N] = 1;
        for (it = M.rbegin(); it != M.rend(); ++it) {
            if (it->first == 1) continue;
            M[it->first / 2] += it->second;
            M[(it->first - 1) / 2] += it->second;
        }
        long long ANS = -1;
        long long sum = 0;
        for (it = M.rbegin(); it != M.rend(); ++it) {
            sum += it->second;
            if (sum >= K) {
                ANS = it->first;
                break;
            }
        }
        cout << "Case #" << TT << ": ";
        cout << ANS / 2 << " " << (ANS - 1) / 2 << "\n";
        M.clear();
    }
    return 0;
}
