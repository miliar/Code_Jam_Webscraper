#include <iostream>

#define swap(x) (x == '+' ? '-' : '+')

using namespace std;

int main() {
    
    int t, j, ci, i, cnt;
    char s[2000];
    int k;
    bool allhappy;
    
    cin >> t;
    
    for (int ci = 1; ci <= t; ++ci) {
        
        //cin >> s >> k;
        scanf("%s %d", s, &k);

        allhappy = true;
        int l = 0;
        while (s[l] != 0) {
            if (s[l] == '-') {
                allhappy = false;
            }
            l++;
        }
        
        if (allhappy) {
            cout << "Case #" << ci << ": " << 0 << endl;
            continue;
        }
/*
        bool impossible = false;
        for(i = 1; i < k - 1; i++) {
            if (s[i] != s[i+1])
                impossible = true;
        }
        
        for(i = l - 2; i > l - k; i--) {
            if (s[i] != s[i-1])
                impossible = true;
        }
*/
        if (l < k) {
            cout << "Case #" << ci << ": " << "IMPOSSIBLE" << endl;
            continue;
        }

        cnt = 0;
        for(i = 0; i <= l - k; i++) {
//            cout << i << ": ";
            if (s[i] == '-') {
                cnt++;
                for(j = i; j < i + k; j++) {
                    s[j] = swap(s[j]);
                }
            }
//            cout << s << endl;
        }
        
        allhappy = true;
        for(i = l - k + 1; i < l; i++) {
            if (s[i] == '-') {
                allhappy = false;
                cout << "Case #" << ci << ": " << "IMPOSSIBLE" << endl;
                break;
            }
        }
        
        if (allhappy)
            cout << "Case #" << ci << ": " << cnt << endl;
    }
}