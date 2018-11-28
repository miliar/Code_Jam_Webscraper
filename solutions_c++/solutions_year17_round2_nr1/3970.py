#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define speed std::ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define int long long
using namespace std;
int k[1005],s[1005];
main()
{
    //speed
    freopen("inpbhai.in","r",stdin);
    freopen("outbhai.txt","w",stdout);

    int t,c=1,d,n;
    cin>>t;
    while(t--)
    {
        cout<<"Case #"<<c<<": ";
        c++;
        cin>>d>>n;
        for(int i=0; i<n; i++)
        {
            cin>>k[i]>>s[i];
        }
        double prec=1e-6,lo=0.0,hi=1e13,ans=-1e10;
        double maxx=-1e10;
        for(int i=0; i<n; i++)
        {
            double t=double(d-k[i])/double(s[i]);
            if(t>maxx)
            {
                maxx=t;
            }
        }
        //cout<<maxx<<endl;
        //cout<<(hi+lo)/2.0<<endl;
        while(hi-lo>=prec&&lo<=hi)
        {
            double mid=(hi+lo)/2.0;
            double ttak=double(d)/double(mid);
          //  cout<<ttak<<endl;
            //cout<<lo<<" "<<hi<<" "<<mid<<endl;
            if(ttak>=maxx)
            {
                lo=mid+(1e-6);
                ans=max(ans,mid);
            }
            /*if(ttak==maxx)
            {
                ans=mid;
                break;
            }*/
            else
            {
                hi=mid-(1e-6);
            }
            //cout<<ttak<<endl;
        }
        printf("%.7lf\n",ans);
        //cout<<ans<<endl;
    }
    return 0;
}
