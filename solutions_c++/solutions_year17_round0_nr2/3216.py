#include <iostream>
#include <string>

using namespace std;

int main() {
    int T;
    string N;

    cin >> T;
    for (int n = 1; n <= T; n++) {
        cin >> N;
        for (int i = N.length() - 1; i > 0; i--) {
            if (N[i - 1] > N[i]) {
                --N[i - 1];
                for (int j = i; j < N.length(); j++) {
                    N[j] = '9';
                }
            }
        }
        cout << "Case #" << n << ": ";
        for (int i = 0; i < N.length(); i++) {
            if (N[i] != '0') {
                for (int j = i; j < N.length(); j++) {
                    cout << N[j];
                }
                break;
            }
        }
        cout << endl;
    }
    return 0;
}
