#include <iostream>
#include <string>

using namespace std;

struct Rec {
    char c; int x, y;
    Rec() {}
    Rec(char c, int x, int y): c(c), x(x), y(y) {}
};

Rec r[300];

int T;
int n, m;
int x, y;
int value, N;
int a[105][105];
int b[105][105];
string s;

void putX() {
    int c;
    for (c = 0; c < n; c++)
        if ((a[0][c]) && a[0][c] != 1)
            break;
    c %= n;
    x = 0; y = c;
    for (int i = 0; i < n; i++) {
        b[x][y] = min(3, b[x][y] + 2);
        x = (x + 1) % n; y = (y + 1) % n;
    }
}

void putJ() {
    int c;
    for (c = 0; c < n; c++) {
        if (b[0][c] != 1)
            b[0][c] = min(b[0][c] + 1, 3);
        if (c > 0 && c < n - 1)
            b[n - 1][c] += 1;
    }
}

char lookup(int i) {
    if (i == 1) return '+';
    else if (i == 2) return 'x';
    else return 'o';
}

void calOutput() {
    value = 0; N = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) {
            value += (b[i][j] + 1) >> 1;
            if (a[i][j] != b[i][j])
                r[N++] = Rec(lookup(b[i][j]), i + 1, j + 1);
        }
}

void show() {
    for (int i = 0; i < n; i++, cout <<endl)
        for (int j = 0; j < n; j++) {
            cout <<b[i][j] <<' ';
        }
}

int main() {
    cin >>T;
    for (int t = 1; t <= T; t++) {
        string ans;
        cin >>n >>m;
        memset(a, 0, sizeof(a));
        for (int i = 0; i < m; i++) {
            cin >>s >>x >>y;
            x--; y--;
            if (s[0] == '+') a[x][y] = 1;
            else if (s[0] == 'o') a[x][y] = 3;
            else a[x][y] = 2;
        }
        memcpy(b, a, sizeof(b));
        putX(); putJ();
        calOutput();
        printf("Case #%d: ", t);
        cout <<value <<' ' <<N <<endl;
        for(int i = 0; i < N; i++)
            printf("%c %d %d\n", r[i].c, r[i].x, r[i].y);
        //show();
    }
    return 0;
}
