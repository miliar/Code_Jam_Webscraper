#include <bits/stdc++.h>

using namespace std;

#define N 25
int t, r, c; char data[N][N];

void run(int i, int j) {
    
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> t;
    for (int it = 1; it <= t; it++) {
        cin >> r >> c;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++)
                cin >> data[i][j];
        }
        for (int i = 0; i < r; i++) {
            int k = 0;
            while (k < c && data[i][k] == '?') k++;
            if (k == c) continue;
            for (int j = 0; j < k; j++)
                data[i][j] = data[i][k];
            int pre = data[i][k];
            for (int j = k + 1; j < c; j++)
                if (data[i][j] == '?')
                    data[i][j] = pre;
                else pre = data[i][j];
        }
        int pre = -1;
        for (int i = 0; i < r; i++) {
            int k = 0;
            while (k < c && data[i][k] == '?') k++;
            if (k == c && pre == -1) {
                int ii = i + 1;
                for (; ii < r; ii++)
                    if (data[ii][0] != '?') break;
                for (int j = 0; j < c; j++)
                    data[i][j] = data[ii][j];
                pre = i;
            } else if (k == c && pre != -1) {
                for (int j = 0; j < c; j++)
                    data[i][j] = data[pre][j];
            } else {
                pre = i;
            }
        }
        cout << "Case #" << it << ":" << endl;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++)
                cout << data[i][j];
            cout << endl;
        }
    }
    return 0;
}
