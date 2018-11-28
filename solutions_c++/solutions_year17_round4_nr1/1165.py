#include<bits/stdc++.h>
using namespace std;

int N, P;
vector<int> G, cnt;

vector<vector<vector<vector<int> > > > cc;
int dp(int a, int b, int c, int r) {
    int &ret = cc[a][b][c][r];
    if(ret != -1) return ret;
    ret = 0;
    if(a) ret = max(ret, dp(a - 1, b, c, (r + 1) % P));
    if(b) ret = max(ret, dp(a, b - 1, c, (r + 2) % P));
    if(c) ret = max(ret, dp(a, b, c - 1, (r + 3) % P));
    if(a != 0 || b != 0 || c != 0) ret += r == 0;
    return ret;
}

void main2(int tc) {
    scanf("%d %d", &N, &P);
    G.clear();
    G.resize(N);
    cnt.clear();
    cnt = vector<int>(4, 0);
    for(int i = 0; i < N; i++) {
        scanf("%d", &G[i]);
        cnt[ G[i] % P ]++;
    }
    int ans = cnt[0];
    cc.clear();
    cc = vector<vector<vector<vector<int> > > >(102, vector<vector<vector<int> > >(102, vector<vector<int> >(102, vector<int>(4, -1))));
    //cout << cnt[1] << ' ' << cnt[2] << ' ' << cnt[3] << endl;
    ans += dp(cnt[1], cnt[2], cnt[3], 0);
    cerr << tc << endl;
    printf("Case #%d: %d\n", tc, ans);
}

int TC;
int main() {
//*
    freopen("inA.txt", "r", stdin);
    freopen("outA.txt", "w", stdout);
//*/
    scanf("%d", &TC);
    for(int i = 1; i <= TC; i++) main2(i);
}
