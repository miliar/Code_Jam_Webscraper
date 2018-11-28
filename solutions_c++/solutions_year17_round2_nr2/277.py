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

string COL = "RYB";

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

    int T; cin >> T;
    forn(cas,T) {
        cout << "Case #" << cas+1 << ": ";

        int n; cin >> n;
        int col[3], _;
        forn(i,3) cin >> col[i] >> _;
        vi p(3); iota(all(p),0);
        sort(all(p), [&](int i, int j) { return col[i] > col[j]; });

        vi ind(n); iota(all(ind),0);
        sort(all(ind), [](int i, int j) {
            if ((i&1) != (j&1)) return (i&1) < (j&1);
            return i < j;
        });

        vi ans(n);
        int pos = 0;
        for (auto c : p) {
            while (col[c]--) {
                ans[ind[pos++]] = c;
            }
        }

        bool ok = true;
        forn(i,n) {
            int j = (i+1)%n;
            if (ans[i] == ans[j]) ok = false;
        }
        
        if (ok) {
            forn(i,n) cout << COL[ans[i]];
            cout << '\n';
        }
        else cout << "IMPOSSIBLE\n";
    }

    return 0;
}
