#include <iostream>
#include <string>
#include <climits>
#include <vector>

using std::endl;
using std::cin;
using std::cout;
using std::string;
using std::vector;

void doCase(int caseNum) {
    string S;
    unsigned int K;
    cin >> S >> K;
    int len = S.length();
    vector<bool> f(len);

    for (int i = 0; i < len; i++) {
        f[i] = S[i] == '+';
    }

    int flips = 0;
    for (int i = 0; i < len - K + 1; i++) {
        if (!f[i]) {
            //cout << "Flipping at pos " << i << endl;
            flips++;
            for (int j = 0; j < K; j++) {
                f[i + j] = !f[i + j];
            }
        }
    }

    bool ok = true;
    for (int i = len - K; i < len; i++) {
        if (!f[i]) {
            ok = false;
            break;
        }
    }

    if (!ok) {
        cout << "Case #" << caseNum << ": IMPOSSIBLE" << endl;
    } else {
        cout << "Case #" << caseNum << ": " << flips << endl;
        /*
        for (int i = 0; i < len; i++) {
            cout << (f[i] ? '+' : '-');
        }
        cout << " " << endl;
        */
    }
}

int main() {
    int numCases;
    cin >> numCases;

    for (int i = 0; i < numCases; i++) {
        doCase(i+1);
    }
}
