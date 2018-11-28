#include<bits/stdc++.h>
using namespace std;
 
// Numeric Constants
#define MOD 1000000007
#define maxs 250005
#define mins 1005
#define eps 0.000000000001
#define imax 2000000200
#define llmax 1000000002000000000ll
 
// Others
#define ll long long int
#define pb push_back
#define gc getchar_unlocked
#define iosbase ios_base::sync_with_stdio(false)
#define pii pair<int,int>
#define pll pair<ll,ll>
#define ppi pair<pair<int,int>,int>
#define ppl pair<pll,ll>
#define vi vector<int>
#define sc scanf
#define pr printf
#define lld I64d
#define F first
#define S second
#define siter set<int>::iterator
#define p_pq priority_queue
#define ub upper_bound
#define lb lower_bound

ll a[10][19];
ll po[19];

int main()
{
    po[0]=1;
    for(ll i=1;i<19;++i)
        po[i]=po[i-1]*10;
    for(ll i=0;i<10;++i)
    {
        a[i][0]=0;
        for(ll j=1;j<19;++j)
            a[i][j]=(a[i][j-1]*10+i);
    }
	ll t,n;
    scanf("%lld",&t);
    for(ll o=1;o<=t;++o)
    {
        scanf("%lld",&n);
        ll sum=0;
        for(ll j=18;j>=1;--j)
        {
            for(ll i=9;i>=0;--i)
            {
                if(sum+a[i][j]<=n)
                {
                    sum+=(i*po[j-1]);
                    break;
                }
            }
        }
        printf("Case #%lld: %lld\n",o,sum);
    }
	return 0;
}