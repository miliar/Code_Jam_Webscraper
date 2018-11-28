#include <algorithm>
#include <cassert>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <vector>
using namespace std;

#define FR(i,a,b) for(int i=(a);i<(b);++i)
#define FOR(i,n) FR(i,0,n)
#define CLR(x,a) memset(x,a,sizeof(x))
#define setmin(a,b) a = min(a,b)
#define PB push_back
#define FORALL(i,v) for(typeof((v).end())i=(v).begin();i!=(v).end();++i)
#define MP make_pair
#define A first
#define B second
#define RF(i,a,b) for(int i=(a)-1;i>=(b);--i)
#define BEND(v) (v).begin(),(v).end()
#define SZ(v) int((v).size())
#define FORI(i,v) FOR(i,SZ(v))
typedef long double ld;
typedef long long ll;

const int HALF = 720;
const int DAY = 2*HALF;

int A[2];
vector<pair<pair<int,int>,int>> busy;

vector<int> gaps0;
int alt;
vector<int> gaps1;
int ans;
int rem;

void calc()
{
    sort(BEND(gaps0));
    reverse(BEND(gaps0));
    while (gaps0.size()) {
        int g = gaps0.back();

        if (rem < g) {
            ans += 2 * gaps0.size();
            return;
        }
        rem -= g;
        gaps0.pop_back();
    }

    if (rem < alt) return;
    rem -= alt;

    sort(BEND(gaps1));
    while (gaps1.size()) {
        if (rem <= 0) return;

        int g = gaps1.back();

        rem -= g;
        gaps1.pop_back();
        ans += 2;
    }
}

void doit(int cas)
{
    scanf(" %d %d", &A[0], &A[1]);

    busy.clear();
    FOR(i,2) {
        FOR(j,A[i]) {
            int s,e;
            scanf(" %d %d", &s, &e);
            busy.push_back(MP(MP(s,e),i));
        }
    }
    sort(BEND(busy));

    gaps0.clear();
    alt = 0;
    gaps1.clear();

    ans = 0;
    rem = HALF; // 0's remaining baby time

    FORI(i,busy) {
        int j = (i+1) % (int)(busy.size());

        int si = busy[i].first.first;
        int ei = busy[i].first.second;
        int wi = busy[i].second;

        if (wi == 1) rem -= (ei - si);

        int sj = busy[j].first.first;
        //int ej = busy[j].first.second;
        int wj = busy[j].second;

        int gap = sj - ei;
        if (gap < 0) gap += DAY;

        //printf("  Between (%d,%d,%d) and (%d,%d,%d), gap of %d\n", si, ei, wi, sj, ej, wj, gap);

        if (wi != wj) {
            alt += gap;
            ++ans;
        } else if (wi == 0) { // && wj == 0
            gaps1.push_back(gap);
        } else { // wi == 1 && wj == 1
            gaps0.push_back(gap);
        }
    }

    calc();

    printf("Case #%d: %d\n", cas, ans);
}

int T;
int main()
{
    scanf(" %d", &T);
    assert(1 <= T && T <= 100);
    FOR(cas,T) doit(cas+1);
    return 0;
}
