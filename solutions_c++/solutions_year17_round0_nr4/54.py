#include <vector>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;

bool FindMatch(int i, const VVI &w, VI &mr, VI &mc, VI &seen) {
    for (int j = 0; j < w[i].size(); j++) {
        if (w[i][j] && !seen[j]) {
            seen[j] = true;
            if (mc[j] < 0 || FindMatch(mc[j], w, mr, mc, seen)) {
                mr[i] = j;
                mc[j] = i;
                return true;
            }
        }
    }
    return false;
}

int BipartiteMatching(const VVI &w, VI &mr, VI &mc) {
    mr = VI(w.size(), -1);
    mc = VI(w[0].size(), -1);

    int ct = 0;
    for (int i = 0; i < w.size(); i++) {
        VI seen(w[0].size());
        if (FindMatch(i, w, mr, mc, seen)) ct++;
    }
    return ct;
}

int main () {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        int n, k;
        cin >> n >> k;
        vector<vector<char>> data(n, vector<char>(n, '.'));
        for (int j = 0; j < k; j++) {
            char tmp;
            int p, q;
            cin >> tmp >> p >> q;
            p--;q--;
            data[p][q] = tmp;
        }
        // do X
        vector<vector<int>> board(n, vector<int>(n, 1));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (data[i][j] == 'x' || data[i][j] == 'o') {
                    for (int ii = 0; ii < n; ii++) {
                        board[ii][j] = 0;
                        board[i][ii] = 0;
                    }
                }
            }
        }
        vector<int> mr;
        vector<int> mc;
        //printf("n = %d\n", n );
        vector<vector<char>> cross(n, vector<char>(n, '.'));
        BipartiteMatching(board, mr, mc);
        for (int i = 0; i < n; i++) {
            //printf("mr0[i] = %d\n", mr[i]);
            if (mr[i] == -1) continue;
            cross[i][mr[i]] = 'x';
        }
        vector<vector<int>> bb(2*n-1,vector<int>(2*n-1,0));
        // (i, j) -> (i+j, n-1-j+i)
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                bb[i+j][n-1-j+i] = 1;
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (data[i][j] == '+' || data[i][j] == 'o') {
                    for (int ii = 0; ii < 2 * n - 1; ii++) {
                        bb[i+j][ii] = 0;
                        bb[ii][n-1-j+i] = 0;
                    }
                }
            }
        }
        BipartiteMatching(bb, mr, mc);
        vector<vector<char>> plus(n, vector<char>(n, '.'));
        for (int i = 0; i < 2*n-1; i++) {
            //printf("mr[i] = %d\n", mr[i]);
            if (mr[i] == -1) continue;
            int jj = mr[i];
            int pi = (i + jj - n + 1) / 2;
            int pj = (i - jj + n - 1) / 2;
            plus[pi][pj] = '+';
        }
        int s = 0;
        int aa = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (data[i][j] == '+' || data[i][j] == 'x') {
                    s++;
                } else if (data[i][j] == 'o') {
                    s+=2;
                }
                bool flag = false;
                if (cross[i][j] != '.') {
                    flag = true; 
                    s++;
                }
                if (plus[i][j] != '.') {
                    flag = true; 
                    s++;
                }
                if (flag) aa++;
            }
        }
        cout << "Case #" << i << ": " << s << " " << aa << endl;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if ((cross[i][j] != '.' && plus[i][j] != '.')) {
                    cout << 'o' << " " << i+1 << " " << j+1 << endl;
                } else if (cross[i][j] != '.' && data[i][j] != '.') {
                    cout << 'o' << " " << i+1 << " " << j+1 << endl;
                } else if (plus[i][j] != '.' && data[i][j] != '.') {
                    cout << 'o' << " " << i+1 << " " << j+1 << endl;
                } else if (cross[i][j] != '.') {
                    cout << 'x' << " " << i+1 << " " << j+1 << endl;
                } else if (plus[i][j] != '.') {
                    cout << '+' << " " << i+1 << " " << j+1 << endl;
                }
            }
        }
    }
}
