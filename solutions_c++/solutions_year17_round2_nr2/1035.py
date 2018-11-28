#include <bits/stdc++.h>

using namespace std;

int main() {
    int t;
    scanf("%d", &t);

    for(int c = 1 ; c <= t ; c++) {
        int n, r, o, y, g, b, v;
        scanf("%d %d %d %d %d %d %d", &n, &r, &o, &y, &g, &b, &v);

        // BRY
        string res = "";
        bool imp = false;

        if(b) {
            res = "B";
            b--;
        } else if(r) {
            res = "R";
            r--;
        } else {
            res = "Y";
            y--;
        }

        for(int i = 1 ; i < n ; i++) {
            char last = res[i - 1];
            if(last == 'B') {
                if(y == 0 && r == 0) {
                    imp = true;
                    break;
                }

                if(y > r)
                    res += "Y", y--;
                else
                    res += "R", r--;
            } else if(last == 'Y') {
                if(b == 0 && r == 0) {
                    imp = true;
                    break;
                }


                if(b > r)
                    res += "B", b--;
                else
                    res += "R", r--;
            } else {
                if(y == 0 && b == 0) {
                    imp = true;
                    break;
                }


                if(y > b)
                    res += "Y", y--;
                else
                    res += "B", b--;
            }
        }

        cout << "Case #" << c << ": ";
        if(imp || res[0] == res[n - 1]) {
            cout << "IMPOSSIBLE";
        } else
            cout << res;
        cout << endl;
    }

    return 0;
}
