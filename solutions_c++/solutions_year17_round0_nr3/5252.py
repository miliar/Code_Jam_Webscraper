#include <cstdio>
#include <cstring>
#include <queue>

int main() {
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; i++) {
        
        long long n, k;

        scanf("%lld", &n);
        scanf("%lld", &k);

        std::priority_queue <long long> q;

        q.push(n);

        long long ma, mi, cnt = 0, temp;

        while (cnt < k && !q.empty()) {
            temp = q.top();
            q.pop();
            if (temp%2 == 0) {
                ma = temp/2;
                mi = ma - 1;
            }
            else
                ma = mi = (temp-1)/2;
            if (ma != 0)
                q.push(ma);
            if (mi != 0)
                q.push(mi);
            cnt++;
        }

        printf("Case #%d: ", i);
        
        printf("%lld %lld\n", ma, mi);
    }   
    return 0;
}