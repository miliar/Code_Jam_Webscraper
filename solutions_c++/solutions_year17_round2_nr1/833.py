#include <bits/stdc++.h>

using namespace std;

const int maxN = 1e3+10;
int test, N, D;
int A[maxN], speed[maxN];

int main()
{
    freopen("googlejam.inp","r",stdin);
    freopen("googlejam.out","w",stdout);
    cin >> test;
    for (int t=1; t <= test; t++)
    {
        printf("Case #%d: ",t);
        cin >> D >> N;
        for (int i=1; i <= N; i++) cin >> A[i] >> speed[i];
        double maxtime = 0, ans = 1e18;
        for (int i=1; i <= N; i++)
            ans = min(ans,double(1ll*D*speed[i])/(D-A[i]));
        printf("%.9lf\n",ans);
    }
}
