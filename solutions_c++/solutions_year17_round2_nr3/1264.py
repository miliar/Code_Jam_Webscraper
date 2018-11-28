#include <bits/stdc++.h>
using namespace std;

#define INF 10000000000000
//vector<vector<int> > tali;
vector<vector<double> > dist,tali;
vector<pair<int,int > > v;
vector<bool> visited;
int n,q,t,e,s,a,b;
long long temp;
double dp[105][105][105];

double rekur(int now, int kuda, int cari){
    if (now == cari) return 0;
    double &ret = dp[now][kuda][cari];
    if (ret < INF) return ret;
    visited[now] = true;
    for (int i = 0; i < tali[now].size(); i++){
        if (!visited[i]){
            if (v[now].first >= dist[now][i]) ret = min(ret, rekur(i, now, cari) + dist[now][i]/v[now].second);
            if (v[kuda].first >= dist[kuda][i]) ret = min(ret, rekur(i,kuda, cari) + dist[kuda][i]/v[kuda].second);
        }
    }
    visited[now] = false;
    //cout<<ret<<endl;
    return ret;
}

int main(){
    scanf("%d", &t);
    for (int i = 1; i <= t; i++){
        scanf("%d %d", &n, &q);
        v.resize(n);
        dist.resize(n);
        visited.resize(n,0);
        for (int j = 0; j < n; j++){
            scanf("%d %d", &e, &s);
            v[j] = make_pair(e,s);
            dist[j].resize(n,INF);
        }
        for (int j = 0; j < n; j++){
            for (int k = 0; k < n; k++){
                scanf("%lld", &temp);
                if (temp == -1) temp = INF;
                dist[j][k] = temp;
                for (int l = 0; l < n; l++){
                    dp[j][k][l] = INF;
                }
            }
        }
        tali = dist;
        for (int j = 0; j < n; j++){
            for (int k = 0; k < n; k++){
                for (int l = 0; l < n; l++){
                    dist[k][l] = min (dist[k][j]+dist[j][l],dist[k][l]);
                }
            }
        }
        printf("Case #%d: ",i);
        for (int j = 0; j < q; j++){
            scanf("%d %d", &a, &b);
            printf("%f", rekur(a-1, a-1, b-1));
            if (j == q-1)printf("\n");
            else printf(" ");
        }
    }
}
