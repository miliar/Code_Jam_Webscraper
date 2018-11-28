#include <bits/stdc++.h>

using namespace std;

int t, n, w = 1;

double d, q[1000], m;

pair<double, double> ks[1000];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    while(w <= t){
        cout << "Case #" << w << ": ";
        ++w;
        cin >> d >> n;
        m = 0;
        for(int i = 0; i < n; ++i){
            cin >> ks[i].first >> ks[i].second;
        }
        stable_sort(ks, ks + n);
        q[n - 1] = (d - ks[n - 1].first) / ks[n - 1].second;
        m = max(m, q[n - 1]);
        //cout << m << "\n";
        for(int i = n - 2; i >= 0; --i){
            if((d - ks[i].first) / ks[i].second < q[i + 1]){
                q[i] = q[i + 1];
            } else q[i] = (d - ks[i].first) / ks[i].second;
            m = max(m, q[i]);
        }
        printf("%.8lf\n", d / m);
    }
    return 0;
}