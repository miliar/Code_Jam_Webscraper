#include<bits/stdc++.h>
#define ll long long int
using namespace std;

const int maxN = 105;
ll edge[maxN][maxN], dist[maxN][maxN];
int E[maxN], S[maxN];

double cost[maxN][maxN];
double realcost[maxN][maxN];

double work(){
    int n, q;
    cin >> n >> q;
    for(int i = 0; i < n; i++)
        cin >> E[i] >> S[i];
    for(int i = 0; i < n; i++)
    for(int j = 0; j < n; j++)
        cin >> edge[i][j];

    for(int i = 0; i < n; i++)
    for(int j = 0; j < n; j++)
        if(i == j)
            dist[i][j] = 0;
        else
            dist[i][j] = edge[i][j] > -1? edge[i][j] : -1;

    for(int k = 0; k < n; k++){
    for(int i = 0; i < n; i++)
    for(int j = 0; j < n; j++){
        if(dist[i][k] > -1 && dist[k][j] > -1){
            if(dist[i][j] == -1)
                dist[i][j] = dist[i][k] + dist[k][j];
            else
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
        }
    }
    }

    double M = 1e15; 
    for(int i = 0; i < n; i++)
    for(int j = 0; j < n; j++)
        if(i == j)
            cost[i][j] = 0.0;
        else
            cost[i][j] = (dist[i][j] > -1 && dist[i][j] <= E[i]) ? dist[i][j]/(1.0*S[i]) : M;

    for(int i = 0; i < n; i++)
    for(int j = 0; j < n; j++)
        if(i == j)
            realcost[i][j] = 0.0;
        else
            realcost[i][j] = cost[i][j];
 
    for(int k = 0; k < n; k++){
    for(int i = 0; i < n; i++)
    for(int j = 0; j < n; j++){
            realcost[i][j] = min(realcost[i][j], realcost[i][k] + realcost[k][j]);
    }
    }
 
    for(int i = 0; i < q; i++){
        int s, t;
        cin >> s >> t;
        printf("%.7lf ", realcost[s-1][t-1]);
    }

}

int main(){
    int t;
    cin >> t;
    for(int i = 1; i <= t; i++){
        printf("Case #%d: ", i);
        work();
        printf("\n");
    }
    return 0;
}
