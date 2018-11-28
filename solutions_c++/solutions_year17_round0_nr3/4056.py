#include<cstdio>
#include<queue>
using namespace std;
#define ll long long
int main() {
    freopen("F:\\Users\\zheng\\Desktop\\C-small-2-attempt0.in","r",stdin);
    freopen("F:\\Users\\zheng\\Desktop\\C.txt","w",stdout);
    int T,ca=1;scanf("%d",&T);
    while(T--)
    {
        ll n, k;
        scanf("%I64d%I64d",&n,&k);
        priority_queue<ll> pq;
        pq.push(n);
        ll r1, r2;
        while(k--)
        {
            ll t = pq.top();
            pq.pop();
            if(t%2 == 1) {
                r1 = r2 = t / 2;
                pq.push(r1);
                pq.push(r2);
            }
            else
            {
                r1 = t/2 - 1;
                r2 = t/2;
                pq.push(r1);
                pq.push(r2);
            }
        }
        printf("Case #%d: %I64d %I64d\n",ca++,r2,r1);
    }
    return 0;
}
