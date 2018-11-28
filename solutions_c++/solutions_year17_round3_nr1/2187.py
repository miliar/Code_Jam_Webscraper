#include <bits/stdc++.h>
#define se second
#define  mp make_pair
#define pb push_back
#define fi first
#define maxn 1000001
typedef long long ll;
using namespace std;
#define pi pair<int,int>
double PI = 3.14159265359;
vector<pair<ll,ll> > v;
int main()
{
    int q;
    cin>>q;
    int t =0 ;
    for(int ii=1; ii<=q; ii++)
    {
        int n,k;
        cin>>n>>k;
        v.clear();
        for(int i=0; i<n; i++)
        {ll a,b;
            cin>>a>>b;
            v.pb(mp(a,b));}
        sort(v.begin(),v.end());
        double max1 = 0.0;
        for(int i=n-1; i>=k-1; i--)
        {
            set<ll> s;
            double total = PI*(v[i].fi*v[i].fi)+2*PI*v[i].fi*v[i].se;
            for(int j=i-1; j>=0; j--)
            s.insert(v[j].fi*v[j].se);
            set<ll>::iterator IT = s.end();
            if(s.size()>0)
                IT--;
            int c =0;
            for(c=0; c<k-1; c++)
            {
                total+=2*PI*(*IT);
                IT--;
            }
            max1=max(max1,total);
        }
        printf("Case #%d: %0.6lf\n",ii,max1);
    }
    return 0;
}
