#include <set>
#include <cmath>
#include <queue>
#include <cstdio>
#include <vector>
#include <cassert>
#include <algorithm>
using namespace std;

int fdif(double lf) {
    if( fabs(lf) < 1e-6 ) return 0;
    return lf < 0 ? -1 : 1;
}

struct Event {
    int x, l, r, v, type;
};

int N, P;
vector<int> R;
vector< vector<int> > Q;

int solve() {
    vector<Event> es;
    for(int i=0; i<N; ++i)
        for(int j=0; j<P; ++j) {
            int low_bound = -1, up_bound = -1;
            for(int k=1; fdif(0.9 * R[i] * k - Q[i][j]) <= 0; ++k)
                if( fdif(Q[i][j] - 1.1 * R[i] * k) <= 0 ) {
                    if( low_bound == -1 )
                        low_bound = up_bound = k;
                    else
                        up_bound = k;
                }
            if( low_bound == -1 )
                continue;
            es.push_back({low_bound, low_bound, up_bound, i, 0});
            es.push_back({up_bound+1, low_bound, up_bound, i, 1});
        }
    sort(es.begin(), es.end(), [](Event &l, Event &r) {
        return l.x < r.x || (l.x == r.x && l.type > r.type)
                || (l.x == r.x && l.type == r.type && l.r < r.r);
    });
    int total = 0;
    vector< multiset<pair<int,int>> > cnt(N);
    for(auto e : es) {
        if( e.type == 0 ) {
            cnt[e.v].insert(make_pair(e.l, e.r));

            bool ok = true;
            for(int i=0; i<N; ++i)
                if( cnt[i].size() == 0 ) {
                    ok = false;
                    break;
                }
            if( ok ) {
                total++;
                for(int i=0; i<N; ++i)
                    cnt[i].erase(cnt[i].begin());
            }
        }
        else {
            auto it = cnt[e.v].find(make_pair(e.l, e.r));
            if( it != cnt[e.v].end() )
                cnt[e.v].erase(it);
        }
    }
    return total;
}


int main() {
    int T;
    scanf("%d", &T);
    for(int NCASE=1; NCASE<=T; ++NCASE) {
        scanf("%d%d", &N, &P);
        R = vector<int>(N, 0);
        Q = vector< vector<int> >(N, vector<int>(P));
        for(int i=0; i<N; ++i)
            scanf("%d", &R[i]);
        for(int i=0; i<N; ++i)
            for(int j=0; j<P; ++j)
                scanf("%d", &Q[i][j]);
        printf("Case #%d: %d\n", NCASE, solve());
    }
    return 0;
}
