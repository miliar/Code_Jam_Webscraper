/**
 *    @author     : Maruf Tuhin
 *    @College    : CUET CSE 11
 *    @Topcoder   : the_redback
 *    @CodeForces : the_redback
 *    @UVA        : the_redback
 *    @link       : http://www.fb.com/maruf.2hin
 */

#include <bits/stdc++.h>
using namespace std;

typedef long long          ll;
typedef unsigned long long llu;

#define ft         first
#define sd         second
#define mp         make_pair
#define pb(x)      push_back(x)
#define all(x)     x.begin(),x.end()
#define allr(x)    x.rbegin(),x.rend()
#define mem(a,b)   memset(a,b,sizeof(a))
#define sf(a)      scanf("%lld",&a)
#define ssf(a)     scanf("%s",&a)
#define sf2(a,b)   scanf("%lld %lld",&a,&b)
#define sf3(a,b,c) scanf("%lld %lld %lld",&a,&b,&c)
#define inf        1e9
#define eps        1e-9
#define mod        1000000007
#define NN         100010

#ifdef  redback
#define bug printf("line=%d\n",__LINE__);
#define debug(args...) {cout<<":: "; dbg,args; cerr<<endl;}
struct  debugger{template<typename T>debugger& operator ,(const T& v){cerr<<v<<" ";return *this;}}dbg;
#else
#define bug
#define debug(args...)
#endif  //debugging macros

char a[20];

ll fixLast(ll n)
{
    for(int i=n;i>0;i--)
    {
        if(a[i]<a[i-1])
        {
            a[i]='9';
            a[i-1]--;
        }
        else
            return 0;
    }
}

int main()
{
    #ifdef redback
        freopen("C:\\Users\\Maruf\\Desktop\\in.txt","r",stdin);
    #endif

    ll t=1,tc;
    sf(tc);
    ll l,m,n;
    while(tc--) {
        ll i,j,k;
        int smaller=0;
        scanf("%s",a);
        l=strlen(a);

        for(i=0;i<l-1;i++)
        {
            if(smaller)
                a[i]='9';
            else if(a[i]>a[i+1])
            {
                    a[i]--;
                    fixLast(i);
                    smaller=1;
            }

        }
        if(smaller)
            a[l-1]='9';

        printf("Case #%lld: ",t++);
        if(a[0]!='0')
            printf("%c",a[0]);
        for(i=1;i<l;i++)
        {
            printf("%c",a[i]);
        }
        puts("");
    }
    return 0;
}
