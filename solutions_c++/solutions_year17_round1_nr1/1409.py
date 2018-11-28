#include <bits/stdc++.h>

using namespace std;

#define fi first
#define se second
#define pb push_back
#define fil(a,b) memset((a),(b),sizeof(a))
#define sz(x) ((int)(x).size())
#define rep(i,a,b) for (int i=(a); i <= int(b); i++)
#define per(i,a,b) for (int i=(a); i >= int(b); i--)
#define foreach(it,c) for (auto it=(c).begin(); it != (c).end(); it++)

template<typename T>
void _R( T &x ) { cin>>x; }
void _R( int &x ) { scanf("%d",&x); }
void _R( long long &x ) { cin>>x; }
void _R( double &x ) { scanf("%lf",&x); }
void _R( char &x ) { scanf(" %c",&x); }
void _R( char *x ) { scanf("%s",x); }

void R() {}
template<typename T, typename... U>
void R( T& head, U&... tail ) {
    _R(head);
    R(tail...);
}

template<typename T>
void _W(const T &x) { cout << x; }
void _W(const int &x) { printf("%d", x); }
template<typename T>
void _W(const vector<T> &x) {
    for (auto i = x.cbegin(); i != x.cend(); i++) {
        if (i != x.cbegin()) putchar(' ');
        _W(*i);
    }
}

void W() {}
template<typename T, typename... U> void W(const T& head, const U&... tail) {
    _W(head);
    putchar(sizeof...(tail) ? ' ' : '\n');
    W(tail...);
}

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
typedef double db;

const int inf = 0x3f3f3f3f;
// const ll inf = 0x3f3f3f3f3f3f3f3f;
const db pi = 3.14159265358979323846264338327950288L;
const db eps = 1e-6;
const int mo = 1e9+7;

char grid[30][30];

int main() {
    int tc,testcase=1,r,c;
    R(tc);
    while (tc--) {
        R(r,c);
        rep(i,0,r-1) rep(j,0,c-1) scanf(" %c", &grid[i][j]);
        rep(i,0,r-1) rep(j,0,c-1) {
            if (grid[i][j] != '?') {
                int k = i - 1;
                while (k >= 0 && grid[k][j] == '?') {
                    grid[k][j] = grid[i][j];
                    k--;
                }
                k = i + 1;
                while (k < r && grid[k][j] == '?') {
                    grid[k][j] = grid[i][j];
                    k++;
                }
            }
        }
        rep(i,0,r-1) rep(j,0,c-1) {
            if (grid[i][j] != '?') {
                int k = j - 1;
                while (k >= 0 && grid[i][k] == '?') {
                    grid[i][k] = grid[i][j];
                    k--;
                }
                k = j + 1;
                while (k < c && grid[i][k] == '?') {
                    grid[i][k] = grid[i][j];
                    k++;
                }
            }
        }
        printf("Case #%d:\n", testcase++);
        rep(i,0,r-1) {
            rep(j,0,c-1) printf("%c",grid[i][j]);
            printf("\n");
        }
    }
    return 0;
}