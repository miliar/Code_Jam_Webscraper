#include <bits/stdc++.h>

using namespace std;

bool hits(double speed, const vector<pair<double, double> > & horses, double dist) {
    double myTime = dist/speed;
    for(const auto& horse: horses) {
        double distToGo = dist - horse.first;
        double horseTime = distToGo/horse.second;
        if(horseTime > myTime){
            return true;
        }
    }
    return false;
}

void solve() {
    int n;
    double d;
    cin >>d >>n;
    vector<pair<double , double>> horses;
    
    for(int i = 0 ;i < n ; i++) {
        double where, s;
        cin >> where >> s;
        horses.push_back(make_pair(where, s));
    }

    // cout << "done" << endl;
    
    double lo = 0.0, hi = 1e14;
    double md;

    for(int i = 0 ;i < 10000; i++) {
        md = (lo + hi)/2;
        if(hits(md, horses, d)) {
            hi = md;
        } else {
            lo = md;
        }
    }
    cout << setprecision(8) << fixed << md << endl;
}

int main() {
    int tes;
    cin >> tes;
    for(int t = 1 ; t <= tes; t++) {
        cout << "Case #" << t << ": ";
        solve();
    }
    return 0;

}
