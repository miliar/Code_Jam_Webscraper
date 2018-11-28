#include <iostream>

using namespace std;

void printResult(int nr, int result) {
    cout << "Case #" << nr << ": " << result << "\n";
}

void printResult(int nr, string result) {
    cout << "Case #" << nr << ": " << result << "\n";
}

int main() {
    ios_base::sync_with_stdio(0);

    int t;
    cin >> t;

    string n;
    char last;

    for (int i = 1; i <= t; i++) {
        cin >> n;
        last = n[0];

        if (n.size() == 1) {
            printResult(i, n);
            continue;
        }

        for (int j = 1; j < n.size(); j++) {
            if (last <= n[j]) {
                last = n[j];
            }
            else {
                n[j-1] = (char) (last - 1);

                for (int h = j; h < n.size(); h++) {
                    n[h] = '9';
                }

                for (int h = j - 2; h >= 0; h--) {
                    if (n[h] == last) {
                        n[h] = (char) (last - 1);
                        n[h+1] = '9';
                    }
                }

                break;
            }
        }

        if (n[0] == '0') {
            printResult(i, n.substr(1));
        }
        else {
            printResult(i, n);
        }

    }

    return 0;
}