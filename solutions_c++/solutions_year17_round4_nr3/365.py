
#include<bits/stdc++.h>
#define rep(i,a,b) for(int i=a;i<b;i++)
using namespace std; void _main(); int main() { cin.tie(0); ios::sync_with_stdio(false); _main(); }
//---------------------------------------------------------------------------------------------------
/*---------------------------------------------------------------------------------------------------
　　　　　　　　　　　 ∧＿∧  
　　　　　 ∧＿∧ 　（´<_｀ ）　 Welcome to My Coding Space!
　　　　 （ ´_ゝ`）　/　 ⌒i     
　　　　／　　　＼　 　  |　|     
　　　 /　　 /￣￣￣￣/　　|  
　 ＿_(__ﾆつ/　    ＿/ .| .|＿＿＿＿  
　 　　　＼/＿＿＿＿/　（u　⊃  
---------------------------------------------------------------------------------------------------*/



#define rrep(i,a,b) for(int i = a;i>=b;i--)
int H, W;
string B[60];
vector<int> v;
//---------------------------------------------------------------------------------------------------
int C[60][60], ans[10101];
int chk() {
    rep(y, 0, H) rep(x, 0, W) if (B[y][x] == '.') if (C[y][x] == 0) return false;
    return true;
}
//---------------------------------------------------------------------------------------------------
bool dfs(int cu) {
    if (cu == v.size()) {
        return chk();
    }

    int x = v[cu] % W;
    int y = v[cu] / W;

    // 囲まれている
    if (B[y - 1][x] == '#' && B[y + 1][x] == '#' && B[y][x - 1] == '#' && B[y][x + 1] == '#') return dfs(cu + 1);

    // '-'
    bool ok = true;
    rep(xx, x + 1, W) {
        if (B[y][xx] == '#') break;
        if (B[y][xx] == 'X') {
            ok = false;
            break;
        }
    }
    rrep(xx, x - 1, 0) {
        if (B[y][xx] == '#') break;
        if (B[y][xx] == 'X') {
            ok = false;
            break;
        }
    }
    if (ok) {
        rep(xx, x + 1, W) {
            if (B[y][xx] == '#') break;
            C[y][xx]++;
        }
        rrep(xx, x - 1, 0) {
            if (B[y][xx] == '#') break;
            C[y][xx]++;
        }

        ans[cu] = 0;
        bool a = dfs(cu + 1);
        if (a) return true;

        rep(xx, x + 1, W) {
            if (B[y][xx] == '#') break;
            C[y][xx]--;
        }
        rrep(xx, x - 1, 0) {
            if (B[y][xx] == '#') break;
            C[y][xx]--;
        }
    }

    // '|'
    ok = true;
    rep(yy, y + 1, H) {
        if (B[yy][x] == '#') break;
        if (B[yy][x] == 'X') {
            ok = false;
            break;
        }
    }
    rrep(yy, y - 1, 0) {
        if (B[yy][x] == '#') break;
        if (B[yy][x] == 'X') {
            ok = false;
            break;
        }
    }
    if (ok) {
        rep(yy, y + 1, H) {
            if (B[yy][x] == '#') break;
            C[yy][x]++;
        }
        rrep(yy, y - 1, 0) {
            if (B[yy][x] == '#') break;
            C[yy][x]++;
        }

        ans[cu] = 1;
        bool a = dfs(cu + 1);
        if (a) return true;

        rep(yy, y + 1, H) {
            if (B[yy][x] == '#') break;
            C[yy][x]--;
        }
        rrep(yy, y - 1, 0) {
            if (B[yy][x] == '#') break;
            C[yy][x]--;
        }
    }

    return false;
}
//---------------------------------------------------------------------------------------------------
void sol() {
    cin >> H >> W;
    rep(y, 1, H + 1) cin >> B[y];

    rep(y, 1, H + 1) B[y] = "#" + B[y] + "#";
    W += 2; H += 2;
    B[0] = ""; B[H - 1] = "";
    rep(x, 0, W) B[0] += "#", B[H - 1] += "#";

    v.clear();
    rep(y, 0, H) rep(x, 0, W) if (B[y][x] == '|' || B[y][x] == '-') B[y][x] = 'X';
    rep(y, 0, H) rep(x, 0, W) if (B[y][x] == 'X') v.push_back(y * W + x);

    rep(y, 0, H) rep(x, 0, W) C[y][x] = 0;
    
    if (!dfs(0)) {
        printf("IMPOSSIBLE\n");
        return;
    }

    printf("POSSIBLE\n");
    rep(i, 0, v.size()) {
        int x = v[i] % W;
        int y = v[i] / W;
        if (ans[i] == 0) B[y][x] = '-';
        else B[y][x] = '|';
    }
    rep(y, 1, H - 1) {
        string s = B[y].substr(1, W - 2);
        printf("%s\n", s.c_str());
    }
}
//---------------------------------------------------------------------------------------------------
void _main() {
    int T; cin >> T;
    rep(t, 1, T + 1) {
        printf("Case #%d: ", t);
        fprintf(stderr, "Finish : %d\n", t);
        sol();
    }
}