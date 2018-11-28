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



string solve(int r, int y, int b, char R, char Y, char B)
{
    string res;
    int tmp=r-y;
    int cnt=b-tmp;
    for(int i=0; i<y; i++)
    {
        res.pb(R);
        if(cnt)
        {
            cnt--;
            res.pb(B);
        }
        res.pb(Y);
    }
    for(int i=0; i<tmp; i++)
    {
        res.pb(R);
        res.pb(B);
    }
    return res;
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
        int n;
        sf(n);
        int r,y,b,tmp;
        sf2(r,tmp);
        sf2(y,tmp);
        sf2(b,tmp);
        if(r>y+b||y>r+b||b>r+y)
        {
            printf("Case #%d: IMPOSSIBLE\n",t);
        }
        else
        {
            string res;
            if(r>=y&&r>=b)
            {
                if(y>=b)
                res=solve(r,y,b,'R','Y','B');
                else
                res=solve(r,b,y,'R','B','Y');
            }
            else if(y>=r&&y>=b)
            {
                if(r>=b)
                res=solve(y,r,b,'Y','R','B');
                else
                res=solve(y,b,r,'Y','B','R');
            }
            else if(b>=r&&b>=y)
            {
                if(y>=r)
                res=solve(b,y,r,'B','Y','R');
                else
                res=solve(b,r,y,'B','R','Y');
            }
            printf("Case #%d: %s\n",t,res.c_str());
        }
    }
    
    
    
    return 0;
}























