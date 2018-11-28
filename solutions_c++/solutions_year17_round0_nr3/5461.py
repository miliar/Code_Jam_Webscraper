#include <cstdio>
#include <queue>
using namespace std;
int q;
void fileIO() {
    freopen("C-small-1-attempt0.in", "r", stdin);
    freopen("C-small-1-attempt0.out", "w", stdout);
}
void solve(int t) {
    priority_queue<int> hp;
    int n, k;
    scanf("%d %d", &n, &k);
    hp.push(n);
    while(--k) {
        n = hp.top();
        hp.pop();
        hp.push( (n-1)/2 );
        hp.push( n/2 );
    }
    n = hp.top();
    printf("Case #%d: %d %d\n", t, n/2, (n-1)/2);
}
int main() {
    fileIO();
    scanf("%d", &q);
    for(int i = 1; i <= q; i++)
        solve(i);
    return 0;
}
