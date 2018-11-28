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

void Solve() {
    int N, P;
    cin >> N >> P;
    vector<int> cnt(P, 0);
    REP(i, N) {
        int x;
        cin >> x;
        ++cnt[x % P];
    }
    int ans = cnt[0];
    if (P == 2) {
        ans += cnt[1] + 1 >> 1;
        cnt[1] = 0;
    } else if (P == 3) {
        int t = min(cnt[1], cnt[2]);
        ans += t;
        cnt[1] -= t;
        cnt[2] -= t;
        if (cnt[1]) {
            ans += (cnt[1] + 2) / 3;
        } else if (cnt[2]) {
            ans += (cnt[2] + 2) / 3;
        }
    } else if (P == 4) {
        int t = min(cnt[1], cnt[3]);
        ans += t;
        cnt[1] -= t;
        cnt[3] -= t;
        if (cnt[1] > 0 && cnt[2] > 0) {
            int tt = min(cnt[1] / 2, cnt[2]);
            ans += tt;
            cnt[1] -= tt + tt;
            cnt[2] -= tt;
        }
        if (cnt[3] > 0 && cnt[2] > 0) {
            int tt = min(cnt[3] / 2, cnt[2]);
            ans += tt;
            cnt[3] -= tt + tt;
            cnt[2] -= tt;
        }
        if (cnt[2] > 0) {
            ans += cnt[2] / 2;
            cnt[2] &= 1;
        }
        int sum = 0;
        for (int i = P - 1; i > 0; --i) {
            REP(j, cnt[i]) {
                sum += i;
                if (sum % P == 0) {
                    ++ans;
                    sum %= P;
                }
            }
        }
        if (sum > 0) {
            ++ans;
        }
    }
    cout << ans << endl;
}

int main() {
//	freopen("A.in","r",stdin);
//	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
//  freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
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


