#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cmath>
#include <cctype>
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <utility>
#include <algorithm>
#include <bitset>
#include <iomanip>

using namespace std;

typedef long long int LLI;

#define _ ios_base::sync_with_stdio(0);

const int inf = 0x3f3f3f3f;
const double eps = 1e-8; 

char str[20];
map<pair<LLI, LLI>, int> cnt[70];

int main() { _
    int t, k, tmp, idx;
    LLI n, a, b;
    cin >> t;

    map<pair<LLI, LLI>, int>::iterator it;
    map<pair<LLI, LLI>, int>::reverse_iterator rit;
    for (int kase = 1; kase <= t; ++kase) {
        cout << "Case #" << kase << ": ";
        cin >> n >> k;
        // first is n/2,(n-1)/2
        // binary with k
        tmp = idx = log2(n);
        cnt[tmp][make_pair((n-1)/2, n/2)] = 1;
        n -= 1L<<tmp;
        for (int i = tmp-1; i >= 0; --i) {
            for (it = cnt[i+1].begin(); it != cnt[i+1].end(); ++it) {
                a = it->first.first;
                b = it->first.second;
                cnt[i][make_pair((a-1)/2, a/2)] += it->second;
                cnt[i][make_pair((b-1)/2, b/2)] += it->second;
            }
        }
        LLI num = 0;
        while (num < k) {
            for (rit = cnt[idx].rbegin(); rit != cnt[idx].rend(); ++rit) {
                num += rit->second;
                if (num >= k) {
                    a = rit->first.second;
                    b = rit->first.first;
                    break;
                }
            }
            --idx;
        }
        cout << a << " " << b << "\n";
        for (int i = 0; i < 70; ++i) cnt[i].clear();
    }

    return 0;
}
