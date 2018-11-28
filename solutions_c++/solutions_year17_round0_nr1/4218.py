#include <iostream>
#include <string> 

using namespace std;

string flip(string s, int n, int k) {
    string t = s;
    for (int i=n; i<n+k; i++) {
        if (t[i] == '+') {
            t[i] = '-';
        }
        else {
            t[i] = '+';
        }
    };
    return t;
}

int main() {
    int n;
    cin >> n;
    for (int i=0; i<n; i++) {
        int flips = 0;
        string pms;
        int k;
        cin >> pms >> k;
        int l = pms.length();
        for (int j=0; j<=l-k; j++) {
            if (pms[j] == '-') {
                pms = flip(pms, j, k);
                flips++;
            }
        }
        if (pms == string(l, '+')) {
            cout << "Case #" << i+1 << ": " << flips << "\n";
        }
        else {
            cout << "Case #" << i+1 << ": IMPOSSIBLE \n";
        }
    }
	return 0;
}
