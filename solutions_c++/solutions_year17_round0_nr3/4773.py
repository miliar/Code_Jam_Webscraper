#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

const int INF = 1000000000;
// double EPS = 1e-12;
const int MOD = 1000000007;

priority_queue<int> pq;

int main() {
    freopen("C-small-2-attempt0.in", "r", stdin);
    freopen("C-small-2-attempt0.out", "w", stdout);
    int t, k;
    int n;
    char str[1010];
    scanf("%d", &t);
    for (int tt=0 ; tt<t ; tt++) {
        scanf("%d%d", &n, &k);

        while(!pq.empty()) pq.pop();
        pq.push(n);
        for (int i=1; i<k ; i++) {
            int t = pq.top();
            pq.pop();
            if (t%2 == 0) {
                pq.push(t/2);
                pq.push(t/2-1);
            }
            else {
                pq.push(t/2);
                pq.push(t/2);
            }
        }
        int t = pq.top();
        pq.pop();
        if (t%2 == 0) {
            printf("Case #%d: %d %d\n", tt+1, t/2, t/2-1);
        }
        else {
            printf("Case #%d: %d %d\n", tt+1, t/2, t/2);
        }
    }
}
