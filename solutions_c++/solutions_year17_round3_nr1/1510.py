#include<bits/stdc++.h>

using namespace std;

const long double PI = 3.141592653589793238462643383;

long double mem[1001][1001][2];
bool vis[1001][1001][2];
vector<pair<int, int>> dim;
int n, k;

long double solve(int ind, int taken, int any){
    if(ind == n || taken == k)
        return 0;

    if(vis[ind][taken][any]++)
        return mem[ind][taken][any];

    long double res1 = 0, res2 = 0;


    res1 = solve(ind + 1, taken, any);


    if(!any){
        res2 = (long long)dim[ind].first * dim[ind].first * PI;
    }
    res2 += 2LL * dim[ind].first * dim[ind].second * PI;
    res2 += solve(ind+1, taken+1, 1);
    return mem[ind][taken][any] = max(res1, res2);
}

int main() {
    freopen ("input.txt","r",stdin);
    freopen ("output.txt","w",stdout);
    int t;
    cin >> t;
    for(int f=1; f<=t; f++){
        memset(vis, 0, sizeof vis);
        dim.clear();
        cin >> n >> k;

        for(int i=0; i<n; i++){
            int x, y;
            cin >> x >> y;
            dim.push_back({x, y});
        }
        sort(dim.rbegin(), dim.rend());
        cout << "Case #" << f << ": ";
        cout << fixed << setprecision(10) << solve(0, 0, 0) << endl;

    }
    return 0;
}
