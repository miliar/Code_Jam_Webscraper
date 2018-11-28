#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;
typedef vector<int> vi;
#define REP(i, a, b) for(int i = a; i < b; ++i)

int main() {
    int TC; cin >> TC; ++TC;
    REP(tc, 1, TC) {
        int N, K;
        cin >> N >> K;
        priority_queue<int> pq;
        pq.push(N);
        int t = pq.top();
        REP(k, 0, K) {
            t = pq.top(); pq.pop();
            if (t % 2)
                pq.push(t/2), pq.push(t/2);
            else
                pq.push(t/2-1), pq.push(t/2);
        }
        if (t % 2)
            printf("Case #%d: %d %d\n", tc, t/2, t/2); 
        else
            printf("Case #%d: %d %d\n", tc, t/2, t/2-1); 
    }
    return 0;
}
