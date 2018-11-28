#include <bits/stdc++.h>
using namespace std;
#define MAXN 110
int E[MAXN], S[MAXN], mp[MAXN][MAXN];
double dis[MAXN][MAXN];
void Solve(){
    int N, Q;
    scanf("%d%d", &N, &Q);
    for(int i = 0 ; i < N ; i++)
        scanf("%d%d", &E[i], &S[i]);
    for(int i = 0 ; i < N ; i++)
        for(int j = 0 ; j < N ; j++)
            scanf("%d", &mp[i][j]);
    for(int i = 0 ; i < N ; i++)
        for(int j = 0 ; j < N ; j++)
            if(mp[i][j] == -1)
                mp[i][j] = 0x3f3f3f3f;
    for(int i = 0 ; i < N ; i++)
        for(int j = 0 ; j < N ; j++)
            dis[i][j] = 1e15;
    for(int i = 0 ; i < N ; i++){
        queue<int> q;
        vector<int> nE(N, 0);
        vector<bool> inq(N, false);
        nE[i] = E[i];
        inq[i] = true;
        dis[i][i] = 0;
        q.push(i);
        while(!q.empty()){
            auto now = q.front();
            q.pop();
            inq[now] = false;
            for(int v = 0 ; v < N ; v++){
                if(mp[now][v] <= nE[now] && dis[i][v] > dis[i][now] + (double)mp[now][v] / (double)S[i]){
                    dis[i][v] = dis[i][now] + (double)mp[now][v] / (double)S[i];
                    nE[v] = nE[now] - mp[now][v];
                    if(!inq[v])
                        q.push(v), inq[v] = true;
                }
            }
        }
    }
    for(int k = 0 ; k < N ; k++)
        for(int i = 0 ; i < N ; i++)
            for(int j = 0 ; j < N ; j++)
                if(dis[i][j] > dis[i][k] + dis[k][j])
                    dis[i][j] = dis[i][k] + dis[k][j];
    for(int i = 0 ; i < Q ; i++){
        int u, v;
        scanf("%d%d", &u, &v);
        u--, v--;
        printf(" %.7f", dis[u][v]);
    }
    puts("");
}
int main(){
    int T;
    scanf("%d", &T);
    for(int t = 1 ; t <= T ; t++){
        printf("Case #%d:", t);
        Solve();
    }
    return 0;
}
