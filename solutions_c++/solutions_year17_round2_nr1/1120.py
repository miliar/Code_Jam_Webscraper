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

const i64 INF = 1e18 + 9;

int main()
{
#ifdef HOME
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif // HOME
    ios::sync_with_stdio(NULL); cin.tie(NULL);
    int T; cin >> T;

    int d, n;

    For(t, 1, T) {
        cin >> d >> n;
        int x, speed;

        double ans = INF;
        For(i, 1, n) {
            cin >> x >> speed;
            ans = min(ans, d * 1.0 * speed / (d - x));
        }

        cout << "Case #" << t << ": " << fixed << setprecision(15) << ans << '\n';
    }
    return 0;
}
