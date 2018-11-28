#include <bits/stdc++.h>
#define ll long long
#define ss second
#define ff first
using namespace std;

#define PI 3.14159265358979323
vector<pair<double, double> > p;
int n, k;
double dp[1005][1005];
int vis[1005][1005];
int amr = 0;

double solve(int idx, int f){
    if(f < 0)return -1e15;
    if(idx == -1){
        if(f == 0)return 0;
        else return -1e15;
    }
    double &ret = dp[idx][f];
    if(vis[idx][f] == amr)return ret;
    vis[idx][f] = amr;
    ret = max(solve(idx-1, f), 2*p[idx].ff*p[idx].ss + solve(idx-1, f-1));
    return ret;
}

int main(){
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int t;
    cin >> t;
    for(int z = 1; z <= t; ++z)
    {
            p.clear();
            ++amr;
            cin >> n >> k;
            for(int i = 0; i < n; ++i){
                double x, y;
                cin >> x >> y;
                p.push_back({x, y});
            }

            sort(p.begin(), p.end());
            double anss = 0;
            for(int i = n-1; i >= 0; --i){
                anss = max(anss, p[i].ff*p[i].ff + 2*p[i].ss*p[i].ff + solve(i-1, k-1));
            }

            printf("Case #%d: %.6f\n", z, anss * PI );
    }
}
