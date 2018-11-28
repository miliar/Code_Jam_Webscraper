#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <climits>

using namespace std;

int main(int argc, char **argv)
{
        int T;
        cin >> T;
        for (int testcase = 0; testcase < T; testcase++) {
                int N, M;
                cin >> N >> M;
                vector<vector<char>> s(N, vector<char>(N, '.'));
                vector<vector<char>> t(N, vector<char>(N, '.'));
                for (int i = 0; i < M; i++) {
                        char m;
                        int r, c;
                        cin >> m >> r >> c;
                        s[r - 1][c - 1] = m;
                }
                int o = -1;
                for (int i = 0; i < N; i++) {
                        switch (s[0][i]) {
                        case 'o':
                        case 'x':
                                o = i;
                                t[0][i] = 'o';
                                break;
                        default:
                                t[0][i] = '+';
                                break;
                        }
                }
                if (o < 0) {
                        t[0][0] = 'o';
                        o = 0;
                }
                for (int i = 1; i < N - 1; i++) {
                        t[N - 1][i] = '+';
                }
                for (int i = 1; i < N; i++) {
                        if (o + i < N) {
                                t[i][o + i] = 'x';
                        }
                        else {
                                t[i][N - i - 1] = 'x';
                        }
                }
                int u = 0, m = 0;
                for (int r = 0; r < N; r++) {
                        for (int c = 0; c < N; c++) {
                                switch (t[r][c]) {
                                case 'o':
                                        u++;
                                case '+':
                                case 'x':
                                        u++;
                                }
                                if (s[r][c] != t[r][c]) {
                                        m++;
                                }
                        }
                }
                cout << "Case #" << testcase+1 << ": ";
                cout << u << ' ' << m << endl;
                for (int r = 0; r < N; r++) {
                        for (int c = 0; c < N; c++) {
                                if (s[r][c] != t[r][c]) {
                                        cout << t[r][c] << ' ';
                                        cout << r + 1 << ' ';
                                        cout << c + 1 << endl;
                                }
                        }
                }
        }
        return 0;
}

/*
o+++++++
.x......
..x.....
...x....
....x...
.....x..
......x.
.++++++x

x++++
.x...
..o..
...x.
.+++x

+x+++
..x..
...x.
....x
x+++.

++x++
...x.
....x
.x...
x+++.

++x+++
...x..
....x.
.....x
.x....
x+++++
*/
