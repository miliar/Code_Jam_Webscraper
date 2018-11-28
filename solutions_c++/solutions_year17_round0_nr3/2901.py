#include <cstdio>
#include <queue>
#include <map>
using namespace std;
using ll = long long;

void prog() {
    ll n, k;
    scanf("%lld%lld", &n, &k);
    k--;
    priority_queue<ll>q;
    map<ll, ll> x;
    q.push(n);
    x[n] = 1;
    while(1) {
        ll v = q.top();
        q.pop();
        if(x.find(v) != x.end()) {
            if(x[v] > k) {
                printf("%lld %lld\n", v / 2, (v - 1) / 2);
                return;
            }
            k -= x[v];
            x[v / 2] += x[v];
            x[(v - 1) / 2] += x[v];
            q.push(v / 2);
            q.push((v - 1) / 2);
            x.erase(v);
        }
    }
}

int main() {
    int t; scanf("%d", &t);
    for(int i = 1; i <= t; ++i) {
        printf("Case #%d: ", i);
        prog();
    }
}
