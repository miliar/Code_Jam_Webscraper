#include <bits/stdc++.h>

using namespace std;

void true_main(int testcase) {
    string n;
    cin >> n;

    for (int i = n.length() - 1; i > 0; --i) {
        if (n[i] < n[i - 1]) {
            n[i - 1]--;
            for (int j = i; j < n.length(); ++j) n[j] = '9';
        }
    }

    if (n[0] == '0') n = n.substr(1, n.length());
    cout << "Case #" << testcase << ": " << n << "\n";

}

main () {
#define FILES
#ifdef FILES
    freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);
#endif
    int T;

    cin >> T;

    for (int t = 1; t <= T; ++t) {
        true_main(t);
    }
}
