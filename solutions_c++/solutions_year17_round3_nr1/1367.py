#include <bits/stdc++.h>

typedef long long int ll;
typedef unsigned long long int ull;
#define rep(i,n) for(ll i=0;i<(n);i++)

using namespace std;


int main(){
    int t;
    cin >> t;

    rep(times, t){
        int n, k;
        cin >> n >> k;
        vector<ll> r(n);
        vector<ll> h(n);
        rep(i, n)   cin >> r[i] >> h[i];

        vector<ll> g;
        rep(i, n)   g.push_back(r[i]);
        sort(g.begin(), g.end());

        double ms = 0.0;
        rep(base, n){
            if(r[base] < g[k-1])    continue;
            //double sum = r[base]*r[base]*M_PI + 2*r[base]*M_PI*h[base];
            double sum = r[base]*M_PI*(r[base] + 2.0*h[base]);

            priority_queue<double> que;
            rep(i, n){
                if(i != base)   que.push(2.0*r[i]*M_PI*h[i]);
            }

            rep(i, k-1){
                double it = que.top(); que.pop();
                sum += it;
            }
            ms = max(ms, sum);
        }

        
        
        cout << fixed << setprecision(9)
            << "Case #" << times+1 << ": " << ms << endl;
    }



    return 0;
}
