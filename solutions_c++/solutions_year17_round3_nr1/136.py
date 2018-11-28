#include <bits/stdc++.h>
using namespace std;
template <class T> int size(const T &x) { return x.size(); }
#define rep(i,a,b) for (decltype(a) i=(a); i<(b); ++i)
#define iter(it,c) for (decltype((c).begin()) it = (c).begin(); it != (c).end(); ++it)
typedef pair<long long, long long> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
typedef unsigned long long ull;
const int INF = (1LL<<61);

const double EPS = 1e-9;
const double pi = acos(-1);
typedef unsigned long long ull;
typedef vector<vi> vvi;
typedef vector<vii> vvii;
template <class T> T smod(T a, T b) {
  return (a % b + b) % b; }

int n, k;
ii pancakes[1000];

ll mem[1000][1001];

ll dp(int at, int left)
{
    if(left == 0) return 0;
    if(at == n) return -INF;
    if(mem[at][left] == -1)
    {
        if(left == k)
        {
            mem[at][left] = max(dp(at+1, left), dp(at+1, left-1) + pancakes[at].first*pancakes[at].first + 2*pancakes[at].first*pancakes[at].second);
        }
        else
        {
            mem[at][left] = max(dp(at+1, left), dp(at+1, left-1) + 2*pancakes[at].first*pancakes[at].second);
        }
    }
    return mem[at][left];
}

int main()
{
    cin.sync_with_stdio(false);
    cout << setprecision(9) << fixed;
    int T;
    cin >> T;
    rep(t,1,T+1)
    {
        cin >> n >> k;
        rep(i,0,n)
        {
            cin >> pancakes[i].first >> pancakes[i].second;
        }
        sort(pancakes, pancakes+n, greater<ii>());
        memset(mem, -1, sizeof(mem));
        double res = pi * dp(0,k);
        cout << "Case #" << t << ": " << res << endl;
    }

    return 0;
}
