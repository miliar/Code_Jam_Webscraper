#include<bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int (i)=(a);(i)<=(b);++i)
#define repd(i,a,b) for(int (i)=(a); (i)>=(b);--i)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define ll long long int

int main()
{
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        int i,j,n1,ans=2,n2,a[100],b[100];
        cin>>n1>>n2;
        rep(i,1,n1+n2)
        {
                cin>>a[i]>>b[i];
        }
        if(n1<=1&&n2<=1)
            ans=2;
        else if(n1==2||n2==2)
        {
            if((b[2]-a[1]<=720&&b[2]>a[1])||(b[1]-a[2]<=720&&b[1]>a[2])||(a[1]-b[2]>=720)||(a[2]-b[1]>=720))
                ans=2;
            else ans=4;
        }
        cout<<"Case #"<<tt<<": "<<ans<<endl;
    }
        return 0;
}
