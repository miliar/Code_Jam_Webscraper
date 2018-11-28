#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#include<math.h>
#include<map>
#include<vector>
#include<string>
#include<set>
#include<queue>
#define MP(x,y) make_pair(x,y)
#define clr(x,y) memset(x,y,sizeof(x))
#define forn(i,n) for(int i=0;i<n;i++)
#define sqr(x) ((x)*(x))
#define MAX(a,b) if(a<b) a=b;
#define ll long long
using namespace std;

map<ll, ll> mp;
int main() {
    //freopen("in","r",stdin);
    freopen("/home/zyc/Downloads/in","r",stdin);
    freopen("/home/zyc/Downloads/out","w",stdout);
    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; cas++)
    {
        ll n, k; 
        scanf("%lld%lld", &n, &k);
        printf("Case #%d: ", cas);
        mp.clear();
        mp[n] = 1;
        while(k > 0)
        {
            map<ll, ll>::iterator it = mp.end();
            it--;
            if(it->second < k)
            {
                ll a = it->first / 2, b = (it->first - 1) / 2;
                if(a != 0) mp[a] += it->second;
                if(b != 0) mp[b] += it->second;
                mp.erase(it);
                k -= it->second;
            }
            else if(it->second >= k)
            {
                printf("%lld %lld\n", it->first / 2, (it->first - 1) / 2);
                break;
            }
        }
    }
    return 0;
}
