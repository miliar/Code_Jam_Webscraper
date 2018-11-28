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

int main() {
    lli cases;
    scanf("%lld\n", &cases);

    FOR(__i, cases) {
        printf("Case #%lld: ", __i + 1);
        lli d, n;
        scanf("%lld%lld", &d, &n);
        vi k(n), s(n);
        FOR(i, n) scanf("%lld%lld", &k[i], &s[i]);
        double lastTime = 0;
        FOR(i, n) lastTime = max(lastTime, (d - k[i])/((double)s[i]));
        printf("%lf\n", d/lastTime);
    }

	return 0;
}
