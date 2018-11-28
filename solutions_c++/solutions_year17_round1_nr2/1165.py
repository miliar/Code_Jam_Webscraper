#include <bits/stdc++.h>
using namespace std;
template <class T> int size(const T &x) { return x.size(); }
#define rep(i,a,b) for (decltype(a) i=(a); i<(b); ++i)
#define iter(it,c) for (decltype((c).begin()) \
  it = (c).begin(); it != (c).end(); ++it)
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
const int INF = ~(1<<31);

const double EPS = 1e-9;
const double pi = acos(-1);
typedef unsigned long long ull;
typedef vector<vi> vvi;
typedef vector<vii> vvii;
template <class T> T smod(T a, T b) {
  return (a % b + b) % b; }

bool use1[10], use2[10];
int mx, curr;
vii edges;

void bt(int at)
{
    if(at == size(edges)) return;
    if(!use1[edges[at].first] && !use2[edges[at].second])
    {
        use1[edges[at].first] = true;
        use2[edges[at].second] = true;
        curr++;
        mx = max(mx, curr);
        bt(at+1);
        use1[edges[at].first] = false;
        use2[edges[at].second] = false;
        curr--;
    }
    bt(at+1);
}

int main()
{
    int T;
    cin >> T;
    rep(t,1,T+1)
    {
        int n, p;
        cin >> n >> p;
        vi R(2);
        rep(i,0,n) cin >> R[i];
        vvi Q(2,vi(p));
        vvi lo(2,vi(p));
        vvi hi(2,vi(p));
        rep(i,0,n)
        {
            rep(j,0,p)
            {
                cin >> Q[i][j];
                hi[i][j] = floor(Q[i][j]/0.9/R[i]);
                lo[i][j] = ceil(Q[i][j]/1.1/R[i]);
            }
        }
        if(n == 1)
        {
            R[1] = R[0];
            rep(j,0,p)
            {
                Q[1][j] = Q[0][j];
                hi[1][j] = hi[0][j];
                lo[1][j] = lo[0][j];
            }
        }
        
        memset(use1, 0, sizeof(use1));
        memset(use2, 0, sizeof(use2));
        edges.clear();
        mx = 0;
        curr = 0;
        rep(i,0,p)
        {
            rep(j,0,p)
            {
                //cout << i << " " << j << " " << lo[0][i] << " " << hi[0][i] << " " << lo[1][j] << " " << hi[1][j] << endl;
                if(max(lo[0][i], lo[1][j]) <= min(hi[0][i], hi[1][j]))
                {
                    edges.push_back(ii(i,j));
                }
            }
        }

        bt(0);

        int res = mx;
        cout << "Case #" << t << ": " << res << endl;
    }
    return 0;
}
