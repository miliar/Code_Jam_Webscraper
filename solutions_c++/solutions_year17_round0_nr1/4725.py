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

#define MX 10007

#define pi 2*acos(0.00)

#define open       freopen("input.txt","r",stdin)
#define close       freopen("output.txt","w",stdout)

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

        string st;
        mem(inp);
        cin >> st;
        sc(n);
        sz = st.size();
        rep(i,0,sz)
        {
            if(st[i]=='+') inp[i]=1;
        }
        cnt = 0;
        rep(i,0,sz-n+1)
        {
            if(!inp[i])
            {
                rep(j,i,i+n) inp[j]^=1;
                cnt++;
            }
        }
        ans = 1;

        rep(i,0,sz)
        {

            if(!inp[i]) ans = 0;
        }

        printf("Case #%lld: ",t++);
        if(ans) printf("%lld\n",cnt);
        else printf("IMPOSSIBLE\n");
    }




    return 0;

}


/*



*/









