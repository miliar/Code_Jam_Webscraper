#include <bits/stdc++.h>
#include <math.h>
#define INF 100000000000005
#define MAXN 100005
#define mod 1000000007
#pragma comment(lib, "user32")

using namespace std;

#define F first
#define S second
#define MP make_pair
#define all(x) (x).begin(), (x).end()

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

ll k[1005], s[1005];

int main() {
    freopen("A-large (2).in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t; cin >> t;
    for(int z = 0; z < t; ++z) {
        int n; ll d;
        double f = 0.0;
        cin >> d >> n;
        for(int i = 0; i < n; ++i) {
            cin >> k[i] >> s[i];
            double temp_f = (d - k[i]) / (double) s[i];
            if(temp_f >= f) {
                f = temp_f;
            }
        }
        cout << fixed << setprecision(6) << "Case #" << z + 1 << ": " << d / f << endl;
    }
}
