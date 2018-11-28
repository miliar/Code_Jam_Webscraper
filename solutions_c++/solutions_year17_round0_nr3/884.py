#include <bits/stdc++.h>

#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define FILE "file"

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

const int INF = numeric_limits<int>::max();
const ll LLINF = numeric_limits<ll>::max();
const ull ULLINF = numeric_limits<ull>::max();
const double PI = acos(-1.0);

class Compare
{
public:
    bool operator() (pair<int, int> a, pair<int, int> b)
    {
        if(a.second - a.first != b.second - b.first)
            return a.second - a.first > b.second - b.first;
        return a.first > b.first;
    }
};

int main()
{
    freopen(FILE".in", "r", stdin);
    freopen(FILE".out", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
//    set<pair<int, int>, Compare> s;
//    long long n;
//    cin >> n;
//    s.insert(mp(1, n));
//    int ls, rs;
//    for(int i = 0; i < n; i++)
//    {
//        long long l = s.begin()->first, r = s.begin()->second;
//        s.erase(s.begin());
//        long long m = (l + r) >> 1;
//        ls = m - l, rs = r - m;
//        s.insert(mp(l, m - 1));
//        s.insert(mp(m + 1, r));
//        cout << max(ls, rs) << " " << min(ls, rs) << endl;
//    }
    int T;
    cin >> T;
    for(int tcase = 1; tcase <= T; tcase++)
    {
        cerr << "Case #" << tcase << " done" << endl;
        cout << "Case #" << tcase << ": ";
//        set<pair<int, int>, Compare> s;
//        long long n, k;
//        cin >> n >> k;
//        s.insert(mp(1, n));
//        int ls, rs;
//        for(int i = 0; i < k; i++)
//        {
//            long long l = s.begin()->first, r = s.begin()->second;
//            s.erase(s.begin());
//            long long m = (l + r) >> 1;
//            ls = m - l, rs = r - m;
//            s.insert(mp(l, m - 1));
//            s.insert(mp(m + 1, r));
//        }
//        cout << max(ls, rs) << " " << min(ls, rs) << '\n';
        long long n, k;
        cin >> n >> k;
        long long sum = n - 1, blockSum = n - 1;
        long long current = 1;
        while((current << 1LL) <= k)
        {
            current <<= 1LL;
            sum = (sum + 1) / 2LL - 1;
            blockSum -= current;
        }
        if(sum == 0)
        {
            cout << 0 << " " << 0 << '\n';
            continue;
        }
        long long mx = (sum + 1) / 2, mn = sum - mx;
        long long l = 1, r = current, res = -1;
        while(l <= r)
        {
            long long m = (l + r) >> 1;
            if((mx + mn) * m + (current - m) * (mx + mn - 1) == blockSum)
            {
                res = m;
                break;
            }
            else if((mx + mn) * m + (current - m) * (mx + mn - 1) < blockSum)
                l = m + 1;
            else
                r = m - 1;
        }
        if(k <= current + res - 1)
            cout << mx << " " << mn << '\n';
        else
            cout << max(mx - 1, mn) << " " << min(mx - 1, mn) << '\n';
    }
    return 0;
}
