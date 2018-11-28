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

int main()
{
    int t;
    cin >> t;
    rep(j,0,t)
    {
        map<ll,ll> segs;
        ll n, k, c = 0;
        cin >> n >> k;
        segs[n] = 1;
        pair<ll,ll> res;
        while(true)
        {
            map<ll,ll>::reverse_iterator it = segs.rbegin();
            n = it->first;
            if(k <= it->second)
            {
                res = make_pair(n/2, (n-1)/2);
                break;
            }
            k -= it->second;
            segs[n/2] += it->second;
            segs[(n-1)/2] += it->second;
            segs.erase(it->first);
        }
        cout << "Case #" << j+1 << ": " << res.first << " " << res.second << endl;
    }
    return 0;
}
