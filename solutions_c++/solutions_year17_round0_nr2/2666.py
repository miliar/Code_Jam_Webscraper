#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forab(i, k, n) for (int i = (int)(k); i < (int)(n); i++)
#define forba(i, n, k) for (int i = (int)(n) - 1; i >= (int)(k); i--)

#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x)*(x))
#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define db(x) cout << #x << " = " << x << endl

using namespace std;

typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long ll;
typedef double ld; 

const ld pi = acos(-1.0);
const ld eps = 1e-8;
const int INF = (int)1e9;
const int MAXN = 500500;

int T;
int n;
string s, t;

bool ok() {
    assert(s.size() == t.size());
    if (s < t) {
        return 0;
    }
    for (int i = 0; i < (int)t.size() - 1; i++) {
        if (t[i] > t[i + 1]) {
            return 0;
        }
    }
    return 1;
}

bool get(int pos) {
    if (pos == n) {
        return 1;
    }
    
    int last = (pos > 0 ? t[pos - 1] - '0' : -1);
    int cur = (s[pos] - '0');
    
    // -> max
    if (last <= cur) {
        t[pos] = '0' + cur;
        if (get(pos + 1)) {
            return 1;
        }
    }
    
    // -> dec 1
    if (last <= cur - 1 && cur > 0) {
        t[pos] = '0' + cur - 1;
        for (int i = pos + 1; i < n; i++) {
            t[i] = '9';
        }
        
        if (ok()) {
            return 1;
        }
    }
    
    return 0;
}

int main() {

    cin >> T;
    forn(tt, T) {
        printf("Case #%d: ", tt + 1);
        
        cin >> s;
        n = (int)s.size();
        t = s;
        
        assert(get(0));
        assert(ok);
                
        while (!t.empty() && t[0] == '0') {
            t = t.substr(1, t.size() - 1);   
        }
        assert(!t.empty());
        
        cout << t << '\n';        
    }
    
    return 0;
}