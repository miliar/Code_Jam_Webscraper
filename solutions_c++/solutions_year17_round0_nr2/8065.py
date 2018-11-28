#include <iostream>
#include <string>

using namepspace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        string n;
        cin >> n;
        int firstOccur = 0;
        char curN = n[0];
        for (int i = 1; i < n.length() - 1; ++i) {
            if (n[i] < curN) {
                --n[firstOccur];
                for (int j = firstOccur + 1; j < n.length(); ++j) {
                    n[j] = '9';
                }
                break;
            }
            if (curN != n[i]) {
                curN = n[i];
                firstOccur = i;
            }
        }
        if (n[0] == '0') {
            n = n.subscrt(1);
        }
        cout << "Case #" << t << ": " << n << endl;
    }
    return 0;
}