#include <bits/stdc++.h>
using namespace std;
#define DB(v) cerr << #v << ' ' << v << endl
#define sz(v) int(v.size())
#define For(i, a, b) for(int i = a;i <= b; ++i)
#define fi first
#define se second

template <typename T>
inline ostream &operator << (ostream &out, const vector <T> &v) {
    for(auto to: v)
        out << to << ' ';
    out << '\n';
    return out;
}

template <typename T>
inline ostream &operator << (ostream &out, const set <T> &v) {
    for(auto to: v)
        out << to << ' ';
    out << '\n';
    return out;
}


typedef pair <int,int> pii;
typedef long long i64;

const int N = 109;
const i64 INF = 1e18;

double dp [N][N];

vector <int> dist;
vector <pii> horse;
vector <int> pref_sum;

int n;

void get_graph () {
    int x;
    For(i, 1, n) {
        For(j, 1, n)  {
            cin >> x;
            if(j == i + 1) {
                dist[i] = x;
            }
        }
    }
}

void prepare() {
    pref_sum.assign(n + 1, 0);
    For(i, 2, n) {
        pref_sum[i] = pref_sum[i - 1] + dist[i - 1];
    }

    For(i, 1, n) {
        For(j, 1, n) {
            dp[i][j] = INF;
        }
    }
    for(int j = 1;j <= n; ++j)
        dp[n][j] = 0;
}

int get_dist (int l, int r) {
    return pref_sum[r] - pref_sum[l];
}

int main()
{
#ifdef HOME
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif // HOME
    ios::sync_with_stdio(NULL); cin.tie(NULL);
    int T, Q; cin >> T;

    int u, v;
    For(t, 1, T) {
        cout << "Case #" << t << ": ";
        cin >> n >> Q;
        dist.resize(n + 1);
        horse.resize(n + 1);
        For(i, 1, n) {
            cin >> horse[i].fi >> horse[i].se;
        }

        get_graph();
        cin >> u >> v;
        prepare();

        for(int i = n - 1;i >= 1;i--) {
            for(int j = 1;j <= i; ++j) {
                if(get_dist(j, i + 1) <= horse[j].fi)
                    dp[i][j] = min(dp[i][j], dp[i + 1][j] + dist[i] * 1.0 / horse[j].se);

                if(dist[i] <= horse[i].fi)
                    dp[i][j] = min(dp[i][j], dp[i + 1][i] + dist[i] * 1.0 / horse[i].se);
            }
        }
        cout << fixed << setprecision(15) << dp[1][1] << '\n';
    }
    return 0;
}
