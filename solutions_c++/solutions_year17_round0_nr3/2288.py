#include <bits/stdc++.h>
#define INF 1000000009
#define mod 1000000007
#define PI 3.14159
#define vi vector<int>
#define ll long long
#define ii pair<int, int>
#define pll pair<ll, ll>
#define vii vector<ii>
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define mt make_tuple
#define eb emplace_back
#define CLR(arr) memset(arr, 0, sizeof(arr))
#define FAST_IO ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0)
using namespace std;

inline ll isodd(ll N)
{
    return N&0x1 ? 1 : 0;
}

int main()
{
    int T;
    cin>>T;
    for(int ctr=1; ctr<=T; ++ctr)
    {
        ll N, K;
        cin>>N>>K;
        ll lo=0, hi=0;
        ll o1, e1, o2, e2;
        if(isodd(N))
        {
            N>>=1;
            o1 = 2*isodd(N);
            e1 = 2 - o1;
        }
        else
        {
            N>>=1;
            N -= 1;
            o1 = e1 = 1;
        }
        o2 = e2 = 0;
        ll occupied = 0;

        for(ll lvl=0; occupied+(1LL<<lvl)<K; ++lvl)
        {
            occupied += 1LL<<lvl;
            if(isodd(N))
            {
                N>>=1;
                if(isodd(N))
                {
                    o2 = 2*o1 + e1;
                    e2 = e1;
                }
                else
                {
                    e2 = 2*o1 + e1;
                    o2 = e1;
                }
            }
            else
            {
                N>>=1;
                N -= 1;
                if(isodd(N))
                {
                    e2 = 2*o1 + e1;
                    o2 = e1;
                }
                else
                {
                    o2 = 2*o1 + e1;
                    e2 = e1;
                }
            }
            o1 = o2;
            e1 = e2;
        }

        K -= occupied;
        ll ch, cl, Nh, Nl;
        Nl = N;
        Nh = N+1;
        if(isodd(N))
        {
            cl = o1;
            ch = e1;
        }
        else
        {
            cl = e1;
            ch = o1;
        }
        if(ch>=cl)
        {
            if(K<=(ch-cl)/2)
                lo = hi = Nh;
            else
            {
                lo = Nl;
                hi = Nh;
            }
        }
        else
        {
            if(K<=ch)
            {
                lo = Nl;
                hi = Nh;
            }
            else
                lo = hi = Nl;
        }

        cout<<"Case #"<<ctr<<": "<<hi<<" "<<lo<<endl;

    }
    return 0;
}
