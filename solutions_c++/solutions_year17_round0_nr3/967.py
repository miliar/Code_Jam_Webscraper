#include <bits/stdc++.h>

using namespace std;

long long t,x,n,k,tes;
map<long long, long long> mem;
priority_queue<long long> pq;

int main() {
    scanf("%lld",&t);
    for (tes=1 ; tes<=t ; tes++) {
        scanf("%lld%lld",&n,&k);
        printf("Case #%lld: ",tes);
        
        mem.clear();
        while (!pq.empty()) pq.pop();
        
        mem[n] = 1;
        pq.push(n);
        
        x = pq.top();
        pq.pop();
        while (k - mem[x] > 0) {
            k -= mem[x];
            
            if (x % 2 == 1) {
                if (mem[x / 2] == 0) pq.push(x / 2);
                mem[x / 2] += mem[x];
                mem[x / 2] += mem[x];
            } else {
                if (mem[x / 2] == 0) pq.push(x / 2);
                if (mem[x / 2 - 1] == 0) pq.push(x / 2 - 1);
                mem[x / 2] += mem[x];
                mem[x / 2 - 1] += mem[x];
            }
            
            x = pq.top();
            pq.pop();
        }
        
        printf("%lld %lld\n",x / 2,(x - 1) / 2);
    }
}

