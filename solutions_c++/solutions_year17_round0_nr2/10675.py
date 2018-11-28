#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iterator>
#include <map>
#include <string>
#include <cstdio>
#include <sstream>
#include <utility>

using namespace std;

#define lld long long int
#define REP(i,n) for (lld i = 0; i < (lld)n; i++)
#define REPD(i,n) for (lld i = (lld)n; i >= 0; i--)
#define FOR(i,a,b) for (lld i = (lld)a; i <= (lld)b; i++)
#define FORD(i,a,b) for (lld i = (lld)b; i >= (lld)a; i--)
#define PB(x) push_back(x)
#define MP(x,y) make_pair(x,y)
#define RESET(a,x) memset(a,x,sizeof(a))
#define EXIST(a,s) ((s).find(a) != (s).end())
#define MX(a,b) a = max((a),(b));
#define MN(a,b) a = min((a),(b));
#define VC(a) vector< a >
#define PR(a,b) pair<a, b>
#define sc second
#define ft first

vector< pair<string, lld> > all;

bool isTidy(lld n) {
    string d=to_string(n);
    REP(i,d.length()-1)
        if ((lld)d[i] > (lld)d[i+1]) return false;
    return true;
}

void solve(lld idx, lld n) {
    lld ans;

    if (n<10||isTidy(n)) ans=n;
    else {
        REPD(i,n-1) {
            if (isTidy(i)) {
                ans=i;
                break;
            }
        }
    }

    printf("Case #%lld: %lld\n", idx+1, ans);
}

int main(int argc, char *argv[]) {
    lld N, inp;

    scanf("%lld", &N);

    REP(i,N) {
        scanf("%lld", &inp);
        solve(i, inp);
    }
}
