#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define sci(fd) scanf("%d",&fd)
#define scll(fd) scanf("%lld",&fd)
#define scd(fd) scanf("%lf",&fd)
#define pb push_back
#define mp make_pair
#define MOD 1000000007
#define PI 3.1415926535897932
#define pii pair < int,int > 
#define pll pair < ll,ll >
#define fi first
#define se second
#define LOGN 20
const ll infi=1000000000000000009;
ll ar[1009][2];
ll ar1[1009][2];
int main()
{
    int t;
    sci(t);
    ll y=0;
    while(t--)
    {
        y++;
        ll n,k,i,j;
        scll(n);
        scll(k);
        for(i=0;i<n;i++)
        {

            scll(ar1[i][0]);
            scll(ar1[i][1]);
            ar[i][0]=ar1[i][0];
            ar[i][1]=ar1[i][1];
        }
        ll ans=0.0;
        k--;
        for(i=0;i<n;i++)
        {
            multiset < ll  > mt;
            ll curr=(2)*ar[i][0]*ar[i][1]+ar[i][0]*ar[i][0];
            for(j=0;j<n;j++)
            {
                if(j==i)
                continue;
                if(ar1[j][0]<=ar1[i][0])
                {
                    // /printf("%lf\n",curr);
                    mt.insert((2LL)*ar[j][0]*ar[j][1]);
                    curr+=(2LL)*ar[j][0]*ar[j][1];
                }
                if(mt.size()>k)
                {
                    //printf("%lld\n",mt.size());
                    curr=curr-(*(mt.begin()));
                    mt.erase(mt.begin());
                }
            }
            //printf("%lld\n",curr);
            //printf("%d\n",mt.size());
            if(mt.size()==k)
            ans=max(ans,curr);
        }
        double an=PI*ans;
        printf("Case #%lld: %0.9lf\n",y,an);
    }
    return 0;
}