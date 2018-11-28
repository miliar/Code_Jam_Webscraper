#include<bits/stdc++.h>
#include<cstdlib>   
#define sf(x) scanf("%d",&x)
#define pf(x) printf("%d ",x)
#define sf2(x,y) scanf("%d %d",&x,&y)
#define pf2(x,y) printf("%d %d ",x,y)
#define sf3(x,y,z) scanf("%d %d %d",&x,&y,&z)
#define pf3(x,y,z) printf("%d %d %d ",x,y,z)
#define sfc(c) scanf(" %c",&c)
#define pfc(c) printf("%c",c)
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define INF 2000000008
#define ENDL puts("")


using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef unsigned int uint;
typedef long double ld;



int d[1500];


int main()
{
    /*
    freopen("china.in","r",stdin);
    freopen("china.out","w",stdout);
    /**/
    
    int T;
    sf(T);
    for(int t=1; t<=T; t++)
    {
        memset(d,0,sizeof(d));
        int n,m;
        sf2(n,m);
        vector<pii> v1,v2;
        int a,b;
        for(int i=0; i<n; i++)
        {
            sf2(a,b);
            v1.pb(pii(a,b));
        }
        for(int i=0; i<m; i++)
        {
            sf2(a,b);
            v2.pb(pii(a,b));
        }
        if(n&&m)
        {
            printf("Case #%d: 2\n",t);
        }
        else
        {
            int res=0;
            if(n)
            {
                if(n==1) res=2;
                else
                {
                    sort(v1.begin(),v1.end());
                    if(v1[1].second-v1[0].first<=720||1440+v1[0].second-v1[1].first<=720) res=2;
                    else res=4;
                }
            }
            else
            {
                if(m==1) res=2;
                else
                {
                    sort(v2.begin(),v2.end());
                    if(v2[1].second-v2[0].first<=720||1440+v2[0].second-v2[1].first<=720) res=2;
                    else res=4;
                }
            }
            printf("Case #%d: %d\n",t,res);
        }
    }
    
    
    
    return 0;
}























