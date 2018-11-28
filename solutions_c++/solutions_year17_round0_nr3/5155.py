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

struct Seg {
    Seg(lli b, lli e) : beg(b), end(e) {}
    lli beg;
    lli end;
    bool operator<(const Seg& oth) const {
        lli sz = end-beg;
        lli othsz = oth.end - oth.beg;
        if(sz < othsz) return true;
        if(sz == othsz && beg < oth.beg) return true;
        return false;
    }
};

int main() {
    lli cases;
    scanf("%lld\n", &cases);

    FOR(__i, cases) {
        //read
        lli n, k;
        scanf("%lld%lld", &n, &k);
        //solve
        priority_queue<Seg> segs;
        segs.push(Seg(0, n+1));
        lli mini = 0;
        lli maxi = 0;
        FOR(i, k) {
            Seg s = segs.top(); segs.pop();
            lli p = (s.beg + s.end)/2;
            //printf("p:%lld beg:%lld end:%lld\n", p, s.beg, s.end);
            segs.push(Seg(s.beg, p));
            segs.push(Seg(p, s.end));
            mini = min(p-s.beg-1, s.end-p-1);
            maxi = max(p-s.beg-1, s.end-p-1);
        }

        printf("Case #%lld: ", __i + 1);
        //print
        printf("%lld %lld\n", maxi, mini);
    }

	return 0;
}

