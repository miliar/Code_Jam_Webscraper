#include <cstdio>
#include <queue>
#include <string>
#include <cstring>
#include <cmath>
#include <set>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair<int, int> P;

int T = 0, K = 0;
ll N = 0L;

ll calc() {
    priority_queue<ll> que;
    que.push(N);
    
    while (K > 1) {
        ll curr = que.top(); que.pop();
        
        if (curr > 1) {
            que.push(curr / 2);
            que.push((curr / 2) - (1 - curr % 2));
        }
        K--;
    }
    
    return que.top();
}

int main() {
    freopen("1C_small.in", "r", stdin);
    cin >> T;
    
    for (int t = 1; t <= T; t++) {
        cin >> N >> K;
        ll lastRange = calc();
        
        ll large = lastRange / 2;
        ll small = (lastRange / 2) - (1 - lastRange % 2);
        printf("Case #%d: %lld %lld\n", t, large, small);
    }
    
    return 0;
}
