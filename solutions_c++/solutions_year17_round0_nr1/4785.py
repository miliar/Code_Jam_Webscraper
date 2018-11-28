#include <iostream>
#include <vector>
#include <set>
#include <unordered_set>
#include <deque>

using namespace std;

void get_digits(long long number, deque<int> &digits) {

    while(1) {
        int res = number % 10;

        digits.push_front(res);

        number /= 10;
        if (number == 0) break;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.precision(2);
    cout << fixed;

    const char PLUS = '+';
    const char MINUS = '-';

    vector<int> flips_ctr(1005);

    int T;

    cin >> T;

    for(int i = 1;i <= T;++i) {
        int K;
        string S;

        cin >> S;
        cin >> K;

        int res = 0;
        fill(flips_ctr.begin(), flips_ctr.end(), 0);

        for(int j = 0;j < S.length();++j) {
            // apply previous flips
            if (flips_ctr[j] % 2) {
                if (S[j] == PLUS) S[j] = MINUS;
                else S[j] = PLUS;
            }

            if (j > (S.length() - K)) { // can't flip anymore
                if (S[j] != PLUS) {
                    res = -1;
                    break;
                }
                continue;
            }

            // check if need to flip
            if (S[j] != PLUS) {
                res++;

                // Store count of flips
                for(int k = j; k < min((int)S.length(), j + K);++k) {
                    flips_ctr[k]++;
                }
            }
        }

        if (res < 0) cout << "Case #" << i << ": IMPOSSIBLE" << '\n';
        else cout << "Case #" << i << ": " << res << '\n';
    }

    return 0;
}
