#include <bits/stdc++.h>
using namespace std;
const int inf=1e5+9;
const int mod=1e9+7;
int occ[5];
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int t,n,p,a;
    cin>>t;
    for (int test=1;test<=t;++test)
    {
        cin>>n>>p;
        for (int i=0;i<5;++i)occ[i]=0;
        for (int i=0;i<n;++i)
        {
            cin>>a;
            occ[a%p]++;
        }
        cout<<"Case #"<<test<<": ";
        if (p==2)
            cout<<occ[0]+(occ[1]+1)/2<<endl;
        else if (p==3)
        {
            int ans=occ[0];
            int k=min(occ[1],occ[2]);
            occ[1]-=k;
            occ[2]-=k;
            ans+=k;
            ans+=occ[1]/3;
            ans+=occ[2]/3;
            if (occ[1]%3!=0)++ans;
            if (occ[2]%3!=0)++ans;
            cout<<ans<<endl;
        }
        else
        {
            int ans=occ[0];
            ans+=occ[2]/2;
            occ[2]%=2;
            int k=min(occ[1],occ[3]);
            occ[1]-=k;
            occ[3]-=k;
            ans+=k;
            if (occ[2])
            {
                if (occ[3]>1)
                    ans++,occ[3]-=2;
                if (occ[1]>1)
                    ans++,occ[1]-=2;
            }
            ans+=occ[1]/4;
            ans+=occ[3]/4;
            if (occ[1]%4!=0)++ans;
            if (occ[3]%4!=0)++ans;
            cout<<ans<<endl;
        }
    }
}
