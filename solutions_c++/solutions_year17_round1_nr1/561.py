#include <iostream>
using namespace std;
char cake[30][30];
bool flag[30];
int T, R, C;
int main()
{
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> R >> C;
        for (int i = 0; i < R; i++)
            cin >> cake[i];
        char cur;
        for (int i = 0; i < R; i++) {
            flag[i] = false;
            cur = '?';
            for (int j = 0; j < C; j++) {
                if (cur != '?' && cake[i][j] == '?') cake[i][j] = cur;
                else if (cake[i][j] != '?') {cur = cake[i][j]; flag[i] = true;}
            }
            if (!flag[i]) continue;
            cur = '?';
            for (int j = C-1; j >= 0; j--) {
                if (cur != '?' && cake[i][j] == '?') cake[i][j] = cur;
                else if (cake[i][j] != '?') cur = cake[i][j];
            }
        }
        int k = 0;
        for (int i = 0; i < R; i++)
            if (flag[i]) {
                k = i;
                break;
            }
        for (int i = k-1; i >= 0; i--)
            for (int j = 0; j < C; j++)
                cake[i][j] = cake[i+1][j];
        for (int i = k+1; i < R; i++)
            if (!flag[i]) {
                for (int j = 0; j < C; j++)
                    cake[i][j] = cake[i-1][j];
            }
        printf("Case #%d:\n", t);
        for (int i = 0; i < R; i++)
            cout << cake[i] << endl;
    }
    return 0;
}
