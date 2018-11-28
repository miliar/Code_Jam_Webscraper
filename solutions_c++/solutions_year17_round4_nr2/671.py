#include <bits/stdc++.h>


#define f(i, a, b) for(int i = a; i <= b; i++)
#define fd(i, a, b) for(int i = a; i >= b; i--)
#define fin ""
#define fou ""
#define mp make_pair
#define fi first
#define se second
#define pb push_back

using namespace std;


typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;

int cnt[1005], t, n, c, p[1005], b[1005], m, dem[1005];

int check(int v)
{
    int remain = 0;
    int res = 0;
    f(i, 1, n)
    {
        if (cnt[i] > v + remain) return -1;
        remain -= cnt[i] - v;
        if (cnt[i] > v) res += (cnt[i] - v);
    }
    return res;
}


int main()
{
    ios_base::sync_with_stdio(0);
    freopen("B-large.in", "r", stdin);
    freopen("B.ou", "w", stdout);
    cin >> t;
    f(tt, 1, t)
    {
        cin >> n >> c >> m;
        f(i, 1, n)
            cnt[i] = 0;
        f(i, 1, c)
            dem[i] = 0;
        int first = 1;
        f(i, 1, m)
        {
            cin >> p[i] >> b[i];
            cnt[p[i]]++;
            dem[b[i]]++;
            first = max(first, dem[b[i]]);
        }
        int last = m;
        int res = 0;
        while (first <= last)
        {
            int mid = (first + last) / 2;
            int v = check(mid);
            if (v != -1)
            {
                res = v;
                last = mid - 1;
            } else first = mid + 1;
        }
        cout << "Case #" << tt << ": " << last + 1 << " " << res << endl;
    }
    return 0;
}
