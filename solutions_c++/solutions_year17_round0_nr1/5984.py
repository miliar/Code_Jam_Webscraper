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

string s;

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
        cin>>s;
        sf(k);
        ll count=0;
        ll l=(ll)s.size();

        for(i=0;i<l;i++)
        {
            if(s[i]=='-')
            {
                if(i+k>l)
                {
                    count=-1;
                    break;
                }
                count++;
                for(j=i;j<(i+k);j++)
                {
                    if(s[j]=='+')
                        s[j]='-';
                    else
                        s[j]='+';
                }
            }
        }
        if(count==-1)
            printf("Case #%lld: IMPOSSIBLE\n",t++);
        else
            printf("Case #%lld: %lld\n",t++,count);
    }
    return 0;
}
