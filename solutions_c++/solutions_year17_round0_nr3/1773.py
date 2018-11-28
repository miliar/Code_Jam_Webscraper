#define TXTOUT
//#define DEBUG
#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
const int M = 1e3 + 10;
typedef pair<LL, LL> pii;
pii Solve(LL n, LL k) {
    if (k == 1) {
        pii answer;
        if (n & 1) {
            answer.first = answer.second = (n - 1) / 2;
        } else {
            answer.first = n / 2;
            answer.second = answer.first - 1;
        }
        return answer;
    }
    if (k & 1) {
        if (n & 1) {
            return Solve((n - 1) / 2, (k - 1) / 2);
        } else {
            return Solve(n / 2 - 1, (k - 1) / 2);
        }
    } else {
        if (n & 1) {
            return Solve((n - 1) / 2, k / 2);
        } else {
            return Solve(n / 2, k / 2);
        }
    }
}
int main() {
    #ifdef TXTOUT
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
//    freopen("in.txt", "r", stdin);
//    freopen("out.txt", "w", stdout);
    #endif // TXTOUT
    int t;
    scanf("%d", &t);
    int cas = 1;
    while (t--) {
        LL n, k;
        scanf("%lld%lld", &n, &k);
        printf("Case #%d: ", cas++);
        pii answer = Solve(n, k);
        printf("%lld %lld\n", answer.first, answer.second);
    }
    return 0;
}

/**

4
132
1000
7
111111111111111110

*/
