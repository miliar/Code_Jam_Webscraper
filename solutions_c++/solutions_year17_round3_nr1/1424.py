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

struct info 
{ 
    ld rad, hlen;
    bool operator>(const info& i) const {
        return hlen > i.hlen;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(0);
    int CASES;
    cin >> CASES;
    for (int casenum = 1; casenum <= CASES; casenum++) {
        cout << "Case #" << casenum << ": ";
        //////////////start//////////////

        int N, K;
        cin >> N >> K;
        vector<info> pcs;
        rep(i, N) {
            int R, H;
            cin >> R >> H;
            info in;
            in.rad = R;
            in.hlen = 2 * PI * R * H;
            pcs.push_back(in);
        }

        sort(all(pcs), greater<info>());
        ld result = 0;
        ld largestrad = 0;

        int indx = 0;
        for (indx = 0; indx < N; indx++) {
            if (K <= 1)
                break;
            largestrad = max(largestrad, pcs[indx].rad);
            K--;
            result += pcs[indx].hlen;
        }

        if (K == 1) {
            ld oldtopd = PI * largestrad * largestrad;
            ld bestget = 0;
            for (int i = indx; i < N; i++) {
                ld nextval;
                if (largestrad < pcs[i].rad) {
                    nextval = (pcs[i].rad * pcs[i].rad * PI) + pcs[i].hlen;
                }
                else 
                    nextval = pcs[i].hlen + (largestrad*largestrad*PI);
                if (nextval > bestget) {
                    bestget = nextval;
                }
            }

            result += bestget;
        }

        cout << setprecision(10) << fixed << result << endl;

        //////////////end////////////////
    }
        return 0;

}
