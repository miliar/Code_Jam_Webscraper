#include"bits/stdc++.h"
using namespace std;
priority_queue<double, vector<double>, greater<double> > q;
const double eps = 1e-8;
int main()
{
    freopen("C-small-1-attempt0.in", "r", stdin);
    freopen("Cans.out", "w", stdout);
    int T;
    cin >> T;
    int cas = 0;
    while(T --){
        cas ++;
        int n, k;
        double t, tem;
        cin >> n >> k;
        cin >> t;
        for(int i = 1; i <= n; i ++){
            cin >> tem;
            q.push(tem);
        }
        while(t > eps){
            double now = q.top(); q.pop();
            now += 0.0001;
            t -= 0.0001;
            q.push(now);
        }
        double ans = 1.0;
        while(!q.empty()){
            double now = q.top(); q.pop();
            ans *= now;
        }
        printf("Case #%d: %.7f\n", cas, ans);
    }
    return 0;
}
