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




void go(string &s, int n)
{
    if(n==s.size()-1) return;
    if(s[n]<=s[n+1])
    {
        go(s,n+1);
    }
    if(s[n]>s[n+1])
    {
        s[n]--;
        for(int i=n+1; i<s.size(); i++)
        {
            s[i]='9';
        }
    }
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
        if(s.size()==1)
        {
            printf("Case #%d: %s\n",t,s.c_str());
        }
        else
        {
            go(s,0);
            ll n;
            sscanf(s.c_str(),"%I64d",&n);
            printf("Case #%d: %I64d\n",t,n);
        }
    }
    
    
    return 0;
}























