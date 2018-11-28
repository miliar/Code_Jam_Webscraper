#include <bits/stdc++.h>

using namespace std;

#define FROM_FILE freopen("input.txt", "r", stdin)
#define TO_FILE freopen("output.txt", "w", stdout)

#define ull unsigned long long
#define ll long long

#define PI 3.1415926535
#define INF 1e9
#define EPS 1e-6
#define prv(v) for (int iqiq = 0; iqiq < v.size(); iqiq++) cout << v[iqiq] << " "; cout << "\n"

struct pt
{
    int from;
    int to;
};

bool cmp(const pt& p1, const pt& p2)
{
    return p1.from < p2.from;
}

int solve()
{
    int ac, aj;
    cin >> ac >> aj;
    vector<pt> vc(ac), vj(aj);

    for (int i = 0; i < ac; ++i)
        cin >> vc[i].from >> vc[i].to;
    for (int i = 0; i < aj; ++i)
        cin >> vj[i].from >> vj[i].to;

    sort(vc.begin(), vc.end(), cmp);
    sort(vj.begin(), vj.end(), cmp);

    if (ac == 2)
    {
        if (vc[1].to - vc[0].from > 720 && vc[1].from - vc[0].to < 720)
            return 4;
        return 2;
    }

    if (aj == 2)
    {
        if (vj[1].to - vj[0].from > 720 && vj[1].from - vj[0].to < 720)
            return 4;
        return 2;
    }

    return 2;
}

int main()
{
    FROM_FILE;
    TO_FILE;

    int tt;
    cin >> tt;
    for (int cs = 1; cs <= tt; ++cs)
    {
        cout << "Case #" << cs << ": " << solve() << "\n";
    }

    return 0;
}
