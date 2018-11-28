#include <bits/stdc++.h>

using namespace std;

int main() {
//    freopen("A-large.in", "r", stdin);
//    freopen("A-large.out", "w", stdout);
    int t, n;
    char str[1005];
    scanf("%d", &t);
    for (int tc = 1; tc <= t; tc++) {
        scanf("%s %d", str, &n);
        int sz = (int) strlen(str);
        int cnt = 0;
        for(int i=0; i<=sz-n; i++) {
            if (str[i] == '-') {
                for(int j=i; j<i+n; j++) {
                    if (str[j] == '-') {
                        str[j] = '+';
                    } else if(str[j] == '+') {
                        str[j] = '-';
                    }
                }
                cnt++;
            }
        }
        bool happy = true;
        for(int i=sz-n+1; i<sz; i++) {
            if (str[i] == '-') {
                happy = false;
                break;
            }
        }
        if (happy) {
            cout << "Case #" << tc << ": " << cnt << endl;
        } else {
            cout << "Case #" << tc << ": " << "IMPOSSIBLE" << endl;
        }
    }
    return 0;
}
