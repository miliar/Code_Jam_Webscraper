#include <iostream>

using namespace std;

char **cake;
int R, C;

int fr1(int r, int c) {
    int r1;
    for(r1 = r - 1; r1 >= 0; --r1)
        if(cake[r1][c] != '?')
            return r1 + 1;

    return 0;
}

int fc1(int r, int c) {
    int c1;
    for(c1 = c - 1; c1 >= 0; --c1)
        if(cake[r][c1] != '?')
            return c1 + 1;

    return 0;
}

int fc2(int r, int c) {
    int c2;
    for(c2 = c + 1; c2 < C; ++c2)
        if(cake[r][c2] != '?')
            return c2 - 1;

    return C - 1;
}

int fr2(int r, int c1, int c2) {
    int r2;
    for(r2 = r + 1; r2 < R; ++r2) {
        for(int l = c1; l <= c2; ++l)
            if(cake[r2][l] != '?')
                return r2 - 1;
    }

    return R - 1;
}

void cut(int r1, int r2, int c1, int c2, char n) {
    for(int r = r1; r <= r2; ++r)
        for(int c = c1; c <= c2; ++c)
            cake[r][c] = n;
}

int main() {
    int T;
    cin >> T;
    for(int i = 1; i <= T; ++i) {
        bool take[26];

        for(int j = 0; j < 26; ++j)
            take[j] = false;

        cin >> R >> C;
        cake = new char*[R];
        for(int r = 0; r < R; ++r) {
            cake[r] = new char[C];
            for (int c = 0; c < C; ++c)
                cin >> cake[r][c];
        }

        for(int r = 0; r < R; ++r) {
            for (int c = 0; c < C; ++c) {
                if (cake[r][c] != '?' && !take[cake[r][c] - 'A']) {
                    int r1 = fr1(r,c);
                    int c1 = fc1(r, c);
                    int c2 = fc2(r, c);
                    int r2 = fr2(r, c1, c2);
                    cut(r1, r2, c1, c2, cake[r][c]);
                    take[cake[r][c] - 'A'] = true;
                }
            }
        }

        cout << "Case #" << i << ":" << endl;
        for(int r = 0; r < R; ++r) {
            for (int c = 0; c < C; ++c)
                cout << cake[r][c];
            cout << endl;
            delete [] cake[r];
        }
        delete []cake;
    }
}