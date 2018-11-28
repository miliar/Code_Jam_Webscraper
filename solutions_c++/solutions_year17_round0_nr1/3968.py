#include <bits/stdc++.h>
using namespace std;

int t, k, res;
string pancakes;

int main (int argc, char** argv) {
    cin >> t;
    for (int cur = 1; cur <= t; cur++) {
        res = 0;
        cin >> pancakes >> k;
        for (int i = 0; i < pancakes.size(); i++) {
            if (pancakes[i] == '-') {
                if (i+k > pancakes.size()) {
                    res = -1;
                    break;
                } else {
                    res++;
                    for (int j = i; j < i+k; j++) {
                        pancakes[j] = (pancakes[j] == '-') ? '+' : '-';
                    }
                }
            }
        }
        if (res == -1) {
            cout << "Case #" << cur << ": IMPOSSIBLE" << endl; 
        } else {
            cout << "Case #" << cur << ": " << res << endl; 
        }
    }
    return 0;
}