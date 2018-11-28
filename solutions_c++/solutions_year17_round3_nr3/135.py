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
    cin.sync_with_stdio(false);
    cout << setprecision(9) << fixed;
    int T;
    cin >> T;
    rep(t,1,T+1)
    {
        int n, k;
        cin >> n >> k;
        assert(n == k);
        long double U;
        cin >> U;
        vector<long double> arr(n);
        long double mn = 1;
        rep(i,0,n)
        {
            cin >> arr[i];
            mn = min(mn, arr[i]);
        }
        long double lim = 0.00009;
        while(U > lim)
        {
            rep(i,0,n)
            {
                if(U > lim && abs(arr[i]-mn) < lim)
                {
                    arr[i] += 0.0001;
                    U -= 0.0001;
                }
            }
            mn += 0.0001;
        }

        long double res = 1;
        rep(i,0,n)
        {
            res *= arr[i];
        }

        cout << "Case #" << t << ": " << res << endl;
    }

    return 0;
}
