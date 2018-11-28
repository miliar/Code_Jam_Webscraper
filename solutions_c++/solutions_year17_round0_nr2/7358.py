#include <vector>
#include <iostream>
#include <string>
using namespace std;

string n;

int main() {
    int TT;
    cin >> TT;
    for (int T = 0; T < TT; ++T) {
        cin >> n;
        int res = 0;
        while (res != -1) {
            res = -1;
            for (int i = 1; i < static_cast<int>(n.size()); ++i) {
                if (!(n[i - 1] <= n[i])) {
                    res = i - 1;
                }
            }
            if (res != -1) {
                n[res]--;
                for (int i = res + 1; i < static_cast<int>(n.size()); ++i) {
                    n[i] = '9';
                }
            }
        }
        cout << "Case #" << T + 1 << ": ";
        bool all_zeros = true;
        for (int i = 0; i < static_cast<int>(n.size()); ++i) {
            if (n[i] != '0') {
                all_zeros = false;
            }
            if (!all_zeros) {
                cout << n[i];
            }
        }
        cout << "\n";
    }
}
