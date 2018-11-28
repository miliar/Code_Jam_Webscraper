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
#define frer freopen ("C:/Users/Sachin/Desktop/B-small-attempt3.in","r",stdin);

using namespace std;

main()
{
    frer;
    frew;
    int t;
    cin>>t;
    for(int w=1;w<=t;w++)
    {
        int i,n,r,o,y,g,b,vv;
        cin>>n>>r>>o>>y>>g>>b>>vv;
        pii a[3];
        a[0]={r,0};
        a[1]={y,1};
        a[2]={b,2};
        sort(a,a+3);
        reverse(a,a+3);
        vector <int> v;
        int f=0;
        if(a[0].f > a[1].f+a[2].f)
        {
            f=1;
        }
        while(f==0 && v.size()<n)
        {
            if(a[0].f!=a[1].f)
            {
                v.pb(a[0].s);
                v.pb(a[1].s);
                a[0].f--;
                a[1].f--;
                if(a[2].f>0)
                {
                    v.pb(a[0].s);
                    a[0].f--;
                    v.pb(a[2].s);
                    a[2].f--;
                }
            }
            else
            {
                v.pb(a[0].s);
                a[0].f--;
                if(a[1].f>0)
                {
                    v.pb(a[1].s);
                    a[1].f--;
                }
                if(a[2].f>0)
                {
                    v.pb(a[2].s);
                    a[2].f--;
                }
            }
        }
        cout<<"Case #"<<w<<": ";
        if(f==1)
            cout<<"IMPOSSIBLE\n";
        else
        {
            for(i=0;i<n;i++)
            {
                if(v[i]==0)
                    cout<<"R";
                else if(v[i]==1)
                    cout<<"Y";
                else
                    cout<<"B";
            }
            cout<<"\n";
        }
    }
}
