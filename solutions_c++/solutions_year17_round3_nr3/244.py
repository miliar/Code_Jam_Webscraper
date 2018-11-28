#include <bits/stdc++.h>

using namespace std;


vector<double> ps;
double U;

bool solve(double m){
    double ans = 0;
    for(int i = 0; i < ps.size(); i++){
        if(ps[i] >= m) continue;
        ans += m - ps[i];
    }
    return ans <= U;
}

int main()
{
    freopen("C-small-1-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);

    ios::sync_with_stdio(false); cin.tie(0);
    int T, cnt = 0;
    cin >> T;
    while(T--){
        cnt++;
        int N, K;
        cin >> N >> K;
        cin >> U;
        ps.assign(N, 0.0);
        for(int i = 0; i < N; i++) cin >> ps[i];
        double l = 0, r = 1.0;
        while(r-l > 0.000000001){
            double mid = (l + r) / 2.0;
            if(solve(mid)){
                l = mid;
            } else {
                r = mid;
            }
        }
        double ans = 1, mid = (l+r)/2.0;
        for(int i = 0; i < N; i++){
            if(ps[i] > mid) ans *= ps[i];
            else ans *= mid;
        }
        cout << "Case #" << cnt << ": ";
        cout << fixed << setprecision(8) << ans << endl;
    }

    return 0;
}
