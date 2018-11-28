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

const int MAXN = 1e3 + 10;

int N, C, M;

void Solve() {
    int P[MAXN], B[MAXN];
    cin >> N >> C >> M;
    int have[MAXN];
    CLEAR(have);
    int numberOfRides = 0;
    vector<int> candi[MAXN];
    REP(i, M) {
        cin >> P[i] >> B[i];
        candi[P[i]].PB(B[i]);
        numberOfRides = max(numberOfRides, ++have[B[i]]);
    }
    int cnt[MAXN];
    CLEAR(cnt);
    for (int pos = 1; pos <= N; ++pos) {
        cnt[pos] += SIZE(candi[pos]);
        while (cnt[pos] > numberOfRides * pos) {
           ++numberOfRides;
        }
        cnt[pos + 1] += cnt[pos];
    }
    int numberOfPromotions = 0;
    for (int i = 1; i <= N; ++i) {
        numberOfPromotions += max(0, SIZE(candi[i]) - numberOfRides);
    }
    cout << numberOfRides << " " << numberOfPromotions << endl;
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
        clock_t start = clock();
        Solve();
        clock_t end = clock();
        cerr << "Case #" << T << " done! " << (end - start) * 1000 / CLOCKS_PER_SEC << "ms" << endl;
    }
    return 0;
}


