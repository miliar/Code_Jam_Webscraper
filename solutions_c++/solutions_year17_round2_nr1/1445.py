#include <bits/stdc++.h>
#define int long long
#define pii pair <int,int>
#define piii pair < pair<int,int> ,int>
#define f first
#define s second
#define pb push_back
#define N 100005
#define mod 1000000007
#define INF 4000000000000000000
#define frew freopen ("C:/Users/Sachin/Desktop/out.txt","w",stdout);
#define frer freopen ("C:/Users/Sachin/Desktop/A-large.in","r",stdin);

using namespace std;

main()
{
    frer;
    frew;
    int t;
    cin>>t;
    for(int w=1;w<=t;w++)
    {
        int d,n,i;
        cin>>d>>n;
        pii a[n];
        for(i=0;i<n;i++)
            cin>>a[i].f>>a[i].s;
        sort(a,a+n);
        double ans=((double)d-a[n-1].f)/a[n-1].s;
        double v=a[n-1].s;
        //printf("%.15f\n",ans);
        for(i=n-2;i>=0;i--)
        {
            double di=((double)a[i].s*a[i+1].f-v*a[i].f)/(a[i].s-v);
            //printf("%.15f\n",di);
            if((double)a[i].s>v && di < (double)d)
            {
                v=((double)d-a[i].f)/ans;
            }
            else
            {
                v=a[i].s;
                ans=((double)d-a[i].f)/a[i].s;
            }
            //printf("%.15f\n",ans);
        }
        //printf("%.15f\n",ans);
        double ss=d/ans;
        cout<<"Case #"<<w<<": ";
        printf("%.15f\n",ss);
    }
}
