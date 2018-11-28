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

ld eps = 0.00000000001;

void solve() {

    int n;
    int k;
    ld u;
    cin >> n >> k >> u;

    vector<ld> scores;
    rep(i,0,n) {
        ld a;
        cin >> a;
        scores.push_back(a);
    }

    sort(scores.begin(), scores.end());

    while (u > 0) {
        ld f = scores[0];
        ld s = f;
        int i = 0;
        while (abs(s - f) <= eps) {
            i++;
            if (i >= n) {
                s = 1.0;
                break;
            }
            s = scores[i];
        }
        ld dist = s - f;
        if (u - dist * i >= eps) {
                u -= dist * i;
                rep(t,0,i) {
                    scores[t] += dist;
                }
        } else {
            ld reald = u / i;
            u = 0;
            rep(t,0,i) {
                scores[t] += reald;
            }
        }
    }

    ld prod = 1;
    rep(i,0,n) {
        prod *= scores[i];
    }

    cout << fixed << setprecision(6);
    cout << prod << endl;






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
