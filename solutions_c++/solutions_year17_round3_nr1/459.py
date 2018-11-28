#include <bits/stdc++.h>
using namespace std;
char enl = '\n';
#define rep(i, from, to) for (int i = from; i < (to); ++i)
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<pair<int, int>> vii;
typedef long double ld;

void solve() {

    int n, k;
    cin >> n >> k;

    vector<pair<ld, int>> pancake_mantel(n);
    vector<ld> pancake_surface(n);

    rep(i,0,n) {
        ld r, h;
        cin >> r >> h;
        pancake_mantel[i] = make_pair(2.0 * M_PI * r * h, i);
        pancake_surface[i] = r * r * M_PI;
    }

    sort(pancake_mantel.rbegin(), pancake_mantel.rend());

    vector<int> pancake_index(n);

    rep(i,0,n) {
        //cout << "I" << i << endl;
        pancake_index[pancake_mantel[i].second] = i;
        //cout << pancake_mantel[i].first << " " << pancake_mantel[i].second << endl;
        //cout << "panck: " << pancake_index[pancake_mantel[i].second] << endl;
    }

    ld first_k = 0;
    ld first_km1 = 0;
    rep(i,0,k) {
        first_k += pancake_mantel[i].first;
    }
    rep(i,0,k-1) {
        first_km1 += pancake_mantel[i].first;
    }

    ld maxx = 0;

    rep(i,0,n) {
        ld ta = pancake_surface[i];
        //cout << "panck index: " << pancake_index[i] << endl;
        if (pancake_index[i] <= k-1) {
            ta += first_k;
            maxx = max(maxx, ta);
        } else {
            ta += pancake_mantel[pancake_index[i]].first;
            ta += first_km1;
            maxx = max(maxx, ta);
        }
        //cout << maxx << endl;
    }

    cout << fixed << setprecision(9);
    cout << maxx << endl;
}








    
        




int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin.exceptions(cin.failbit);

    int t;
    cin >> t;
    rep(i,0,t) {
        cout << "Case #" << (i+1) << ": ";
        solve();
    }



    return 0;
}
