#include <bits/stdc++.h>
#define ii pair<int, int>
#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define vi vector<int>
#define vii vector< pair<int, int> >
typedef long long ll;
using namespace std;
set<ll> inQ;
map<ll, ll> f;
int main()
{
    int tt;
    scanf("%d", &tt);
    for(int qq = 1; qq<= tt; qq++)
    {
        double clock_start = clock();
        inQ.clear();
        f.clear();
        ll n, k;
        scanf("%lld %lld", &n, &k);
        queue<ll> Q;
        Q.push(n);
        f[n] = 1;
        while(!Q.empty())
        {
            ll x = Q.front(); Q.pop();
            inQ.erase(x);
            ll a1 = (x-1)/2, a2 = x/2;
            if(a1) f[a1] += f[x];
            if(a2) f[a2] += f[x];
            if(a1 && inQ.find(a1) == inQ.end())
            {
                inQ.insert(a1);
                Q.push(a1);
            }
            if(a2 && inQ.find(a2) == inQ.end())
            {
                inQ.insert(a2);
                Q.push(a2);
            }
        }
        ll sum = 0;
        ll res = 0;
        for(auto it = f.rbegin(); it != f.rend(); it++)
        {
            sum += it->Y;
            if(sum>= k)
            {
                res = it->X;
                break;
            }
        }
        printf("Case #%d: ", qq);
        ll a1 = (res-1)/2, a2 = res/2;
        printf("%lld %lld\n", a2, a1);
        fprintf(stderr, "Test %d solved in %.2lf s.\n", qq, (clock()-clock_start)/CLOCKS_PER_SEC);
    }
	return 0;
}
