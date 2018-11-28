#include<algorithm>
#include<cstdio>
#include<sstream>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<iostream>
#include<fstream>
#include<numeric>
#include<string>
#include<vector>
#include<cstring>
#include<map>
#include<iterator>
#include<deque>
#include<climits>
#include<complex>
#include<string.h>


using namespace std;
//-------------------------------------

#define ll long long
#define ull unsigned long long
#define sc(x) scanf("%lld",&x)
#define sc2(x,y) scanf("%lld%lld",&x,&y)
#define sci(x) scanf("%d",&x)
#define sci2(x,y) scanf("%d%d",&x,&y)

#define rep(i,a,n) for(int i=a;i<n;i++)
#define F(i,n) for(int i=0;i<n;i++)
#define mem(x) memset(x,0,sizeof x)
#define all(x) x.begin(),x.end()
#define xx first
#define yy second
#define inf 99999999999999999
#define mkp(x,y) make_pair(x,y)
#define pii pair<ll,ll>
#define pb(x)  push_back(x);
#define uni(vc) vc.resize(unique(all(vc))-vc.begin())
#define db(x) cout<<#x<<" "<<x<<endl;
#define ml(inp) sizeof(inp)/1e6

//---------------------------------------9 12 13 14 15 21 22

#define MX 200007

#define pi 2*acos(0.00)

#define open       freopen("input.txt","r",stdin)
#define close       freopen("B_output.txt","w",stdout)


int main()
{

    ll l, u, v, w, x, y, z, a, b, c, d, e, f, t = 1, tc;
    ll flg, sz, cnt, gt, ans, mx, mn;
    ll m, k, n,i,j;
    ll low, hi, md, inp[MX], sm, ff;
    open;
    close;
    sc(tc);
    while(tc--)
    {
        sc(n);
        z = n;
        vector<int> tk;
        while(z)
        {
            tk.pb(z%10);
            z/=10;
        }
        reverse(all(tk));
        sz = tk.size();
        flg = 1;
        for(i=1; i<sz; i++)
        {
            if(tk[i]>=tk[i-1]);
            else flg = 0;
        }
        if(flg)
        {
            printf("Case #%lld: %lld\n",t++,n);
            continue;
        }
        a = -inf;
        u = 0;
        ans = -inf;
        for(i=0; i<sz; i++)
        {
            b = tk[i];
            ll nbr = u;
            if(b>=a)
            {
                if(b>a) nbr = nbr*10 +max(b-1,0ll);
                if(b==a) nbr = nbr*10 +max(b,0ll);
                for(int j=i+1; j<sz; j++) nbr = nbr*10+9;
                a=b;

            }
            else break;
            u = u*10+tk[i];
            if(nbr<=n) ans = max(ans,nbr);
        }
        printf("Case #%lld: %lld\n",t++,ans);



    }




    return 0;

}


/*
000


*/








