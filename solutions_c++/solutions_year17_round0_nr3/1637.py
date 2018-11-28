#include <bits/stdc++.h>

using namespace std;

#define mem(a,b) memset(a,b,sizeof(a))
#define FOR(i,j,k) for(int i=j;i<=k;i++)
#define REV(i,j,k) for(int i=j;i>=k;i--)
#define FORR(i,j,k,l) for(int i=j;i<=k;i+=l)
#define inf         freopen("in.txt", "r", stdin)
#define outf        freopen("out.txt", "w", stdout)
#define pf          printf
#define sf(n)       scanf("%d", &n)
#define sff(a,b)    scanf("%d %d", &a, &b)
#define sfff(a,b,c)    scanf("%d %d %d", &a, &b, &c)
#define minn          (long long)-1000000000000000000
#define maxx          (long long) 1000000000000000000
#define mod          1000000007
#define LL           long long
#define NL '\n'
#define cnd tree[idx]
#define lnd (2*idx)
#define rnd ((2*idx)+1)
#define PB push_back
#define F first
#define S second
#define MK make_pair
typedef pair<LL,LL> pr;

class Compare
{
public:
    bool operator()(LL x,LL y)
    {
        return x>y;
    }
};
pr ar[1000010];
int main()
{
    ios::sync_with_stdio(false);
    inf;
    outf;
    int tc;
    cin>>tc;
    FOR(tt,1,tc)
    {
        set<LL,Compare> ms;
        set<LL>::iterator it;
        map<LL,LL> mp;
        map<LL,LL>::iterator ii;
        pr na;
        LL i,j,x,y,n,m,a,b,c,d;
        cin>>n>>m;
        ms.insert(n); mp[n]=1;
        while(!ms.empty())
        {
           it=ms.begin(); ms.erase(ms.begin());
           x=*it; a=mp[x];
           b=x/2;
           if(b==0) continue;
           mp[b]+=a;
           ms.insert(b);
           if(x%2==0) b--;
           if(b==0) continue;
           mp[b]+=a;
           ms.insert(b);
        }
        c=mp.size()-1;
        for(ii=mp.begin();ii!=mp.end();ii++)
        {
            ar[c].F=ii->F; ar[c].S=ii->S;
            c--;
        }
        c=mp.size()-1; x=0;
        i=0;
        while(true)
        {
            x+=ar[i].S;
            if(x>=m)
            {
                a=ar[i].F;
                if(a==1) x=0,y=0;
                else if(a%2)
                {
                    x=a/2; y=a/2;
                }
                else
                {
                    x=a/2; y=a/2; y--;
                }
                cout<<"Case #"<<tt<<": "<<max(x,y)<<' '<<min(x,y)<<NL;
                break;
            }
            i++;
        }
    }
    return 0;
}

