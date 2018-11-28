#include<iostream>
#include<string>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<array>
#include<vector>
#include<map>
#include<utility>
#include<bitset>
#include<set>
#include<list>
#include<stack>
#include<queue>
#include<utility>
using namespace std;
typedef long long ll;
typedef long double ld;
#define mod 1000000007
#define vec vector<long long>
#define arl(n) array<long long,n>
#define ard(n) array<double,n>
#define sc(n) scanf("%lld",&n)
#define prn(n) printf("%lld\n",n)
#define prs(n) printf("%lld ",n)
#define pr() printf("\n")
#define pb push_back
#define mp make_pair
int main()
{
    ll t;
    sc(t);
    ll tt=1;
    while(t--)
    {
        char a[1007];
        ll k;
        scanf("%s %lld",a,&k);
        ll c=0;
        bool b=0;
        ll l = strlen(a);
        for(ll i=0;i<l;i++)
        {
            if(a[i]=='-')
            {
                if((i+k)>=(l+1))
                {
                    b=1;
                    break;
                }
                c++;
                for(ll j=i;j<(i+k);j++)
                {
                    if(a[j]=='-')
                    a[j]='+';
                    else
                    a[j]='-';
                }
            }
        }
        if(b)
        printf("Case #%lld: IMPOSSIBLE\n",tt);
        else
        printf("Case #%lld: %lld\n",tt,c);
        tt++;
    }
    return 0;
}