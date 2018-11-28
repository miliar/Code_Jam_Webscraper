#include<bits/stdc++.h>

using namespace std;

#define f first
#define s second
#define int long long

int32_t main(){
    ios_base::sync_with_stdio(0);
    ifstream fin("a.in");
    ofstream fout("outputA.txt");
    #define cin fin
    #define cout fout
    int t;
    cin >> t;
    for(int z = 0; z < t; ++z){
        double d, n;
        cin >> d >> n;
        double ans = 1e18;
        for(int i = 0; i < n; ++i){
            double k, s;
            cin >> k >> s;
            double tm = (d - k)/s;
            double sp = d/tm;
            ans = min(ans, sp);
        }
        cout << fixed << setprecision(7) << "Case #" << z+1 << ": " << ans << endl;
    }
}
