#include <iostream>
#include <cstdio>
#include <queue>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> pr;
#define x first
#define y second

priority_queue<pr> pri;

int main()
{
    freopen("C-large.in.txt", "r", stdin);
    freopen("C-large.out.txt", "w", stdout);

    int T;
    scanf("%d", &T);

    for (int Ti = 1; Ti <= T; Ti++) {
        ll N, K;
        scanf("%lld %lld", &N, &K);

        ll cnt = 0;
        priority_queue<pr>().swap(pri);
        pri.push(pr(N, 1));

        ll ans = -1;

        while ( cnt < K ) {
            pr top = pri.top();
            pri.pop();

            while ( !pri.empty() && pri.top().x == top.x )
                top.y += pri.top().y, pri.pop();

            ans = top.x;
            cnt += top.y;
            pri.push(pr((top.x-1)/2, top.y) );
            pri.push(pr(top.x/2, top.y) );
        }

        printf("Case #%d: %lld %lld\n", Ti, ans/2, (ans-1)/2);
    }
}
