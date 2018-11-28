#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<queue>
#include<map>
using namespace std;
typedef long long ll;
typedef pair<ll, ll> PAIR;

PAIR divide(ll n){
    return PAIR((n + 1) / 2, n / 2);
}

PAIR solve(ll n, ll k)
{
    int cnt = 0;
    queue<ll> q;
    map<ll, ll> Map;
    q.push(n);
    Map[n] = 1;
    while(!q.empty()){
        ll now = q.front();
        cnt ++;
        q.pop();
        ll num = Map[now];
        if(k <= num)
            return divide(now - 1);
        k -= num;
        PAIR next = divide(now - 1);
        if(next.first > 0)
        {
            if(Map.find(next.first) != Map.end())
                Map[next.first] += Map[now];
            else{
                Map[next.first] = Map[now];
                q.push(next.first);
            }
        }
        if(next.second > 0)
        {
            if(Map.find(next.second) != Map.end())
                Map[next.second] += Map[now];
            else{
                Map[next.second] = Map[now];
                q.push(next.second);
            }
        }
    }
}

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int cnt;
    ll k, n;
    scanf("%d", &cnt);
    for(int c = 1; c <= cnt; ++c)
    {
        scanf("%lld %lld", &n, &k);
        PAIR rst = solve(n, k);
        printf("Case #%d: %lld %lld\n", c, rst.first, rst.second);
    }
    return 0;
}
