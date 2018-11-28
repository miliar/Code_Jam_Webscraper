#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;

    string S;
    int K;
    bool side[1002], fail;
    int count;
    for (int i=1; i<=T; ++i) {
        cin >> S >> K;

        cout << "Case #" << i << ": ";

        int L = S.size();
        for (int j=0; j<L; ++j) {
            side[j] = S[j] - '+';
        }

        count = 0;
        for (int j=0; j<=L-K; ++j) {
            if (side[j]) {
                for (int k=j; k<j+K; ++k) {
                    side[k] = !side[k];
                }

                count++;
            }
        }

        fail = false;
        for (int j=L-K; j<L; ++j) {
            if (side[j]) {
                fail = true;
                break;
            }
        }

        if (fail) {
            cout << "IMPOSSIBLE" << endl;
        }
        else {
            cout << count << endl;
        }
    }

    return 0;
}