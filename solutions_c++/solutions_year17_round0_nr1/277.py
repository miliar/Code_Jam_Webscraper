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

char inv(char x) { return x == '+' ? '-' : '+'; } 

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

    int T; cin >> T;
    forn(cas,T) {
        cout << "Case #" << cas+1 << ": ";
        string s; int n,k;
        cin >> s >> k; n = si(s);

        int ans = 0;
        forn(i,n-k+1) if (s[i] == '-') {
            forn(j,k) s[i+j] = inv(s[i+j]);
            ans++;
        }
        forn(i,n) if (s[i] == '-') ans = -1;
        if (ans == -1) cout << "IMPOSSIBLE" << endl;
        else cout << ans << endl;
    }

    return 0;
}
