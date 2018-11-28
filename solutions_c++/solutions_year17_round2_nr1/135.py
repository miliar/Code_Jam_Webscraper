#include <bits/stdc++.h>
using namespace std;
#define int long long
#define all(x) (x).begin(), (x).end()
#define pb push_back

typedef pair<int, int> ii;
typedef long double LD;

const int N = 1005;
int K[N], S[N];

void solve(int tn){ cout << "Case #" << tn << ": ";
    int D, n;
    cin >> D >> n;


    vector<ii> v;
    for(int i = 0; i < n; i++){
        cin >> K[i] >> S[i];
        v.pb({K[i], S[i]});
    }

    sort(all(v));
    reverse(all(v));

    LD t = 0;
    for(auto p : v){
        t = max(t, 1.L*(D-p.first)/p.second);
    }

    cout << 1.L*D/t << endl;
}

int32_t main(){
    cout << fixed << setprecision(11);
        int T;
    cin >> T;
    for(int i = 1; i <= T; i++)
        solve(i);
}
