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
    LL n;
    cin >> n;
    int l = 0, d[20], a[20];
    for (LL i = n; i; i /= 10) {
        d[l] = i % 10;
        a[l++] = i % 10;
    }
    for (int i = l - 1; i > 0; --i) {
        if (a[i] > a[i - 1]) {
            --a[i];
            for (int j = i + 1; j < l; ++j) {
                a[j] = min(a[j], a[j - 1]);
            }
            for (int j = i - 1; j >= 0; --j) {
                a[j] = 9;
            }
            break;
        }
    }
    LL ans = 0;
    for (int i = l - 1; i >= 0; --i) {
        if (a[i] < d[i]) {
            ans = ans * 10 + d[i] - 1;
            for(int j = i - 1; j >= 0; --j) {
                ans = ans * 10 + 9;
            }
            break;

        } else {
            ans = ans * 10 + a[i];
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

