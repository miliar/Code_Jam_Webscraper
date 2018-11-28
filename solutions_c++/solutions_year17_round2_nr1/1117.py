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




int k[2000];
int s[2000];

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
        int d,n;
        sf2(d,n);
        double time=0;
        for(int i=0; i<n; i++)
        {
            sf2(k[i],s[i]);
            time=max(time,double(d-k[i])/s[i]);
        }
        printf("Case #%d: %.10lf\n",t,d/time);
    }
    
    
    
    return 0;
}























