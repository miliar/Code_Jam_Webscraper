#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

vector<int> g[6];
char symb[6] = {'O', 'B', 'R', 'G', 'Y', 'V'};
int rem[6];
int st = 0;
int j = 0;
char ans[1500];
int ord[6] = {2, 0, 4, 3, 1, 5};

void getAns(int v){
    --rem[v];
    ans[j++] = symb[v];
    int mx = 0;
    for(int i = 1; i < g[v].size(); ++i){
        if(rem[g[v][i]] > rem[g[v][mx]]) mx = i;
    }
    if(rem[g[v][mx]]) getAns(g[v][mx]);
}

int main() {
#define TASK "B-small-attempt2"
    freopen(TASK".in", "r", stdin), freopen(TASK".out", "w", stdout);
    int t;
    scanf("%d", &t);
    g[0].push_back(1);
    g[1].push_back(0);
    g[1].push_back(2);
    g[1].push_back(4);
    g[2].push_back(1);
    g[2].push_back(3);
    g[2].push_back(4);
    g[3].push_back(2);
    g[4].push_back(2);
    g[4].push_back(5);
    g[4].push_back(1);
    g[5].push_back(4);
    for (int cs = 1; cs <= t; ++cs) {
        int n;
        scanf("%d", &n);
        st = ord[0];
        for(int i = 0; i < 6; ++i) scanf("%d", rem + ord[i]), st = rem[ord[i]] ? ord[i] : st;
        if(rem[0]) st = 0;
        if(rem[3]) st = 3;
        if(rem[5]) st = 5;
        printf("Case #%d: ", cs);
        j = 0;
        getAns(st);
        if(j == n && ans[0] != ans[n - 1]){
            for(int i = 0; i < n; ++i) printf("%c", ans[i]);
        } else printf("IMPOSSIBLE");
        printf("\n");
    }
    return 0;
}
