#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

ll bla(int d, int k)
{
    ll res=0;
    for(int i=0; i<k; i++)
    {
        res=res*10LL+d;
    }
    return res;
}

int digs(ll A)
{
    int res=0;
    while(A>0)
    {
        A/=10;
        res++;
    }
    return res;
}

ll pow10(int p)
{
    ll res=1LL;
    for(int i=0; i<p; i++) res*=10LL;
    return res;
}

ll solve2(ll N, int k, int from)
{
    //int k=digs(N);
    if(k==1) return min(N, 9LL);

    //ll res=bla(9, k-1);
    for(int d=9; d>=from; d--)
    {
        if(N>=bla(d, k))
        {
            ll wat=d*pow10(k-1);
            //cout << N << ' ' << k << ' ' << d << ' ' << wat << endl;

            return wat+solve2(N-wat, k-1, d);
        }
    }

    return bla(9, k-1);
}

ll solve(ll N)
{
    int k=digs(N);
    return solve2(N, k, 1);
}

int main()
{
    //cout << solve(213);
    //
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    for(int t=1; t<=T; t++)
    {
        ll N;
        cin >> N;
        ll result=solve(N);
        cout << "Case #" << t << ": " << result << endl;
    }
    //*/
    return 0;
}
