#include <bits/stdc++.h>
using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define si(c) ((int)(c).size())
#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define all(c) (c).begin(), (c).end()
#define D(a) cerr << #a << "=" << a << endl;
#define pb push_back
#define eb emplace_back
#define mp make_pair

typedef long long int ll;
typedef vector<int> vi;
typedef pair<int,int> pii;

int n;
double d;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

    cout << fixed << setprecision(15);
    int T; cin >> T;
    forn(cas,T) {
        cout << "Case #" << cas+1 << ": ";
        cin >> d >> n;
        double t = 0;
        forn(_,n) {
            double k,s; cin >> k >> s;
            t = max(t, (d-k)/s);
        }
        double ans = d / t;
        cout << ans << endl;
    }


    return 0;
}
