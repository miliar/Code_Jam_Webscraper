#include<bits/stdc++.h>
using namespace std;
#define pb push_back
typedef vector<double> vi;
typedef long long int ll;
#define FOR(i,n) for(int (i)=0;(i)<(n);++(i))
#define FORI(i,n) for(int (i)=1;(i)<=(n);++(i))
#define REP(i,a,b) for(int (i)=(a);(i)<=(b);++i)
#define REPD(i,a,b) for(int (i)=(a); (i)>=(b);--i)
#define vin vi arr; for(int i=0;i<n;i++){int a;cin>>a;arr.pb(a);}
#define FAST ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);


int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a2.out","w",stdout);

    int t;
    cin>>t;
    for(int z=1;z<=t;z++)
    {
        double D,N;
        cin>>D>>N;
        vi arr,arr2;
        FOR(i,N)
        {
            double a,b;
            cin>>a>>b;
            arr.pb(a);
            arr2.pb(b);
        }

        /*FOR(i,N)
        {
            cout<<arr[i]<<" "<<arr2[i]<<"\n";
        }*/

        vi arr3;

        cout<<fixed;
        cout<<setprecision(6);
        FOR(i,N)
        {
            double p,q;
            p=D-arr[i];
            q=p/arr2[i];

            arr3.pb(q);
        }

        double ans;
        ans=*max_element(arr3.begin(),arr3.end());

        //cout<<ans<<"\n";

        ans=D/ans;

        cout<<fixed;
        cout<<setprecision(6);
        cout<<"Case #"<<z<<": "<<ans<<"\n";;

    }

    return 0;
}
