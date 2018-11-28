
#include<algorithm>
#include<bitset>
#include<cassert>
#include<complex>
#include<cstdio>
#include<cstring>
#include<iomanip>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<string>
#include<vector>
#define FOR(i, a, b) for(int i =(a); i <=(b); ++i)
#define FORD(i, a, b) for(int i = (a); i >= (b); --i)
#define REP(i, n) for(int i = 0;i <(n); ++i)
#define VAR(v, i) __typeof(i) v=(i)
#define FORE(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
#define PB push_back
#define MP make_pair
#define X first
#define Y second 
#define debug(x) {cerr <<#x <<" = " <<x <<endl; }
#define debugv(x) {{cerr <<#x <<" = "; FORE(itt, (x)) cerr <<*itt <<", "; cerr <<endl; }}
#define dprintf(...) fprintf(stderr, __VA_ARGS__)
using namespace std;
typedef long long LL;
typedef long double LD;
typedef pair<int, int> PII;
typedef vector<int> VI;

template<class C> void mini(C&a4, C b4){a4=min(a4, b4); }
template<class C> void maxi(C&a4, C b4){a4=max(a4, b4); }
template<class T1, class T2>
ostream& operator<< (ostream &out, pair<T1, T2> pair) { return out << "(" << pair.X << ", " << pair.Y << ")";}

const int MX = 101;
int tb[4][MX][MX][MX];
int p;

int go(int i, int a, int b, int c) {
    if (a < 0 || b < 0 || c < 0) return -1;
    if (a == 0 && b == 0 && c == 0) return 0;
    if (tb[i][a][b][c] != -1) return tb[i][a][b][c];
    int res = 0;
    res = max(res, go((i+1) % p, a-1, b, c));
    res = max(res, go((i+2) % p, a, b-1, c));
    res = max(res, go((i+3) % p, a, b, c-1));
    res += (i == 0);
    return tb[i][a][b][c] = res;
}



void solve(int tc) {
    cout << "Case #" << tc << ": ";
    int n;
    cin >> n >> p;
    VI cnt(4);
    REP(i,n) {
        int g;
        cin >> g;
        cnt[g % p]++;
    }
    REP(i,p) REP(a, MX) REP(b, MX) REP(c, MX) tb[i][a][b][c] = -1;
    cout << cnt[0] + go(0, cnt[1], cnt[2], cnt[3]) << endl; 


}


int main(){
    ios_base::sync_with_stdio(false);
    cout << fixed << setprecision(10);
    int T;
    cin >> T;
    REP(i,T) solve(i+1);


    return 0;
}

