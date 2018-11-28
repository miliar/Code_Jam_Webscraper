#include <bits/stdc++.h>

#define FOR(i, n) for(lli i = 0; i < (lli)(n); ++i)

#define X(A) get<0>(A)
#define Y(A) get<1>(A)
#define Z(A) get<2>(A)
#define W(A) get<3>(A)

#define mt make_tuple
#define pb push_back

using namespace std;
using lli = long long int;

using pii   = tuple<lli, lli>;
using piii  = tuple<lli, lli, lli>;
using vi    = vector<lli>;
using vii   = vector<pii>;
using viii  = vector<piii>;
using vvi   = vector<vi>;
using vvii  = vector<vii>;
using vviii = vector<viii>;
using vb    = vector<bool>;
using vvb   = vector<vb>;

using namespace std;

char buf[1000+42];

int main() {
    lli cases;
    scanf("%lld\n", &cases);

    FOR(__i, cases) {
        //read
        lli k;
        scanf("%s%lld", buf, &k);
        //solve
        lli n = strlen(buf);
        lli res = 0;
        FOR(i, n-k+1) {
            if(buf[i] == '-') {
                res += 1;
                FOR(j, k) {
                    if(buf[i+j] == '-') buf[i+j] = '+';
                    else buf[i+j] = '-';
                }
            }
        }

        bool imp = false;
        FOR(i, k) {
            if(buf[n-i-1] == '-') imp = true;
        }

        printf("Case #%lld: ", __i + 1);
        //print
        if(imp) printf("IMPOSSIBLE\n");
        else printf("%lld\n", res);
    }

	return 0;
}
