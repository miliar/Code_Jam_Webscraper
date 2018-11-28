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

char a[30][30];

int main()
{
	ll t,r,c;
    scanf("%lld",&t);
    for(ll o=1;o<=t;++o)
    {
        scanf("%lld%lld",&r,&c);
        for(ll i=0;i<r;++i)
        {
            char ch='*';
            for(ll j=0;j<c;++j)
            {
                cin>>a[i][j];
                if(a[i][j]=='?')
                {
                    if(ch!='*')
                        a[i][j]=ch;
                }
                else
                    ch=a[i][j];
            }
        }
        for(ll i=0;i<r;++i)
        {
            char ch='*';
            for(ll j=c-1;j>=0;--j)
            {
                if(a[i][j]=='?')
                {
                    if(ch!='*')
                        a[i][j]=ch;
                }
                else
                    ch=a[i][j];
            }
        }
        for(ll i=0;i<r;++i)
        {
            for(ll j=0;j<c;++j)
            {
                if(a[i][j]=='?')
                {
                    if(i!=0&&a[i-1][j]!='?')
                        a[i][j]=a[i-1][j];
                }
            }
        }
        for(ll i=r-1;i>=0;--i)
        {
            for(ll j=0;j<c;++j)
            {
                if(a[i][j]=='?')
                {
                    if((i!=r-1)&&a[i+1][j]!='?')
                        a[i][j]=a[i+1][j];
                }
            }
        }
        printf("Case #%lld:\n",o);
        for(ll i=0;i<r;++i)
        {
            for(ll j=0;j<c;++j)
            {
                cout<<a[i][j];
            }
            cout<<endl;
        }
    }
	return 0;
}