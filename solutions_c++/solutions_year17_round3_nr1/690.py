#include<bits/stdc++.h>

#define x first
#define y second
#define y0 hi1
#define y1 hi2
#define ll long long
#define mp make_pair
#define pb push_back
#define sqr(a) (a)*(a)
#define ld long double
#define all(a) (a).begin(), (a).end()

using namespace std;

const int inf = 2000000000;

ld PI = acos(0) * 2;

int main(){
    cin.tie(0);
    ios_base::sync_with_stdio(0);

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T;
    cin >> T;
    for(int _num = 1; _num <= T; _num++){
        cout << "Case #" << _num << ": ";
        int n, m;
        ld ans = 0;

        cin >> n >> m;
        pair<ld, ld> a[n];
        for(int i = 0; i < n; i++){
            cin >> a[i].x >> a[i].y;
        }

        for(int i = 0; i < n; i++){
            ld r0 = a[i].x;

            vector<ld> b;
            for(int j = 0; j < n; j++){
                if(i != j && a[j].x <= r0){
                    b.pb(a[j].x * a[j].y);
                }
            }
            sort(all(b));
            reverse(all(b));

            ld res = r0 * (r0 + 2 * a[i].y);
            for(int i = 0; i < min(int(b.size()), m - 1); i++){
                res += b[i] * 2;
            }
            res *= PI;
            ans = max(ans, res);
        }

        cout.precision(7);
        cout << fixed << ans << "\n";
    }
}

