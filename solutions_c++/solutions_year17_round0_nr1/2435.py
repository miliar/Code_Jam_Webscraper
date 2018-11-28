#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main() {
    int T;
    int n, l, tot;
    bool pan[1000];
    bool flag;

    cin >> T;
    for (int Ti = 0; Ti < T; ++Ti) {
        n = 0;
        char x;
        cin >> x;
        pan[n++] = (x == '+');
        scanf("%c", &x);
        while (x == '-' || x == '+') {
            pan[n++] = (x == '+');
            scanf("%c", &x);
        }
        cin >> l;

        tot = 0;
        if (n < l) {
            flag = true;
            for (int i = 0; i < n; i++)
                if (!pan[i]) {
                    flag = false;
                    break;
                }
            if (!flag) tot = -1;
        }
        else {
            for (int i = 0; i <= n-l; i++) {
                if (!pan[i]) {
                    for (int j = i; j < i+l && j < n; j++)
                        pan[j] ^= 1;
                    tot++;
                }
            }
            flag = true;
            for (int i = n-1; i > n-l-1; i--)
                if (!pan[i]) {
                    flag = false;
                    break;
                }
            if (!flag) tot = -1;
        }
        cout << "Case #" << Ti+1 << ": ";
        if (tot >= 0)
            cout << tot << endl;
        else
            cout << "IMPOSSIBLE" << endl;
    }


    return 0;
}
