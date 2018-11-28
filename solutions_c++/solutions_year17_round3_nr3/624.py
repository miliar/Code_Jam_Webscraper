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



double v[100];


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
        int n,k;
        sf2(n,k);
        double u;
        scanf("%lf",&u);
        for(int i=0; i<n; i++)
        {
            scanf("%lf",&v[i]);
        }
        double l=0,r=1;
        for(int q=0; q<100; q++)
        {
            double m=(r+l)/2;
            double tmp=0;
            for(int i=0; i<n; i++)
            {
                tmp+=(max(.0,m-v[i]));
            }
            if(tmp<=u)
            {
                l=m;
            }
            else r=m;
        }
        double res=1;
        for(int i=0; i<n; i++)
        {
            res*=max(v[i],l);
        }
        printf("Case #%d: %.10lf\n",t,res);
        
    }
    
    
    
    return 0;
}























