#include<iostream>
#include<vector>
#include<math.h>
#include<utility>
#include<iomanip>
#include<algorithm>
using namespace std;
typedef unsigned long long ll;
typedef pair<ll,ll> P;

struct myclass {
    bool operator() (P& p1, P& p2) {
        if (p1.first == p2.first) {
            return p1.second > p2.second;
        }
        return p1.first > p2.first;
    }
} myobject;


int main(){
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        int n, k;
        cin >> n >> k;
        ll r, h;
        vector<P> v;
        v.resize(n);
        ll global = 0;
        for (int i = 0; i < n; i++) {
            cin >> r >> h;
            v[i] = make_pair(r*h, r*r);
            global = max(global, r*r);
        }
        sort(v.begin(),v.end(), myobject);
        ll sum = 0;
        ll largest = 0;
        for (int i = 0; i < k-1; i++) {
            sum += v[i].first;
            largest = max(largest, v[i].second);
        }
        ll candidateSide = v[k-1].first;
        largest = max(largest, v[k-1].second);
        if (largest < global) {
            for (int i = k; i < n; i++) {
                if (v[i].second +2*v[i].first > largest + 2*candidateSide) {
                    largest = v[i].second;
                    candidateSide = v[i].first;
                }
            }
        }
        sum += candidateSide;
        double ans = M_PI*((double)sum*2.0+(double)largest);
        cout.precision(6);
        cout << fixed;
        cout << "Case #" << t << ": " << ans << endl;
    }
}