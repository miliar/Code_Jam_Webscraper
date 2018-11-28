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

char buf[42];

int main() {
    lli cases;
    scanf("%lld\n", &cases);

    FOR(__i, cases) {
        //read
        scanf("%s", buf);
        lli n = strlen(buf);
        FOR(i, n) buf[i] -= '0';
        //solve
        lli res = 0;
        FOR(i, n+1) {
            lli cur = 0;
            if(i < n && buf[i] == 0) goto bigContinue;
            FOR(j, i) {
                if(j != 0 && buf[j] < buf[j-1]) goto bigContinue;
                cur = 10*cur+buf[j];
            }
            if(i < n) {
                if(i != 0 && buf[i]-1 < buf[i-1]) goto bigContinue;
                cur = 10*cur+buf[i]-1;
            }
            FOR(j, n-i-1) cur = 10*cur+9;
            res = max(res, cur);
bigContinue:
            (void)res; //ugly ugly
        }

        printf("Case #%lld: ", __i + 1);
        //print
        printf("%lld\n", res);
    }

	return 0;
}
