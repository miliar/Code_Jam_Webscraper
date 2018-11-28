#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

void printSolution(ll D, ll N, vector<pair<ll, ll>> &horses) {
    double max_hour = 0.0;
    for (int i = 0; i < (int)horses.size(); ++i) {
        double hour = (double)(D - horses[i].first) / (double)horses[i].second;
        max_hour = max(max_hour, hour);
    }

    double speed = (double)D / max_hour;
    cout << fixed << speed << endl;
}

int main(int argc, char* argv[]) {
    int t;
    
    cout.precision(17);
    cin >> t;

    for (int i = 1; i <=t; ++i) {
        ll D, N;
        vector<pair<ll, ll>> horses;
        cin >> D >> N;
        for (int j = 0 ; j < N; ++j) {
            ll k,s;
            cin >> k >> s;
            horses.push_back(make_pair(k, s));
        }

        cout << "Case #" << i << ": ";
        printSolution(D, N, horses);        
    }
    return 0;
}