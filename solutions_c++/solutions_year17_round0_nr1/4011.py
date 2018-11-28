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



void flip(char &c)
{
    if(c=='-') c='+';
    else c='-';
}


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
        string s;
        cin>>s;
        int k;
        cin>>k;
        int res=0;
        int n=s.size();
        for(int i=0; i<=n-k; i++)
        {
            if(s[i]=='-')
            {
                for(int j=0; j<k; j++)
                {
                    flip(s[i+j]);
                }
                res++;
            }
        }
        bool f=0;
        for(int i=0; i<n; i++)
        {
            if(s[i]=='-')
            {
                f=1;
            }
        }
        if(f)
        {
            printf("Case #%d: IMPOSSIBLE\n",t);
        }
        else
        {
            printf("Case #%d: %d\n",t,res);
        }
    }
    
    
    return 0;
}























