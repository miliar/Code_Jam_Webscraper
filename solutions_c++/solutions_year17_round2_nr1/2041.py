#include <bits/stdc++.h>

using namespace std;

int main()
{

    freopen("A-large.in","r",stdin);
    freopen("A-largeout.in","w",stdout);

    int t;
    cin>>t;

    int cs=0;

    while(cs<t)    {
        int d,n;
        cin>>d>>n;
        double speed=0;
        for(int i=0;i<n;i++)    {
            int x,y;
            cin>>x>>y;
            speed=max(speed,((d-x)*1.0)/(y*1.0));
        }
        double ans=(d*1.0)/speed;
        printf("Case #%d: %0.10lf\n",++cs,ans);

    }

    return 0;


}
