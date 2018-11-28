#include <iostream>
#include <cstdio>
#include <queue>
#include <algorithm>
#include <map>

using namespace std;

pair<long long, long long> solve(priority_queue<pair<long long, long long> > & q, long long k){
    map<long long, long long> m;
    queue<long long> t;
    while (q.size()){
        pair<long long, long long> cur = q.top();
        q.pop();
        if (cur.second == 0) continue;
        long long b = cur.first >> 1;
        long long s = cur.first - b - 1;
        if (cur.second >= k){
            return make_pair(b, s);
        } else {
            k -= cur.second;
        }
        t.push(b);
        t.push(s);
        m[b] += cur.second;
        m[s] += cur.second;
    }

    while(t.size()){
        long long c = t.front();
        t.pop();
        q.push(make_pair(c, m[c]));
        m[c] = 0;
    }
    return solve(q, k);
}

int main(){
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t){
        long long n, k;
        scanf("%lld%lld", &n, &k);
        priority_queue<pair<long long, long long> > q;
        q.push(make_pair(n, 1));
        pair<long long, long long> ans = solve(q, k);
        printf("Case #%d: %lld %lld\n", t, ans.first, ans.second);
    }
    return 0;
}
