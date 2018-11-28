#include<cstdio>
#include<iostream>
#include<queue>
#include<vector>
using namespace std;
typedef long long ll;
typedef pair<ll,ll> pl;
ll T,N,Q,U,V,S[101],E[101];
bool chk[101];
double R[101],D[101][101];
int main() {
    //freopen("C-large.in", "r", stdin);
    //freopen("output_C3.out", "w", stdout);
    scanf("%lld", &T);
    for(ll t=1;t<=T;t++) {
        scanf("%lld%lld", &N, &Q);
        for(int i=1;i<=N;i++)
            scanf("%lld%lld",E+i,S+i);
        for(int i=1;i<=N;i++)
            for(int j=1;j<=N;j++)
                scanf("%lf",&D[i][j]), D[i][j] = D[i][j] == -1 ? 1e17 : D[i][j];
        for(int i=1;i<=N;i++) D[i][i] = 0;
        for(int k=1;k<=N;k++)
            for(int i=1;i<=N;i++)
                for(int j=1;j<=N;j++)
                    if(D[i][k] + D[k][j] < D[i][j]) D[i][j] = D[i][k] + D[k][j];
        for(int i=1;i<=N;i++)
            for(int j=1;j<=N;j++) {
                if(D[i][j] > E[i]) D[i][j] = 1e17;
                else D[i][j] = (double)D[i][j] / S[i];
            }
        printf("Case #%lld: ", t);
        for(int _q=1;_q<=Q;_q++) {
            scanf("%lld%lld",&U,&V);
            
            for(int i=1;i<=N;i++) R[i] = 1e17;
            priority_queue<pair<int,int>> q;
            q.push({0,U}), R[U] = 0, chk[U] = 1;
            while(!q.empty()) {
                ll u = q.top().second; q.pop();
                for(ll i=1;i<=N;i++) {
                    if(i == u || D[u][i] == (ll)1e17) continue;
                    if(R[u] + D[u][i] < R[i]) {
                        R[i] = R[u] + D[u][i];
                        q.push({-R[i], i});
                    }
                }
            }
            printf("%f ", R[V]);
        }
        puts("");
    }
    return 0;
}
