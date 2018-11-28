#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz size()
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define popc32(x) __builtin_popcount(x)
#define popc64(x) __builtin_popcountll(x)
#define MOD 1000007
#define INF 1e9
#define EPS 1e-9

typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long long ll;
typedef long double ld;

static const double PI = 2 * acos(0);

int main() {
    ios::sync_with_stdio(false); cin.tie(0);
    //////////////start//////////////

    int T;
    cin >> T;
    for (int tc = 1; tc <= T; tc++) {
        cout << "Case #" << tc << ": ";
        ll N, K;
        cin >> N >> K;

        map<ll, ll> curvals;
        curvals.insert(mp(N, 1));
        priority_queue<ll> q;
        q.push(N);
        ll dist = 0;

        ll k = 0;
        while (!q.empty()) {
            ll top = q.top();
            q.pop();
            ll topappear = curvals[top];
            k += topappear;
            if (k >= K) {
                dist = top;
                break;
            }
            ll h1 = top/2, h2 = top - h1 - 1;

            ll h1v = curvals[h1];
            ll h2v = curvals[h2];
            curvals[h1] += topappear;
            curvals[h2] += topappear;
            if (h1v == 0)
                q.push(h1);
            if (h1 != h2 && h2v == 0) 
                q.push(h2);
        }

        cout << dist/2 << " " << (dist-1)/2 << endl;
    }

    //////////////end////////////////
    return 0;
}
