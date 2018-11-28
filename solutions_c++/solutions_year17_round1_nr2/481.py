#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <numeric>
#include <complex>

using namespace std;

typedef long long ll;

#define mp make_pair
#define pb push_back
#define PI 3.1415926535897932384626433832795

#define fill(x, v)  fillchar(x, v, sizeof(x))
typedef pair<int, int>  pii;
typedef vector<int>     vi;
typedef vector< pii >   vpii;

int tc;


#define MAX_VALUE 1000500
#define MAXN 1010

struct tevent {
    int l, r, id, k;
} eo[MAXN], ec[MAXN];

bool lless(const tevent &a, const tevent &b) {
    return a.l < b.l;
}

bool rless(const tevent &a, const tevent &b) {
    return a.r < b.r;
}


set< pii > ss[MAXN];
set< pii >::iterator it;
int cnt[MAXN];
int diff;
int io, ic, k, n, p, ans;
int r[MAXN];

void add(tevent t) {
    if (cnt[t.id] == 0) {
        diff++;
    }
    cnt[t.id]++;

    ss[t.id].insert( mp(t.r, t.k) );
}

void del(tevent t) {
    it = ss[t.id].find( mp(t.r, t.k) );
    if (it == ss[t.id].end()) return;
    ss[t.id].erase(it);

    cnt[t.id]--;
    if (cnt[t.id] == 0) diff--;
}



int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    scanf("%i", &tc);
    for(int tt = 1; tt <= tc; ++tt) {
        scanf("%i%i", &n, &p);
        for(int i=0; i<n; ++i) {
            scanf("%i", &r[i]);
            ss[i].clear();
            cnt[i] = 0;
        }

        k = diff = 0;

        for(int i=0; i<n; ++i)
            for(int j=0; j<p; ++j) {
                int L, R, x;
                scanf("%i", &x);
                L = x * 10 / (11*r[i]);
                if (x *  10 % (11*r[i]) != 0) L++;

                R = x * 10 / (9 * r[i]);
                //if (x * 10 % (9 * r[i]) != 0) 

                if (L <= R) {
                    // open
                    eo[k].l = L;
                    eo[k].r = R;
                    eo[k].id = i;
                    eo[k].k = j;

                    // close
                    ec[k].l = L;
                    ec[k].r = R;
                    ec[k].id = i;
                    ec[k].k = j;

                    k++;
                }
            }

        //printf("k=%i\n", k);

        ans = 0;
        sort(eo, eo + k, lless);
        sort(ec, ec + k, rless);

        io = ic = 0;

        for(int c=1; c<=MAX_VALUE; ++c) {
            //printf("c=%i\n", c);
            while (io < k && eo[io].l == c) {
                add(eo[io++]);
                //printf("+\n");
            }
            // open

            while (diff == n) {
                ans++;
                //printf("d\n");
                for(int i=0; i<n; ++i) {
                    //printf("d1\n");
                    it = ss[i].begin();
                    cnt[i]--;
                    if (cnt[i] == 0) diff--;
                    ss[i].erase(it);
                    //printf("d2\n");
                }
            }

            while (ic < k && ec[ic].r == c) {
                del(ec[ic++]);
                //printf("-\n");
            }


            // close
        }
        printf("Case #%i: %i\n", tt, ans);
    }
    return 0;
}