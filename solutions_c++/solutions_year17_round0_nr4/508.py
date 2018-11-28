#include <bits/stdc++.h>

using namespace std;

#define SZ(x) ((int)(x).size())
#define PB(x) push_back(x)
#define MEMSET(x,v) memset(x,v,sizeof(x))
#define REP(i,n) for(int (i)=0;(i)<(n);++(i))
#define x first
#define y second
#define INF (0x3f3f3f3f)

typedef long long LL;
typedef pair<int, int> P2;
template<class A, class B> inline bool mina(A &x, B y) {return (x > y)?(x=y,1):0;}
template<class A, class B> inline bool maxa(A &x, B y) {return (x < y)?(x=y,1):0;}

const int MAXN = 105;

char in2[MAXN][MAXN];
char in[MAXN][MAXN];
int N, M;

void print(char xx[][MAXN]) {
    REP(i, N) {
        REP(j, N) {
            cout << xx[i][j];
        }
        cout << endl;
    }
}

void solve_small() {
    cin >> N >> M;
    char v;
    int r, c;
    REP(i, N) REP(j, N) in2[i][j] = in[i][j] = '.';
    REP(i, M) {
        scanf(" %c %d %d", &v, &r, &c);
        r--;
        c--;
        in[r][c] = v;
        in2[r][c] = v;
    }
    int pos_o = -1;
    REP(i, N) {
        if (in[0][i] == '.') {
            in[0][i] = '+';
        } else if (in[0][i] == 'o') {
            pos_o = i;
        } else if (in[0][i] == 'x') {
            pos_o = i;
            in[0][i] = 'o';
        }
    }
    if (pos_o == -1) {
        in[0][0] = 'o';
        pos_o = 0;
    }
    for (int i = 1; i < N - 1 && N - 1 > 0; i++) {
        in[N - 1][i] = '+';
    }
    if (in[0][0] == 'o') {
        for (int i = 1; i < N; i++) {
            in[i][i] = 'x';
        }
    } else {
        int cc = 0;
        for (int i = N - 1; i > 0; i--) {
            if (cc == pos_o) cc++;
            in[i][cc] = 'x';
            cc++;
        }
    }

    int score = 0;
    vector<P2> ans;
    REP(i, N) {
        REP(j, N) {
            if (in[i][j] == 'o') score += 2;
            else if (in[i][j] != '.') score += 1;
            if (in[i][j] != in2[i][j]) {
                ans.PB(P2(i, j));
            }
        }
    }
    cout << score << " " << SZ(ans) << endl;
    for (auto p : ans) {
        cout << in[p.x][p.y] << " " << p.x + 1 << " " << p.y + 1 << endl;
    }
    //print(in);
}

int main() {
    int test;
    cin >> test;
    REP(tt, test) {
        cout << "Case #" << (tt + 1) << ": ";
        solve_small();
    }

    return 0;
}
