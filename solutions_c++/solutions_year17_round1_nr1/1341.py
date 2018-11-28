#include <iostream>
#include <string>

using namespace std;

int T;
int n, m;
char a[30][30];

bool valid(int x, int y) {
    return (x >= 0 && x <= n && y >= 0 && y <= m);
}

void fillv(int p, int q, char c, int d) {
    if (!valid(p, q)) return;
    if (a[p][q] != '?') return;
    a[p][q] = c;
    fillv(p, q + d , c, d);
}

void fillh(int p, int q, char c, int d) {
    if (!valid(p, q)) return;
    if (a[p][q] != '?') return;
    a[p][q] = c;
    fillh(p + d, q, c, d);
}

int main() {
    cin >>T;
    for (int t = 1; t <= T; t++) {
        cin >>n >>m;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                cin >>a[i][j];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                if (a[i][j] != '?') {
                    fillv(i, j + 1 , a[i][j], 1);
                    fillv(i, j - 1, a[i][j], -1);
                }
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                if (a[i][j] != '?') {
                    fillh(i + 1, j, a[i][j], 1);
                    fillh(i - 1, j, a[i][j], -1);
                }
        cout <<"Case #" <<t <<":" <<endl;
        for (int i = 0; i < n; i++, cout <<endl)
            for (int j = 0; j < m; j++)
                cout <<a[i][j];
    }
    return 0;
}
