#include <cstdio>
#include <queue>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
int N, R, O, Y, G, B, V;

vector<vector<vector<vector<vector<bool> > > > > cc, chk;

bool dp(int s, int p, int r, int y, int b) {
    if(chk[s][p][r][y][b]) return cc[s][p][r][y][b];
    chk[s][p][r][y][b] = true;
    
    if(r == 0 && y == 0 && b == 0) {
        return cc[s][p][r][y][b] = s != p;
    }
    
    bool ret = cc[s][p][r][y][b];
    
    ret = false;
    if(r && p != 0) ret |= dp(s, 0, r - 1, y, b);
    if(y && p != 1) ret |= dp(s, 1, r, y - 1, b);
    if(b && p != 2) ret |= dp(s, 2, r, y, b - 1);
    
    return cc[s][p][r][y][b] = ret;
}

void dfs(int s, int p, int r, int y, int b) {
    if(p == 0) {
        if(G) {
            for(int i = 0; i < G; i++) printf("RG");
            printf("R");
            G = 0;
        }
        else printf("R");
    }
    if(p == 1) {
        if(V) {
            for(int i = 0; i < V; i++) printf("YV");
            printf("Y");
            V = 0;
        }
        else printf("Y");
    }
    if(p == 2) {
        if(O) {
            for(int i = 0; i < O; i++) printf("BO");
            printf("B");
            O = 0;
        }
        else printf("B");
    }
    
    if(r == 0 && y == 0 && b == 0) return;
    
    if(r && p != 0 && dp(s, 0, r - 1, y, b)) {
        dfs(s, 0, r - 1, y, b);
        return;
    }
    if(y && p != 1 && dp(s, 1, r, y - 1, b)) {
        dfs(s, 1, r, y - 1, b);
        return;
    }
    if(b && p != 2 && dp(s, 2, r, y, b - 1)) {
        dfs(s, 2, r, y, b - 1);
        return;
    }
}

void main2(int tc) {
    scanf("%d %d %d %d %d %d %d", &N, &R, &O, &Y, &G, &B, &V);
    
    if(B + O == N && B == O) {
        printf("Case #%d: ", tc);
        for(int i = 0; i < N / 2; i++) {
            printf("BO");
        }
        printf("\n");
        return;
    }
    if(R + G == N && R == G) {
        printf("Case #%d: ", tc);
        for(int i = 0; i < N / 2; i++) {
            printf("RG");
        }
        printf("\n");
        return;
    }
    if(Y + V == N && Y == V) {
        printf("Case #%d: ", tc);
        for(int i = 0; i < N / 2; i++) {
            printf("YV");
        }
        printf("\n");
        return;
    }
    
    if((O && B < O + 1) || (G && R < G + 1) || (V && Y < V + 1)) {
        printf("Case #%d: IMPOSSIBLE\n", tc);
        return;
    }
    
    B -= O;
    R -= G;
    Y -= V;
    
    cc = chk = vector<vector<vector<vector<vector<bool> > > > >(3, vector<vector<vector<vector<bool> > > >(3, vector<vector<vector<bool> > >(R + 1, vector<vector<bool> >(Y + 1, vector<bool>(B + 1, false)))));
    
    bool ans;
    
    if(R) ans = dp(0, 0, R - 1, Y, B);
    else if(Y) ans = dp(1, 1, R, Y - 1, B);
    else ans = dp(2, 2, R, Y, B - 1);
    
    if(!ans) {
        printf("Case #%d: IMPOSSIBLE\n", tc);
        return;
    }
    
    printf("Case #%d: ", tc);
    
    if(R) dfs(0, 0, R - 1, Y, B);
    else if(Y) dfs(1, 1, R, Y - 1, B);
    else dfs(2, 2, R, Y, B - 1);
    
    printf("\n");
}

int TC;
int main() {
    freopen("/Users/bowbowbow/Downloads/B-large.in", "r", stdin);
    freopen("/Users/bowbowbow/Downloads/B-large.out", "w", stdout);
    
    scanf("%d", &TC);
    for(int i = 1; i <= TC; i++) main2(i);
}
