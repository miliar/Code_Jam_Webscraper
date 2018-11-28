#include <cstdio>
#include <cstdlib>
#include <stack>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <queue>
#define ll long long
#define N 111111
#define md 100000000
#define PI 2*acos(0.0)
using namespace std;

int t;
priority_queue<pair<ll, ll> > q;
void solve(int c, ll n, ll k){
    while(q.empty() == false) q.pop();
    q.push(pair<ll, ll> (n, 1));
    while(1){
        pair<ll, ll> qt = q.top(); q.pop();
        while(q.empty() == false && q.top().first == qt.first) qt.second += q.top().second, q.pop();
        k -= qt.second;
        if(qt.first % 2 == 1)
            q.push(pair<ll, ll> (qt.first / 2, 2 * qt.second));
        else {
            q.push(pair<ll, ll> (qt.first / 2, qt.second));
            q.push(pair<ll, ll> ((qt.first - 1) / 2, qt.second));
        }
        if(k > 0) continue;
        printf("Case #%d: %lld %lld\n", c, qt.first / 2, (qt.first - 1)/ 2);
        return;
    }
}

int main(){
    
    scanf("%d", &t);
    for(int s = 1; s <= t; s++){
        ll n, k;
        scanf("%lld%lld", &n, &k);
        solve(s, n, k);
    }
    
    return 0;
}
