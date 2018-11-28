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


int main()
{
    ll t,n,k,ans;
    scanf("%lld",&t);
    for(ll o=1;o<=t;++o)
    {
        scanf("%lld%lld",&n,&k);
        ans=n;
        map<ll,ll> m,temp;
        map<ll,ll>::iterator it;
        m[n]=1;
        ll sum=0;
        ll cur=1;
        while(cur+sum<k)
        {
            temp.clear();
            for(it=m.begin();it!=m.end();++it)
            {
                temp[(it->first)/2]+=(it->second);
                temp[(it->first)/2-(it->first+1)%2]+=(it->second);
            }
            m.clear();
            for(it=temp.begin();it!=temp.end();++it)
                m[it->first]=it->second;
            sum=sum+cur;
            if(cur>=(1e18-sum)/2)
                break;
            cur*=2;
        }
        if(m.size())
        {
             it=m.end();
        do
        {
            it--;
            if(sum+(it->second)>=k)
            {
                ans=(it->first);
                break;
            }
            else
                sum+=(it->second);
        }while(it!=m.begin());
        }
        printf("Case #%lld: %lld %lld\n",o,(ans/2),(ans/2-(ans+1)%2));
    }
    return 0;
}