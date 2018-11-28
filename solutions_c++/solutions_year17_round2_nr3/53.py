#include <cstdio>
#include <queue>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
#define ll long long
int test, n, Q, E[105], sp[105], arr[105][105];
struct info {
    int t;
    ll dis;
    info(){}
    info(int a, ll b) { t = a, dis = b; }
    bool operator<(const info &i)const {
        if (dis != i.dis)return dis > i.dis;
        return t > i.t;
    }
};
vector<pair<int, double> > v[105];
void preproc(int horse)
{
    priority_queue<info> pq;
    pq.push(info(horse, 0));
    vector<ll> dist(n + 5, 0xffffffffffffff);
    dist[horse] = 0;
    while (!pq.empty()) {
        info now = pq.top(); pq.pop();
        for (int i = 1; i <= n; i++) {
            if (arr[now.t][i] == -1)continue;
            if (dist[i] > now.dis + arr[now.t][i]) {
                dist[i] = now.dis + arr[now.t][i];
                if (dist[i] <= E[horse]) {
                    pq.push(info(i, dist[i]));
                }
            }
        }
    }
    for (int i = 1; i <= n; i++) {
        if (i == horse)continue;
        if (dist[i] <= E[horse]) {
            v[horse].push_back(make_pair(i, (double)dist[i]/(double)sp[horse]));
        }
    }
}
double query(int st, int ed)
{
    priority_queue<pair<double, int> > pq;
    pq.push(make_pair(0, st));
    vector<double> dist(n + 5, 1e18);
    dist[st] = 0;
    while (!pq.empty()) {
        pair<double, int> now = pq.top(); pq.pop();
        if (now.second == ed) {
            return -1.0*now.first;
        }
        for (int i = 0; i < v[now.second].size(); i++) {
            int next = v[now.second][i].first;
            double dis = v[now.second][i].second;
            double nowdis = -1.0*now.first;
            if (dist[next] > nowdis+dis) {
                dist[next] = nowdis + dis;
                pq.push(make_pair(-1.0*dist[next], next));
            }
        }
    }
    
    //not to be here
    return -1;
}
int main() {
    freopen("/Users/bowbowbow/Downloads/C-large.in", "r", stdin);
    freopen("/Users/bowbowbow/Downloads/C-large.out", "w", stdout);

    int lev = 0;
    scanf("%d", &test); while (test--) {
        ++lev;
        scanf("%d %d", &n, &Q);
        for (int i = 1; i <= n; i++)scanf("%d %d", &E[i], &sp[i]);
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++)
                scanf("%d", &arr[i][j]);
        
        for (int i = 1; i <= n; i++)preproc(i);
        
        vector<double> ans;
        for (int from, to, ite = 1; ite <= Q; ite++) {
            scanf("%d %d", &from, &to);
            double ret = query(from, to);
            ans.push_back(ret);
        }
        
        printf("Case #%d:", lev);
        for (int i = 0; i < Q; i++) {
            printf(" %.9lf", ans[i]);
        }
        ans.clear();
        puts("");
        
        
        for (int i = 1; i <= n; i++)v[i].clear();
    }
}
