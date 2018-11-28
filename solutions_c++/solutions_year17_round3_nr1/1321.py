#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;
typedef long long ll;
typedef pair<ll, ll> ii;
double pi = 314159.265358979323;
double xx = 100000;
vector<ii> v;
int main()
{
    freopen("ain.txt", "r", stdin);
    freopen("aout.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int z = 1; z <= t; z++)
    {
        int n, k;
        scanf("%d%d", &n, &k);
        v.clear();
        for (int i = 0; i < n; i++)
        {
            ll r, h;
            scanf("%lld%lld", &r, &h);
            v.push_back(ii(r*r, 2*h*r));
        }
        sort(v.begin(), v.end());
        set<ll> s;
        ll sum = 0;
        ll top = 0;
        for (int i = 0; i < k; i++)
            s.insert(v[i].second);
        for (int i = 0; i < k; i++)
            sum += v[i].second;
        top = v[k-1].first;
        ll ans = sum + top;
        for (int i = k; i < n; i++)
        {
            ans = max(ans,
                sum-(*s.begin())+v[i].second+v[i].first);
            if (v[i].second >= *s.begin())
            {
                sum -= *s.begin();
                sum += v[i].second;
                s.erase(s.begin());
                s.insert(v[i].second);
                top = v[i].first;
                ans = max(ans, sum + top);
            }
        }
        printf("Case #%d: %.7lf\n", z, pi*ans/xx);
    }
    return 0;
}
