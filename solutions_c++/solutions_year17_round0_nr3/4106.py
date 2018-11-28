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



struct foo
{
    int len,l,r;
    foo(int a, int b)
    {
        len=b-a+1;
        l=a;
        r=b;
    }
};


class comp{
    public:
        bool operator()(const foo &a, const foo &b)
        {
            return a.len>b.len||a.len==b.len&&a.l<b.l;
        }
};


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
        set<foo,comp> s;
        s.insert(foo(1,n));
        int mn=INF;
        int mx=0;
        
        for(int i=0; i<k; i++)
        {
            foo tmp=*s.begin();
            s.erase(s.begin());
            int m=(tmp.l+tmp.r)/2;
            int l=tmp.l;
            int r=tmp.r;
            mn=m-l;
            mx=r-m;
            s.insert(foo(l,m-1));
            s.insert(foo(m+1,r));
        }
        
        printf("Case #%d: %d %d\n",t,mx,mn);
    }
    
    
    
    return 0;
}























