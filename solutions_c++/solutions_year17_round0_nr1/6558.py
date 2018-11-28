#include <iostream>
#include <math.h>
#include <algorithm>
#include <map>
using namespace std;
int main() {
    int q;
    cin >> q;
    for (int i = 1; i <= q; i++) {
        string s;
        cin >> s;
        int k;
        cin >> k;
        int flips = 0;
        for (int j = 0; j <= s.size()-k; j++) {
            if (s[j] == '-') {
                flips++;
                int aux = k, mem_j = j;
                bool toggle = false;
                while (aux--) {
                    if (s[mem_j] == '+') {
                        s[mem_j] = '-';
                        toggle = true;
                    }
                    else s[mem_j] = '+';
                    if (!toggle) j++;
                    mem_j++;
                }
                j--;
            }
        }
        for (int j = 0; j < s.size(); j++) {
            if (s[j] == '-') {
                flips = -1;
                break;
            }
        }
        if (flips != -1) cout << "Case #" << i << ": " << flips;
        else cout << "Case #" << i << ": IMPOSSIBLE";
        cout << '\n';
    }
    return 0;
}
