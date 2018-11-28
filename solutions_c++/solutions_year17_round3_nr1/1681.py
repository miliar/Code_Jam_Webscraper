#include <bits/stdc++.h>

using namespace std;

const double pi = M_PI;

struct pc
{
    long long r, h;
    pc(long long _r, long long _h) :
    r(_r),
    h(_h)
    {}
    friend bool operator < (pc& a, pc& b)
    {
        return a.r*a.h > b.r*b.h;
    }
};

int main()
{
    #ifdef FILEIO
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    ios_base::sync_with_stdio(false);

    int tn;
    cin >> tn;
    for(int tc=1; tc<=tn; tc++)
    {
        int n, k;
        cin >> n >> k;
        long long r, h;
        vector< pc > pcs;
        for(int i=0; i<n; i++)
        {
            cin >> r >> h;
            pcs.push_back(pc(r, h));
        }
        sort(pcs.begin(), pcs.end());
        double ans = 0;
        long long maxr = 0;
        double current;
        for(int i=0; i<k; i++)
        {
            if(i==k-1)
                current = ans;
            ans += pcs[i].r*pcs[i].h*2*pi;
            maxr = max(maxr, pcs[i].r);
        }
        ans += pi*maxr*maxr;
        for(int i=k; i<n; i++)
            if(pcs[i].r > maxr)
                ans = max(ans, current + pcs[i].r*pcs[i].h*2*pi + pi*pcs[i].r*pcs[i].r);
        cout << fixed << setprecision(9) << "Case #" << tc << ": " << ans << endl;
    }

    return 0;
}
