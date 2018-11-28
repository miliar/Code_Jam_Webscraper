#include <stdio.h>
#include <stdlib.h>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <deque>
#include <queue>
#include <set>
#include <string.h>
#define pb push_back
#define sz(V) ((int)(V).size())
#define allv(V) ((V).begin()),((V).end())
#define befv(V) ((V)[(sz(V)-2)])
#define upmin(ans,ansx) (ans)=min((ans),(ansx))
#define upmax(ans,ansx) (ans)=max((ans),(ansx))
#define MAXN (55)
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<pii, int> piii;
typedef priority_queue<int, vector<int>, greater<int>> PQTYPE;
const int dx[] = {0, 1, 0, -1}, dy[] = {-1, 0, 1, 0};
const int sldir[2][4] = {{1, 0, 3, 2}, {3, 2, 1, 0}}; // 0 : / 
inline int yxtoidx(const int& y, const int& x) { return y*MAXN + x; }
inline int lgchton(const char& x) { return '/' == x ? 0 : 1; }
inline int rztoidx(const int& y, const int& x, const int& dir) { return (y*MAXN + x)*2 + dir; }
inline void fg(vector<int> G[], const int& A, const int& B) { G[A].pb(B); }

vector<int> STG[MAXN*MAXN*4];
vector<int> STV;
bool STchk[MAXN*MAXN*4];
int STd[MAXN*MAXN*4], STdn;
vector<int> GDIDX;
bool fckAns[MAXN*MAXN*4];

vector<pii> Edge;
vector<int> CG[MAXN*MAXN];
vector<int> LV[MAXN][MAXN][2];
vector<int> Cells;
char str[MAXN][MAXN];
bool isDes[MAXN][MAXN][2]; // 0 : -, 1 : |
bool gottafck[MAXN*MAXN];
int T, H, W;

bool isDestroy(vector<int>& V, const int& _y, const int& _x, const int& _dir) {
    int y = _y, x = _x, dir = _dir;
    while(true) {
        y += dy[dir]; x += dx[dir];
        if(y < 1 || x < 1 || H < y || W < x) return false;
        if('#' == str[y][x]) return false;
        if('.' == str[y][x]) { V.pb(yxtoidx(y, x)); continue; }
        if('-' == str[y][x] || '|' == str[y][x]) return true;
        if('/' == str[y][x] || '\\' == str[y][x]) {
            dir = sldir[lgchton(str[y][x])][dir];
        }
    }
    return false;
}
void STdfs(vector<int>& V, const int& idx) {
    STchk[idx] = true; for(const int& v : STG[idx])
        if(!STchk[v]) STdfs(V, v);
    V.pb(idx);
}
void STdfs1(int d[], const int& idx) {
    STchk[idx] = true; d[idx] = STdn; for(const int& v : STG[idx])
        if(!STchk[v]) STdfs1(d, v);
}
int main() {
    scanf("%d", &T); for(int t_i = 1; t_i <= T; t_i++) {
        vector<pii>().swap(Edge);
        for(int i = 0; i < MAXN*MAXN; i++) vector<int>().swap(CG[i]);
        for(int i = 0; i < MAXN; i++) for(int j = 0; j < MAXN; j++) for(int k = 0; k < 2; k++)
            vector<int>().swap(LV[i][j][k]);
        vector<int>().swap(Cells);
        for(int i = 0; i < MAXN; i++) for(int j = 0; j < MAXN; j++) for(int k = 0; k < 2; k++)
            isDes[i][j][k] = false;
        for(int i = 0; i < MAXN*MAXN; i++) gottafck[i] = false;
        for(int i = 0; i < MAXN*MAXN*4; i++) vector<int>().swap(STG[i]);
        vector<int>().swap(STV);
        fill(STchk, STchk + MAXN*MAXN*4, false);
        fill(STd, STd + MAXN*MAXN*4, 0);
        vector<int>().swap(GDIDX);
        fill(fckAns, fckAns + MAXN*MAXN*4, false);


        scanf("%d%d", &H, &W);
        for(int i = 1; i <= H; i++) scanf(" %s", str[i]+1);
        for(int i = 1; i <= H; i++) for(int j = 1; j <= W; j++) {
            if('-' != str[i][j] && '|' != str[i][j]) continue;
            bool flag;
            flag = isDestroy(LV[i][j][0], i, j, 1);
            flag = flag || isDestroy(LV[i][j][0], i, j, 3);
            isDes[i][j][0] = flag;

            flag = isDestroy(LV[i][j][1], i, j, 0);
            flag = flag || isDestroy(LV[i][j][1], i, j, 2);
            isDes[i][j][1] = flag;
        }
        bool isjotmang = false;
        for(int i = 1; !isjotmang && i <= H; i++) for(int j = 1; j <= W; j++) {
            if('-' != str[i][j] && '|' != str[i][j]) continue;
            if(isDes[i][j][0] && isDes[i][j][1]) {
                isjotmang = true; break;
            }
        }
        if(isjotmang) {
            printf("Case #%d: IMPOSSIBLE\n", t_i);
            continue;
        }

        for(int i = 1; i <= H; i++) for(int j = 1; j <= W; j++) {
            if('-' != str[i][j] && '|' != str[i][j]) continue;
            if(isDes[i][j][0]) {
                for(const int& v : LV[i][j][1]) gottafck[v] = true;
            } else if(isDes[i][j][1]) {
                for(const int& v : LV[i][j][0]) gottafck[v] = true;
            }
        }
        for(int i = 1; i <= H; i++) for(int j = 1; j <= W; j++) {
            if('-' != str[i][j] && '|' != str[i][j]) continue;
            if(!isDes[i][j][0] && !isDes[i][j][1]) {
                GDIDX.pb(rztoidx(i, j, 0)); GDIDX.pb(rztoidx(i, j, 1));

                sort(allv(LV[i][j][0])); sort(allv(LV[i][j][1]));
                LV[i][j][0].erase(unique(allv(LV[i][j][0])), LV[i][j][0].end());
                LV[i][j][1].erase(unique(allv(LV[i][j][1])), LV[i][j][1].end());

                for(const int& v : LV[i][j][0]) {
                    if(gottafck[v]) continue;
                    CG[v].pb(rztoidx(i, j, 0));
                }
                for(const int& v : LV[i][j][1]) {
                    if(gottafck[v]) continue;
                    CG[v].pb(rztoidx(i, j, 1));
                }
            }
        }
        for(int i = 1; i <= H; i++) for(int j = 1; j <= W; j++) {
            if('.' != str[i][j]) continue;
            if(gottafck[yxtoidx(i, j)]) continue;
            Cells.pb(yxtoidx(i, j));
        }
        auto fckINVERSE = [&](const int& a) -> int {
            if(a&1) return a-1;
            return a+1;
        };
        auto fckTWOSAT = [&](const int& a, const int& b) {
            Edge.pb({fckINVERSE(a), b});
            Edge.pb({fckINVERSE(b), a});
        };
        for(const int& v : Cells) {
            if(CG[v].empty()) { isjotmang = true; break; }
            if(2 < sz(CG[v])) puts("WTF?");
            if(1 == sz(CG[v])) {
                fckTWOSAT(CG[v][0], CG[v][0]);
            } else {
                fckTWOSAT(CG[v][0], CG[v][1]);
            }
        }
        if(isjotmang) {
            printf("Case #%d: IMPOSSIBLE\n", t_i);
            continue;
        }
        
        for(const pii& e : Edge) fg(STG, e.first, e.second);
        for(int i : GDIDX) if(!STchk[i]) STdfs(STV, i);
        for(int i : GDIDX) vector<int>().swap(STG[i]);
        for(const pii& e : Edge) fg(STG, e.second, e.first);
        reverse(allv(STV)); fill(STchk, STchk + 4*MAXN*MAXN, false);
        for(const int& v : STV) if(!STchk[v]) { STdfs1(STd, v); STdn++; }
        for(int i : GDIDX) if(STd[i] == STd[fckINVERSE(i)]) {
            isjotmang = true; break;
        }
        if(isjotmang) {
            printf("Case #%d: IMPOSSIBLE\n", t_i);
            continue;
        }

        for(int i : GDIDX) {
            if(i&1) continue;
            fckAns[i] = STd[i] > STd[fckINVERSE(i)];
        }

        printf("Case #%d: POSSIBLE\n", t_i);
        for(int i = 1; i <= H; puts(""), i++) for(int j = 1; j <= W; j++) {
            if('-' == str[i][j] || '|' == str[i][j]) {
                if(isDes[i][j][0]) putchar('|');
                else if(isDes[i][j][1]) putchar('-');
                else {
                    if(fckAns[rztoidx(i, j, 0)]) putchar('-');
                    else putchar('|');
                }
            } else putchar(str[i][j]);
        }
    }
    return 0;
}
