#include <bits/stdc++.h>
using namespace std;

#define LL long long
#define NL '\n'
#define xx first
#define yy second
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define si(x) scanf("%d",&x)
#define sl(x) scanf("%I64d",&x)
#define sd(x) scanf("%lf",&x)
#define ss(x) scanf("%s",x)
#define mem(a,b) memset(a,b,sizeof(a))
#define FOR(i,j,k) for(i=j;i<=k;i++)
#define REV(i,j,k) for(i=j;i>=k;i--)
#define READ(f) freopen(f,"r",stdin)
#define WRITE(f) freopen(f,"w",stdout)
#define cnd tree[idx]
#define lnd tree[idx*2]
#define rnd tree[(idx*2)+1]
#define lndp (idx*2),(b),((b+e)/2)
#define rndp (idx*2+1),((b+e)/2+1),(e)
#define pi 2.0*acos(0.0)
#define MOD 1000000007
#define MAX 1005

set <LL> s;
set <LL>::iterator it;
map <LL, LL> m;
map <LL, LL>::iterator mt;

int main()
{
    //READ("C-large.in");
    //WRITE("C-large.out");
    std::ios_base::sync_with_stdio(0);
    int cases, caseno=0;
    LL n, i, j, k, mx, mn, l, r, x;

    cin >> cases;

    while(cases--)
    {
        cin >> n >> k;

        s.clear();
        m.clear();

        s.insert(n);
        m[n] = 1;

        while(!s.empty())
        {
            it = s.end();
            it--;
            x = *it;
            s.erase(it);
            x--;
            l = x/2LL;
            r = x-l;
            x = m[x+1];
            if(l > 0 && m.find(l) == m.end()) m[l] = x;
            else if(l > 0) m[l] += x;
            if(r > 0 && m.find(r) == m.end()) m[r] = x;
            else if(r > 0) m[r] += x;
            if(l > 0) s.insert(l);
            if(r > 0) s.insert(r);
        }

        mt = m.end();
        mt--;

        while(1)
        {
            if(k <= (mt->yy))
            {
                mn = ((mt->xx) - 1)/2LL;
                mx = ((mt->xx) - 1)-mn;
                break;
            }
            k -= (mt->yy);
            if(mt == m.begin()) break;
            mt--;
        }

        cout << "Case #" << ++caseno << ": " << mx << " " << mn << NL;
    }

    return 0;
}


