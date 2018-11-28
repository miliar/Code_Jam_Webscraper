#include <functional>
#include <algorithm>
#include <stdexcept>
#include <iostream>
#include <sstream>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <utility>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cctype>
#include <cstdio>
#include <vector>
#include <string>
#include <bitset>
#include <cmath>
#include <queue>
#include <stack>
#include <ctime>
#include <list>
#include <map>
#include <set>

#define REP(i,n) for(int i=0;i<(n);i++)
#define TR(i,x) for(__typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define ALL(x) x.begin(),x.end()
#define SORT(x) sort(ALL(x))
#define CLEAR(x) memset(x,0,sizeof(x))
#define FILL(x,c) memset(x,c,sizeof(x))
#define SIZE(x) (int)(x).size()

#define MP make_pair
#define PB push_back

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;

void output(LL x) {
    cout << x - (x + 1) / 2 << " " << (x + 1) / 2 - 1 << endl;
}

vector<pair<LL,LL> > gao(vector<pair<LL,LL> >& v) {
    vector<pair<LL,LL> > ret;
    SORT(v);
    for (int i = 0; i < SIZE(v); ) {
        int j = i + 1;
        LL cnt = v[i].second;
        while (j < SIZE(v) && v[j].first == v[i].first) {
            cnt += v[j].second;
            ++j;
        }
        ret.PB(MP(v[i].first, cnt));
        i = j;
    }
    return ret;
}

void go(vector<pair<LL,LL> > v, LL K) {
    if (SIZE(v) == 1) {
        if (K <= v[0].second) {
            output(v[0].first);
            return;
        } else {
            K -= v[0].second;
        }
    } else {
        assert(SIZE(v) == 2);
        assert(v[0].first + 1 == v[1].first);
        if (K <= v[1].second) {
            output(v[1].first);
            return;
        } else {
            K -= v[1].second;
        }
        if (v[0].first > 1 && K <= v[0].second) {
            output(v[0].first);
            return;
        } else {
            K -= v[0].second;
        }
    }
    vector<pair<LL,LL> > tmp;
    TR(it, v) {
        LL x = it->first, y = it->second;
        if (x > 1) {
            tmp.PB(MP((x + 1) / 2 - 1, y));
            tmp.PB(MP(x - (x + 1) / 2, y));
        }
    }
    go(gao(tmp), K);
}

void Solve() {
    LL N, K;
    cin >> N >> K;
    vector<pair<LL,LL> > v;
    v.PB(MP(N, 1));
    go(gao(v), K);
}

int main() {
//	freopen("C.in","r",stdin);
//	freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
//	freopen("C-small-attempt1.in","r",stdin);freopen("C-small-attempt1.out","w",stdout);
//	freopen("C-small-attempt2.in","r",stdin);freopen("C-small-attempt2.out","w",stdout);
	freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);
    int cas;
    cin >> cas;
    for (int T = 1; T <= cas; ++T) {
        printf("Case #%d: ", T);
        Solve();
        cerr << "Case #" << T << ": done!" << endl;
    }
    return 0;
}

