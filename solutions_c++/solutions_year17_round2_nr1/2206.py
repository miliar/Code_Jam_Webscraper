//Round 1B 2017
#include <bits/stdc++.h>
using namespace std;
#define F first
#define S second
#define mp make_pair
#define pb push_back
#define CLEAR(a) memset(a,0,sizeof a)
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define fr freopen("input.txt", "r", stdin);
#define fw freopen("output.txt", "w", stdout);
#define int long long 
typedef long long LL;
typedef pair<int,int> pii;
const int MOD = 1e9 + 7;
const int MAX = 1e5 + 5;
vector< pair<double, double> > v;
int n, d;

int check(double s){
    FOR(i, 1, n-1){
        double t = v[i].F/s, t1 = 0;
        for(int j=0;j<i;j++) t1 = max(t1, (v[i].F - v[j].F)/v[j].S);
        if(t < t1) return 0; 
    }
    double t = d/s, t1 = 0;
    REP(i, n){
        t1 = max(t1, (d-v[i].F)/v[i].S);
    }
    if(t < t1) return 0;
    return 1;
}

 main() {
    fr;fw;
    cout << fixed << setprecision(10);
    int cases = 1, T;
    cin >> T;
    while(T--){
        v.clear();
        cin >> d >> n;
        REP(i, n){
            int k, s;
            cin >> k >> s;
            v.pb(mp(k, s));
        }
        sort(v.begin(), v.end());
        
        double lo = 0, hi = 1e18;
        REP(i, 300){
            double mid = (lo+hi)/2;
            if(check(mid)) lo = mid;
            else hi = mid;
        }
       cout << "Case #"<<cases++ <<": "<< lo <<"\n";
    }
    return 0;
}