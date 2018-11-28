#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int T;
int n, k;
struct p{
    ll r, h;
};
bool cmp(p x, p y) {
    return x.r<y.r;
}
vector<p> v;
priority_queue<ll> pq;
queue<ll> temp;

ll bot(int idx) {
    ll ret = v[idx].r*v[idx].r;
    ret += 2*v[idx].r*v[idx].h;
        
    for(int i=0;i<k-1;i++) {
        ll u = pq.top();
        ret += u*2;
        temp.push(u); pq.pop();
    }

    while(!temp.empty()) {
        pq.push(temp.front());
        temp.pop();
    }
    return ret;
}

double solve() {
    sort(v.begin(), v.end(), cmp);
    while(!pq.empty()) pq.pop();

    for(int i=0;i<k-1;i++) {
        pq.push(v[i].r*v[i].h);
    }
    
    long long ans = 0;
    for(int i=k-1;i<n;i++) {
        ans = max(ans, bot(i));
        pq.push(v[i].r*v[i].h);
    }
    
    return 3.1415926535*ans;
}

int main() {
    scanf("%d", &T);
    for(int t=1;t<=T;t++) {
        scanf("%d %d", &n, &k);
        v.assign(n, p());
        for(int i=0;i<n;i++) {
            scanf("%lld %lld", &v[i].r, &v[i].h);
        }

        printf("Case #%d: %.10f\n", t, solve());
    }

}
