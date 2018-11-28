#include <algorithm>
#include <cassert>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <vector>
using namespace std;

#define FR(i,a,b) for(int i=(a);i<(b);++i)
#define FOR(i,n) FR(i,0,n)
#define CLR(x,a) memset(x,a,sizeof(x))
#define setmin(a,b) a = min(a,b)
#define PB push_back
#define FORALL(i,v) for(typeof((v).end())i=(v).begin();i!=(v).end();++i)
#define MP make_pair
#define A first
#define B second
#define RF(i,a,b) for(int i=(a)-1;i>=(b);--i)
#define BEND(v) (v).begin(),(v).end()
#define SZ(v) int((v).size())
#define FORI(i,v) FOR(i,SZ(v))
typedef long double ld;
typedef long long ll;

const int MAXN = 128;
int N;
int grid[MAXN][MAXN];
int out[MAXN][MAXN];

const int FLAG_RC = 1;
const int FLAG_DG = 2;

int row_sum[MAXN];
int col_sum[MAXN];
int dgp_sum[2*MAXN]; // r+c diagonal
int dgd_sum[2*MAXN]; // r-c diagonal

bool put_rc(int r, int c)
{
    int & row_val = row_sum[r];
    int & col_val = col_sum[c];

    if (row_val > 0) return false;
    if (col_val > 0) return false;

    out[r][c] |= FLAG_RC;
    ++row_val;
    ++col_val;

    return true;
}

bool put_dg(int r, int c)
{
    //printf("    Trying to put '+' at %d %d...\n", r, c);
    int & dgp_val = dgp_sum[r+c];
    int & dgd_val = dgd_sum[r-c + MAXN];

    if (dgp_val > 0) return false;
    if (dgd_val > 0) return false;

    //printf("      success!\n");

    out[r][c] |= FLAG_DG;
    ++dgp_val;
    ++dgd_val;

    return true;
}

void fill_dgp(int dgp_idx)
{
    //printf("  Filling diagonal r+c = %d\n", dgp_idx);
    FOR(r,dgp_idx+1) {
        int c = dgp_idx - r;
        if (0 <= r && r < N && 0 <= c && c < N) put_dg(r,c);
    }
}

void doit(int cas)
{
    CLR(out, 0);
    CLR(row_sum, 0);
    CLR(col_sum, 0);
    CLR(dgp_sum, 0);
    CLR(dgd_sum, 0);

    int M;
    scanf(" %d %d", &N, &M);
    FOR(i, M) {
        char ch;
        int r;
        int c;
        scanf(" %c %d %d", &ch, &r, &c);
        assert(1 <= r && r <= N);
        assert(1 <= c && c <= N);
        --r; --c;

        if (ch == 'x' || ch == 'o') assert(put_rc(r, c));
        if (ch == '+' || ch == 'o') assert(put_dg(r, c));
    }

    FOR(r,N) FOR(c,N) grid[r][c] = out[r][c];

    FOR(r,N) FOR(c,N) put_rc(r, c);

    for (int dgp_lo = 0, dgp_hi = 2*N-2; dgp_lo <= dgp_hi; ++dgp_lo, --dgp_hi) {
        fill_dgp(dgp_hi);
        fill_dgp(dgp_lo);
    }

    int ans = 0;
    vector< pair<int,int> > diffs;
    FOR(r,N) FOR(c,N) {
        if (out[r][c] & FLAG_RC) ++ans;
        if (out[r][c] & FLAG_DG) ++ans;
        if (grid[r][c] != out[r][c]) diffs.push_back(MP(r,c));
    }

/*
    printf("Case #%d: %d\n", cas, ans);
/*/
    printf("Case #%d: %d %d\n", cas, ans, SZ(diffs));
    for (auto it : diffs) {
        int r = it.first;
        int c = it.second;

        char ch = '.';
        if (out[r][c] & FLAG_RC) {
            if (out[r][c] & FLAG_DG) {
                ch = 'o';
            } else {
                ch = 'x';
            }
        } else {
            if (out[r][c] & FLAG_DG) {
                ch = '+';
            } else {
                assert(false);
            }
        }

        printf("%c %d %d\n", ch, r+1, c+1);
    }
    // */
}

int T;
int main()
{
    scanf(" %d", &T);
    assert(1 <= T && T <= 100);
    FOR(cas,T) doit(cas+1);
    return 0;
}
