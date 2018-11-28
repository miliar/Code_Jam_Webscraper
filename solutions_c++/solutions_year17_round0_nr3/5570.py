#include <stdio.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;
typedef long long ll;

struct stInterval {
    ll start;
    ll end;
    ll length;

    stInterval(ll s, ll e) {
        start = s; end = e; length = end - start;
    }
};

bool operator<(const stInterval& lhs, const stInterval& rhs) {
    if (lhs.length == rhs.length)
        return lhs.start > rhs.start;

    return lhs.length < rhs.length;
}

priority_queue<stInterval> pq;

int main(int argc, char **argv)
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
   
    int T;
    scanf("%d", &T);

    for (int test = 1; test <= T; test++) {
        printf("Case #%d: ", test);
        ll N,K; 
        scanf("%I64d %I64d", &N, &K);

        pq = priority_queue<stInterval>();

        pq.push(stInterval(-1,N));

        while(K-- > 1) {
            stInterval inv = pq.top();
            pq.pop();

            ll mid = (inv.start + inv.end) / 2;
            pq.push(stInterval(inv.start, mid));
            pq.push(stInterval(mid, inv.end));
        }

        stInterval inv = pq.top();
        ll mid = (inv.start + inv.end) / 2;

        ll ls = mid - inv.start -1 ;
        ll rs = inv.end - mid - 1;

        printf("%I64d %I64d", max(ls,rs), min(ls,rs));
        printf("\n");
    }

	return 0;
}
