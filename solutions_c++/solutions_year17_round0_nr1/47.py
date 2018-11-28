#include <iostream>

using namespace std;

int main(void) {

    int test_num;
    cin >> test_num;

    for (int Case = 1 ; Case <= test_num ; ++Case) {

        string s;
        int k;

        cin >> s >> k;

        int ans = 0;
        for (int i = k-1 ; i < s.length() ; ++i) {
            if (s[i-k+1] == '-') {
                ++ans;
                for (int j = i-k+1 ; j <= i ; ++j) {
                    s[j] = (s[j] == '+' ? '-' : '+');
                }
            }
        }

        bool err = false;
        for (char ch : s) {
            err |= ch == '-';
        }

        cout << "Case #" << Case << ": ";
        if (err) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout << ans << endl;
        }

        cerr << Case << endl;
    }

    return 0;
}
