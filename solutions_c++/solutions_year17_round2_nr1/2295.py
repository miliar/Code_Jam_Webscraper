#include <bits/stdc++.h>
using namespace std;
template <class T> int size(const T &x) { return x.size(); }
#define rep(i,a,b) for (decltype(a) i=(a); i<(b); ++i)
#define iter(it,c) for (decltype((c).begin()) it = (c).begin(); it != (c).end(); ++it)
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
typedef unsigned long long ull;
const int INF = ~(1<<31);

const double EPS = 1e-9;
const double pi = acos(-1);
typedef unsigned long long ull;
typedef vector<vi> vvi;
typedef vector<vii> vvii;
template <class T> T smod(T a, T b) {
  return (a % b + b) % b; }

int main()
{
    int T;
    cin >> T;
    cout << setprecision(9) << fixed;
    rep(t,1,T+1)
    {
        int d, n;
        cin >> d >> n;
        double mx = 0;
        rep(i,0,n)
        {
            double k, s;
            cin >> k >> s;
            mx = max(mx, (d-k)/s);
        }
        cout << "Case #" << t << ": " << d/mx << endl;
    }
    return 0;
}
