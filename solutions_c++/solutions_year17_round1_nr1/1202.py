#include <bits/stdc++.h>

using namespace std;

char old[30][30];
char m[30][30];
int dx[] = {0, 1, 0, -1};
int dy[] = {1, 0, -1, 0};

int ini, inj;

void f(int i, int j) {

    int di = i, dj = j;

    while(m[di - 1][dj] == '?') di --;

    dj = 0;
    for(int l = di; l <= i; l ++) {
        int mj = j;

        while(m[l][mj - 1] == '?') mj --;
        dj = max(dj, mj);
    }

//////////////////////////////////////top left
    for(int l = di; l <= i; l ++)
    for(int p = dj; p <= j; p ++)
        m[l][p] = m[i][j];

    int first = dj;

    dj = 555;
    for(int l = di; l <= i; l ++) {
        int mj = j;

        while(m[l][mj + 1] == '?') mj ++;
        dj = min(dj, mj);
    }

//////////////////////////////////////top right
    for(int l = di; l <= i; l ++)
    for(int p = j; p <= dj; p ++)
        m[l][p] = m[i][j];

    int last = dj;

    for(di = i + 1; ; di ++) {
        bool ok = true;
        for(int p = first; p <= last; p ++)
            if(m[di][p] != '?') ok = false;
        if(ok == false) break;
    }
    di --;

    for(int l = i + 1; l <= di; l ++)
    for(int p = first; p <= last; p ++)
        m[l][p] = m[i][j];
}

int main()
{
    freopen("file.in", "r", stdin);
    freopen("file.out", "w", stdout);

    int t;
    cin >> t;

    for(int o = 1; o <= t; o ++) {
        int r, c;
        cin >> r >> c;

        for(int i = 0; i <= r + 1; i ++) m[i][0] = '.', m[i][c + 1] = '.';
        for(int j = 1; j <= c + 1; j ++) m[0][j] = '.', m[r + 1][j] = '.';

        int nr = 0;
        for(int i = 1; i <= r; i ++) {
            for(int j = 1; j <= c; j ++) {
                cin >> old[i][j];
                m[i][j] = old[i][j];
                if(m[i][j] == '?')
                    nr ++;
            }
        }

        if(nr > 0) {
            for(int i = 1; i <= r; i ++) {
                for(int j = 1; j <= c; j ++)
                    if(old[i][j] != '?') {
                        f(i, j);
                    }
            }
        }

        cout << "Case #" << o << ":\n";
        for(int i = 1; i <= r; i ++) {
            for(int j = 1; j <= c; j ++)
                cout << m[i][j];
            cout << "\n";
        }
    }

    return 0;
}
