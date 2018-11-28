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



int d[200];
int s[200];
int dist[200][200];
double res[300];

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
        int n,q;
        sf2(n,q);
        for(int i=0; i<n; i++)
        {
            sf2(d[i],s[i]);
        }
        for(int i=1; i<n; i++)
        {
            res[i]=1e18;
        }
        int tmp;
        for(int i=0; i<n; i++)
        {
            for(int j=0; j<n; j++)
            {
                sf(dist[i][j]);
            }
        }
        for(int i=0; i<q; i++)
        {
            sf2(tmp,tmp);
        }
        for(int i=0; i<n; i++)
        {
            ll sum=0;
            for(int j=i+1; j<n; j++)
            {
                sum+=dist[j-1][j];
                if(d[i]>=sum)
                {
                    res[j]=min(res[j],res[i]+(double)sum/s[i]);
                }
            }
        }
        printf("Case #%d: %.10lf\n",t,res[n-1]);
    }
    
    
    
    return 0;
}























