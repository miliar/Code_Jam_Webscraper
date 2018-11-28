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




ll d[1011][1011];
ll m[1011];


double pi=2*acos(0);


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
        memset(m,0,sizeof(m));
        int n,k;
        sf2(n,k);
        vector<pii> v;
        int a,b;
        for(int i=0; i<n; i++)
        {
            sf2(a,b);
            v.pb(pii(a,b));
        }
        sort(v.begin(),v.end(),greater<pii>());
        for(int i=0; i<n; i++)
        {
            for(int j=0; j<=i; j++)
            {
                d[i+1][j+1]=max(d[i+1][j+1],m[j])+2LL*v[i].first*v[i].second;
                if(j==0) d[i+1][j+1]+=(ll)v[i].first*v[i].first;
            }
            for(int j=0; j<=i+1; j++)
            {
                m[j]=max(d[i+1][j],m[j]);
            }
        }
        printf("Case #%d: %.10lf\n",t,pi*m[k]);
    }
    
    
    
    return 0;
}























