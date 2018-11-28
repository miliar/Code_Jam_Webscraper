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

const int MAXN = 60;
const int MAXP = 60;

int N, P;
int R[MAXN];
int Q[MAXN][MAXP];
int cnt[MAXN];

int cmp(int a, int b) {
    LL t = (LL)Q[a][cnt[a]] * R[b] - (LL)Q[b][cnt[b]] * R[a];
    return t < 0 ? -1 : t > 0;
}

bool Go() {
    int mini = 0, maxi = 0;
    bool ret = true;
    REP(i, N) {
        if (cmp(i, mini) < 0) {
            mini = i;
        }
        if (cmp(i, maxi) > 0) {
            maxi = i;
        }
    }
    double r = floor((double)Q[mini][cnt[mini]] / R[mini] / 0.9); 
    double l = ceil((double)Q[maxi][cnt[maxi]] / R[maxi] / 1.1);
    if (r >= l) {
        REP(i, N) ++cnt[i];
    } else {
        ++cnt[mini];
    }
    return r >= l;
}

void Solve() {
    cin >> N >> P;
    REP(i, N) cin >> R[i];
    REP(i, N) {
        REP(j, P) {
            cin >> Q[i][j];
        }
        sort(Q[i], Q[i] + P);
    }
    int ans = 0;
    int rem = N * P;
    CLEAR(cnt);
    while (rem){
        if (Go()) {
            ++ans;
            rem -= N;
        } else {
            --rem;
        }
    }
    cout << ans << endl;
}

int main() {
//	freopen("B.in","r",stdin);
//	freopen("B-small-attempt0.in","r",stdin);freopen("B-small-attempt0.out","w",stdout);
//	freopen("B-small-attempt1.in","r",stdin);freopen("B-small-attempt1.out","w",stdout);
//	freopen("B-small-attempt2.in","r",stdin);freopen("B-small-attempt2.out","w",stdout);
	freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);
    int cas;
    cin >> cas;
    for (int T = 1; T <= cas; ++T) {
        printf("Case #%d: ", T);
        Solve();
        cerr << "Case #" << T << ": done!" << endl;
    }
    return 0;
}

