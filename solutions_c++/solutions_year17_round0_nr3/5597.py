#include <iostream>
#include <cstdio>
using namespace std;

typedef unsigned long long llu;
typedef pair<llu, llu> P;

int T;
llu N, K;
P ans;

P minLR(llu n, llu k) {
    //cout << "minLR: " << n << " " << k << endl;
    if (n < k || k <= 0 || n <= 0) return make_pair(0, 0);
    if (k == 1) {
        llu mlr = (n+1)/2 - 1;
        llu Mlr = n - 1 - mlr;
        return make_pair(Mlr, mlr);
    }
    else if (n == k) return make_pair(0, 0);
    else {
        P tmp = max(minLR(n/2, k-k/2), minLR(n-n/2-1, k/2));
        //cout << tmp.first << " " << tmp.second << endl;
        return tmp;
    }
}

int main() {
    scanf("%d", &T);
    for (int i = 1; i <= T; i++) {
        scanf("%llu%llu", &N, &K);
        ans = minLR(N, K);
        printf("Case #%d: ", i);
        printf("%llu %llu\n", ans.first, ans.second);
    }
    return 0;
}
