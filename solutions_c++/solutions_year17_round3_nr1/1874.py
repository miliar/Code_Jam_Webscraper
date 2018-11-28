#include<bits/stdc++.h>
using namespace std;
#define ll long long
ll r[1005],h[1005];
long double ans[1005];
pair<ll,ll  > p[1005],p2[1005];
bool compare(pair<ll,ll > p1 ,pair<ll,ll > p2){
    ll r1=p1.first;
    ll h1= p1.second;
    ll r2= p2.second;
    ll h2= p2.first;
    return (r1*h1 < r2*h2);
}
int main()
{
    freopen("test1.txt","r",stdin);
    freopen("file1.txt","w",stdout);
    ll t,n,k;
    ll tot=0;
    cin>>t;
    tot=t;
    while(t--)
    {
        cout<<"Case #"<<(tot-t)<<": ";
        cin>>n>>k;
        for(long i=1;i<=n;i++){
            ans[i]=0;
            cin>>r[i]>>h[i];
            p[i]=make_pair(r[i],h[i]);
            p2[i]=make_pair(h[i],r[i]);

        }
        sort(p+1,p+1+n);
        sort(p2+1,p2+1+n,compare);
        for(long i=k;i<=n;i++){
            long double ans1= 1.0*3.1415926535897932384626*(p[i].first* p[i].first) + 2*3.1415926535897932384626*1.0*p[i].first*p[i].second;
            ans[i]=ans1;
            //cout<<"radius selected: "<<p[i].first<<" : ";
            ll cnt=0;
            ll rad1= p[i].first;
            ll h1= p[i].second;
            long double ans2=0;
            ll track=0;
            for(long j=n;j>=1;j--){
                if(p2[j].first==h1 && p2[j].second==rad1){
                    track++;
                    if(track==1)
                    continue;
                }
                long double  rad2= p2[j].second;
                if(rad2<= rad1){
                    if(cnt==k-1)
                    break;
                    ans2+= 2*3.1415926535897932384626*rad2*p2[j].first*(1.0);
                    //cout<<rad2<<endl;
                    cnt++;
                }
            }
            ans[i]+= ans2;
            //cout<<ans1+ans2<<endl;
        }
        long double ans3=0.0;
        for(long i=k;i<=n;i++){
            ans3=max(ans3,ans[i]);
        }
        printf("%0.12Lf\n",ans3);
    }
}
