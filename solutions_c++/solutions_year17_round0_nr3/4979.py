#include <iostream>
#include <cmath>
#include <queue>

using namespace std;

typedef long double ld;
typedef unsigned long long int ulli;

int main() {
    unsigned int T;
    cin >> T;
    for (unsigned int t = 1; t <= T; ++t) {
        ld N;
        ulli K;
        cin >> N >> K;
        cout << "Case #" << t << ": ";
        if (N == K)
            cout << "0 0" << endl;
        else {
            priority_queue<ulli> open_spaces;
            open_spaces.push((ulli)N);
            while (--K) {
                ulli current = open_spaces.top();
                open_spaces.pop();
                ld ans = current/2.0;
                ulli first_side = (ulli)ceil(ans) - 1;
                ulli second_side = current - first_side - 1;
                open_spaces.push(first_side);
                open_spaces.push(second_side);

                //cout << "K: " << K << " Current: " << current << endl;
                //cout << "1: " << first_side << " 2: " << second_side << endl;
                //cout << "---" << endl;
            }
            ulli current = open_spaces.top();
            ld ans = current/2.0;
            ulli min = (ulli)ceil(ans) - 1;
            ulli max = current - min - 1;
            cout << max << " " << min << endl;
        }
    }
}
