#include <iostream>
#include <string>

using namespace std;

typedef long long int ll;

bool isTidy(ll n) {
    string s = to_string(n);
    int ls = (int)s.size();
    for (int i = 0; i < ls - 1; i++) {
        if (s[i] > s[i+1]) {
            return false;
        }
    }
    return true;
}

int main() {
    int T, TOT;
    cin >> T;
    TOT = T;

    while (T--) {
        ll n, i;
        cin >> n;
        for (i = n; i >= 1; i--) {
            // cout << i << "\n";
            if (isTidy(i)) {
                break;
            }
        }
        cout << "Case #" << TOT - T << ": " << i << "\n";
    }


}