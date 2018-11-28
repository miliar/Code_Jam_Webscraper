#include <bits/stdc++.h>
#define fr(a, b, c) for(int a = b; a < c; ++a)
#define pb push_back

using namespace std;

int r, c;
char mat[30][30];
int mark[30][30];

inline bool ing(int i, int j) {
    return i >= 0 && i < r && j >= 0 && j < c && mat[i][j] == '?';
}

inline bool ing2(int i, int j, char a) {
    return i >= 0 && i < r && j >= 0 && j < c && mat[i][j] == a;
}

inline bool go_down(int i, int j) {
    if (!ing(i+1, j) && !ing(i-1, j)) return false;
    else {
        if (ing(i+1, j)) {
            int k = i+1;
            while (ing(k, j)) {
                mat[k][j] = mat[i][j];
                k++;
            }
        }
        if (ing(i-1, j)) {
            int k = i-1;
            while (ing(k, j)) {
                mat[k][j] = mat[i][j];
                --k;
            }
        }
        return true;
    }
}

inline void go_right1(int i, int j) {
    int k = j+1;
    while (ing(i, k)) {
        mat[i][k] = mat[i][j];
        k++;
    }
    k = j-1;
    while (ing(i, k)) {
        mat[i][k] = mat[i][j];
        --k;
    }
}

inline bool cango(int i, int j, int k) {
    fr(a, i, j) if (mat[a][k] != '?') return false;
    return true;
}

inline void go_right2(int i, int j) {
    int st = i, en = i;

    int k = i+1;
    while (ing2(k, j, mat[i][j])) ++k;
    en = k;

    k = i-1;
    while (ing2(k, j, mat[i][j])) --k;
    st = k+1;

    k = j+1;
    while (cango(st, en, k)) {
        fr(a, st, en) mat[a][k] = mat[i][j];
        ++k;
    }
}

void dbg() {
    fr(i, 0, r) {
        fr(j, 0, c) cout << mat[i][j];
        cout << endl;
    }
}

int main() {
    int t, cas = 0;
    cin >> t;
    while (t--) {
        memset(mat, '\0', sizeof mat);
        memset(mark, 0, sizeof mark);
        scanf("%d %d", &r, &c);
        fr(i, 0, r) {
            fr(j, 0, c) {
                scanf(" %c", &mat[i][j]);
                if (mat[i][j] != '?') mark[i][j] = 1;
            }
        }

        fr(i, 0, r) fr(j, 0, c) {
            if (mark[i][j]) {
                if (go_down(i, j)) {
                    //cout << i << ' ' << j << ' ';
                    //dbg();
                    go_right2(i, j);
                } else go_right1(i, j);
            }
        }
        printf("Case #%d:\n", ++cas);
        fr(i, 0, r) {
            fr(j, 0, c) printf("%c", mat[i][j]);
            cout << endl;
        }
    }
    return 0;
}