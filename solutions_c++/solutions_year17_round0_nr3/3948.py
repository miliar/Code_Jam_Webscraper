#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

char s[1005];

int main() {
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cs = 1; cs <= T; cs++) {
        ll n, k;
        scanf("%I64d%I64d",&n,&k);
        priority_queue<ll> pq;
        pq.push(n);
        ll r1, r2;
        while(k--) {
            ll t = pq.top();
            pq.pop();
            if(t%2 == 1) {
                r1 = r2 = t / 2;
                pq.push(r1);
                pq.push(r2);
            }
            else {
                r1 = t/2 - 1;
                r2 = t/2;
                pq.push(r1);
                pq.push(r2);
            }
        }
        printf("Case #%d: ",cs);
        printf("%I64d %I64d\n",r2,r1);
    }

}