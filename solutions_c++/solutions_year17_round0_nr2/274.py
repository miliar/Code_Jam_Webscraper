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

string s;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

    int T; cin >> T;
    forn(cas,T) {
        cout << "Case #" << cas+1 << ": ";
        int n;
        cin >> s; n = si(s);

        int up = 0, down = -1;
        forsn(i,1,n) {
            if (s[i] > s[i-1]) up = i;
            if (s[i] < s[i-1]) {
                down = i;
                break;
            }
        }
        if (down != -1) {
            s[up]--;
            forsn(i,up+1,n) s[i] = '9';
            while (s[0] == '0') s = s.substr(1);
        }
        cout << s << endl;
    }

    return 0;
}
