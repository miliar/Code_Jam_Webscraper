#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.in","w",stdout);
    int t,cs=0;
    cin >> t;
    while (t--)
    {
        cs++;
        int n,d,k[1001],s[1001];
        double ans,miin=-1.0;
        cin >> d >> n;
        double x;
        for (int i=0;i<n;i++)
        {
            cin >> k[i] >> s[i];
            miin=max(miin,(double)(d-k[i])/(double)s[i]);
        }
        ans = (double)d/miin;
        cout <<"Case #"<<cs<<": "<<fixed << setprecision(6) << ans <<endl;
    }
    return 0;
}
