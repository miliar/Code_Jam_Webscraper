#include <bits/stdc++.h>

using namespace std;

#define FROM_FILE freopen("input.txt", "r", stdin)
#define TO_FILE freopen("output.txt", "w", stdout)

#define ull unsigned long long
#define ll long long

#define PI std::acos(-1)
#define INF 1e10
#define EPS 1e-6
#define prv(v) for (int iqiq = 0; iqiq < v.size(); iqiq++) cout << v[iqiq] << " "; cout << "\n"

struct rec
{
    int r;
    int h;
    double semi;
    double full;
};

bool cmp_r(const rec& p1, const rec& p2)
{
    return p1.r > p2.r;
}

bool cmp_semi(const rec& p1, const rec& p2)
{
    return p1.semi > p2.semi;
}

double solve()
{
    int n, k;
    cin >> n >> k;
    vector<rec> vp(n);
    for (int i = 0; i < n; ++i) {
        cin >> vp[i].r >> vp[i].h;
        vp[i].semi = 2 * PI * vp[i].r * vp[i].h;
        vp[i].full = vp[i].semi + PI * vp[i].r * vp[i].r;
    }

    auto vr = vp;
    sort(vr.begin(), vr.end(), cmp_r);
    sort(vp.begin(), vp.end(), cmp_semi);

    /*for (int i = 0; i < n; ++i)
        cout << vp[i].full << " ";
    cout << "\n";*/

    double ans = 0;
    for (int i = 0; i < n; ++i)
    {
        double cur = vp[i].full;
        int used = 1;

        for (int j = 0; j < n && used < k; ++j)
        {
            if (i != j && vp[i].r >= vp[j].r)
            {
                used++;
                cur += vp[j].semi;
            }
        }

        if (cur > ans && used == k)
            ans = cur;
    }

    return ans;
}

int main()
{
    FROM_FILE;
    TO_FILE;

    int tt;
    cin >> tt;
    cout.precision(8);
    for (int cs = 1; cs <= tt; ++cs)
    {
        cout << "Case #" << cs << ": " << fixed << solve() << "\n";
    }

    return 0;
}
