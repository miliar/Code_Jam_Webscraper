#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll, ll> pi;
#define mp make_pair    
const int MAXN = 1000050;
int TC;
ll N, K;
priority_queue<ll> pq;
map<ll, ll> m;
void add(ll x, ll c) {
    if (m.find(x) == m.end()) pq.push(x);
    m[x] += c;
}
int main() {
    scanf("%d", &TC);
    for (int Txn = 1; Txn <= TC; ++Txn) {
        printf("Case #%d: ", Txn);
        scanf("%lld%lld", &N, &K);
        add(N, 1);
        while (!pq.empty() && K > 0) {
            ll x = pq.top();
            pq.pop();
            ll c = m[x--];
            if (c >= K) {
                printf("%lld %lld\n", x-x/2, x/2);
                break;
            }
            else K -= c;
           add(x/2, c);
           add(x-x/2, c);
        }
        while (!pq.empty()) pq.pop();
        m.clear();
    }
}