#include <iomanip>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <queue>
#include <fstream>
#include <sstream>
#include <set>
#include <cmath>
#include <map>
#include <iomanip>

using namespace std;

typedef long long int64 ;
typedef unsigned long long uint64 ;
typedef pair<int, int> pint ;
typedef pair<int64, int64> pint64 ;
typedef vector<int> vint ;

#define px first
#define py second

#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define ABS(x) ((x) > 0 ? (x) : -(x))

#define REP(i, n) for (int i = 0 ; i < (n) ; i ++)
#define REPD(i, n) for (int i = (n) ; i >= 0 ; i --)
#define FOR(i, a, b) for (int i = (a) ; i < (b) ; i ++)
#define FORD(i, a, b) for (int i = (a) ; i >= (b) ; i --)

#define MUL64(x, y) (((int64) (x)) * ((int64) (y)))
#define MULMOD(x, y, modul) (MUL64(x, y) % modul)
#define MUL(x, y) MULMOD(x, y, modul)
#define ADD(reg, val) { reg += val ; if (reg >= modul) reg -= modul ; }

#define SET(v, val) memset(v, val, sizeof(v)) ;
#define SIZE(v) ((int) (v).size())
#define ALL(v) (v).begin(), (v).end()
#define SORT(v) { sort(ALL(v)) ; }
#define RSORT(v) { SORT(v) ; REVERSE(v) ; }
#define REVERSE(v) { reverse(ALL(v)) ; }
#define UNIQUE(v) unique((v).begin(), (v).end())
#define RUNIQUE(v) { SORT(v) ; (v).resize(UNIQUE(v) - (v).begin()) ; }

#define MAXN 888

int findNextInCol(int nr, int nc, int sr, int col, string table[MAXN]) {
    FOR(r, sr, nr) if (table[r][col] != '?') return r;
    return nr;
}

void fillCol(int curCol, int nr, int nc, string table[MAXN]) {
    int nextRow = findNextInCol(nr, nc, 0, curCol, table), curRow = 0;
    if (nextRow < nr) {
        char lastLetter = table[nextRow][curCol];
        while (nextRow < nr) {
            FOR(r, curRow, nextRow) table[r][curCol] = lastLetter;
            curRow = nextRow+1;
            nextRow = findNextInCol(nr, nc, curRow, curCol, table);
            if (nextRow >= nr) {
                FOR(r, curRow, nr) table[r][curCol] = lastLetter;
                break;
            }
            lastLetter = table[nextRow][curCol];
        }
    } else {
        REP(r, nr) table[r][curCol] = table[r][curCol - 1];
    }
}

int main() {
  int numTests ;
  cin >> numTests ;
  int nr, nc;
  FOR(test, 1, numTests + 1) {
    cin >> nr >> nc;
    string table[MAXN];
    REP(r, nr) cin >> table[r];

    int startCol = 0, curCol, curRow, nextRow;
    while (findNextInCol(nr, nc, 0, startCol, table) >= nr) startCol++;

    fillCol(startCol, nr, nc, table);

    FOR(c, startCol + 1, nc) {
        fillCol(c, nr, nc, table);
    }
    FORD(c, startCol - 1, 0) {
        REP(r, nr) table[r][c] = table[r][c+1];
    }
    cout << "Case #" << test << ":" << endl;
    REP(r, nr) cout << table[r] << endl;
  }

  return 0;
}
