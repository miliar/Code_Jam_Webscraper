#include<bits/stdc++.h>
using namespace std;
const int N=1e3+20;
int t,n,k,i,j,T;
double r[N],h[N],R,H,mr,ans,tans;
int main()
{
    cin>>t;
    while(t--)
    {
        ans=0;

        cin>>n>>k;
        for(i=0;i<n;i++) cin>>r[i]>>h[i];

        for(i=0;i<n;i++)
        {
            mr=r[i]; tans=r[i]*h[i];
            priority_queue <pair<double,double>> pq;

            for(j=0;j<n;j++)
            {
                if(j==i) continue;
                pq.push({r[j]*h[j],r[j]});
            }

            for(j=0;j<k-1;j++)
            {
                R=pq.top().first; H=pq.top().second; pq.pop();
                tans+=R;
                mr=max(mr,H);
            }
            tans*=2*acos(-1);
            tans+=acos(-1)*mr*mr;
            ans=max(ans,tans);
        }

        cout<<"Case #"<<++T<<": "<<setprecision(15)<<ans<<"\n";
    }
}
