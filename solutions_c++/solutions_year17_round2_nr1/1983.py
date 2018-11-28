#include <bits/stdc++.h>
using namespace std;
using ll=long long;
using vll=vector<ll>;
using vvll=vector<vll>;
using vi=vector<int>;
using vvi=vector<vi>;
#define pb push_back

void solve(){
    int d, n;
    cin >> d >> n;
    double arrmax = 0;
    for(int i=0; i<n; ++i){
        int ki, si;
        cin >> ki >> si;
        arrmax = max(arrmax, (d-ki)/(double)si);
    }
    cout << d / arrmax;
}

int main(){
    cout.precision(17);
    int t;
    cin >> t;
    for(int tc=1; tc<=t; ++tc){
        cout << "Case #" << tc << ": ";
        solve();
        cout << "\n";
    }
}
