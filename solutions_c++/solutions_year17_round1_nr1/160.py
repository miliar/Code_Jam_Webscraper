#include <bits/stdc++.h>

#define MAXN 27
#define cin fin
#define cout fout

using namespace std;

ifstream fin("A-large.in");
ofstream fout("A-large.out");

int T;
int R, C;
char grid[MAXN][MAXN];

bool emptyrow(int idx) {
    for (int i=0; i<C; i++)
        if (grid[idx][i] != '?')
            return false;
    return true;
}

int main()
{
    cin >> T;
    for (int caseno=1; caseno<=T; caseno++) {
        cin >> R >> C;
        for (int i=0; i<R; i++)
            for (int j=0; j<C; j++)
                cin >> grid[i][j];

        for (int i=0; i<R; i++) if (!emptyrow(i)) {
            char nextletter;
            for (int j=C-1; j>=0; j--)
                if (grid[i][j] != '?') nextletter = grid[i][j];
            for (int j=0; j<C; j++) {
                if (grid[i][j] == '?')
                    grid[i][j] = nextletter;
                else if (grid[i][j] != nextletter)
                    nextletter = grid[i][j];
            }

            int upd = i;
            while (upd > 0 && emptyrow(upd-1)) {
                for (int j=0; j<C; j++)
                    grid[upd-1][j] = grid[upd][j];
                upd --;
            }
            upd = i;
            while (upd < R-1 && emptyrow(upd+1)) {
                for (int j=0; j<C; j++)
                    grid[upd+1][j] = grid[upd][j];
                upd ++;
            }
        }

        cout << "Case #" << caseno << ":\n";
        for (int i=0; i<R ;i++) {
            for (int j=0; j<C; j++)
                cout << grid[i][j];
            cout << endl;
        }
    }


    return 0;
}
