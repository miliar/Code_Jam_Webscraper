# include <bits/stdc++.h>

using namespace std;

typedef long long ll;

const int MAXN = (int)1e5, INF = (int)2e9;

int tma[4*MAXN];

void update (int v, int L, int R, int pos, int val)
{
    if (L == R)
    {
        tma[v] = val;
    }
    else
    {
        int m = (L + R) / 2;
        if (pos <= m)
            update (v * 2, L, m, pos, val);
        else
            update (v * 2 + 1, m + 1, R, pos, val);
        tma[v] = max (tma[v * 2], tma[v * 2 + 1]);
    }
}
int getmax (int v, int L, int R, int l, int r)
{
    if (r < L || l > R)
        return -INF;
    if (L >= l && r >= R)
        return tma[v];
    int m = (L + R) / 2;
    return max (getmax (v * 2, L, m, l, r), getmax (v * 2 + 1, m + 1, R, l, r));
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    //freopen("input.txt", "r", stdin);

    vector < int > a1, a2;
    vector < pair < int, int > > v1, v2;
    int n, c, d;
    cin >> n >> c >> d;
    for(int i = 1; i <= n; i++) {
        int b, p;
        char ch;
        cin >> b >> p >> ch;
        if(ch == 'C') {
            a1.push_back(p);
            v1.push_back(make_pair(-b, p));
        }
        else {
            a2.push_back(p);
            v2.push_back(make_pair(-b, p));
        }
    }

    sort(a1.begin(), a1.end());
    sort(a2.begin(), a2.end());
    sort(v1.begin(), v1.end());
    sort(v2.begin(), v2.end());

    int ans = 0;
    bool ok1 = 0, ok2 = 0;
    for(int i = 0; i < v1.size(); i++) {
        pair < int, int > x = v1[i];
        if(x.second <= c) {
            ok1 = 1;
            ans = -x.first;
            break;
        }
    }
    for(int i = 0; i < v2.size(); i++) {
        pair < int, int > x = v2[i];
        if(x.second <= d) {
            ok2 = 1;
            ans -= x.first;
            break;
        }
    }

    if(!((ok1 && ok2) || (a1.size() >= 2 && a1[0] + a1[1] <= c) || (a2.size() >= 2 && a2[0] + a2[1] <= d))) {
        puts("0");
        return 0;
    }

    if(!(ok1 && ok2))
        ans = 0;

    for(int i = 0; i < v1.size(); i++)
        v1[i] = make_pair(v1[i].second, v1[i].first);
    for(int i = 0; i < v2.size(); i++)
        v2[i] = make_pair(v2[i].second, v2[i].first);

    sort(v1.begin(), v1.end());
    sort(v2.begin(), v2.end());

    if(a1.size() >= 2 && a1[0] + a1[1] <= c) {
        memset(tma, -INF, sizeof(tma));
        n = a1.size();
        for(int i = 0; i < n; i++)
            update(1, 1, n, i + 1, -v1[i].second);

        for(int i = 0; i < n; i++) {
            vector < int > :: iterator it = lower_bound(a1.begin() + i + 1, a1.end(), c - a1[i]);
            if(it == a1.end())
                break;
            int x = getmax(1, 1, n, i + 2, (it - a1.begin())+1);
            ans = max(ans, x - v1[i].second);
        }
    }
    if(a2.size() >= 2 && a2[0] + a2[1] <= d) {
        memset(tma, -INF, sizeof(tma));
        n = a2.size();
        for(int i = 0; i < n; i++)
            update(1, 1, n, i + 1, -v2[i].second);

        for(int i = 0; i < n; i++) {
            vector < int > :: iterator it = lower_bound(a2.begin() + i + 1, a2.end(), d - a2[i]);
            if(it == a2.end())
                break;
            int x = getmax(1, 1, n, i + 2, (it - a2.begin())+1);
            ans = max(ans, x - v2[i].second);
        }
    }
    cout << ans << endl;
    return 0;
}
