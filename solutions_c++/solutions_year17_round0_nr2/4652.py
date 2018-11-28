#include <iostream>

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int c = 1; c <= t; ++c) {
        string nbr;
        cin >> nbr;
        int i = 0;
        bool bad = false;
        for (; i < nbr.length() - 1; ++i) {
            if (nbr[i] > nbr[i + 1]) {
                bad = true;
                break;
            }
        }
        if (bad) {
            while (i > 0 && nbr[i] == nbr[i - 1]) {
                --i;
            }
            --nbr[i];
            ++i;
            for (; i < nbr.length(); ++i) {
                nbr[i] = '9';
            }
        }
        while (nbr[0] == '0') {
            nbr.erase(0, 1);
        }
        cout << "Case #" + to_string(c) + ": " + nbr << endl;
    }
    return 0;
}