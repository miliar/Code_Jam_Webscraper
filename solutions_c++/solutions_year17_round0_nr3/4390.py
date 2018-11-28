#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <stack>
#include <queue>
#include <functional>
#include <algorithm>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <vector>
#include <array>
#include <tuple>
#include <utility>
#include <numeric>
#include <iomanip>
#include <cctype>
#include <cmath>
#include <assert.h>
#include <cstdlib>
#include <list>
using namespace std;

using ll = long long;
using ull = unsigned long long;
using PII = pair<int, int>;
using PLL = pair<ll, ll>;

template<typename T1, typename T2> ostream& operator<<(ostream& s, const pair<T1, T2>& p) {
    return s << "(" << p.first << ", " << p.second << ")";
}
template<typename T> ostream& operator<<(ostream& s, const vector<T>& v) {
    s << "[";
    for (int i = 0; i < v.size(); i++) s << (i == 0 ? "" : ", ") << v[i];
    s << "]";
    return s;
}

#define ALL(a) (a).begin(), (a).end()

int main() {
    int t;
    cin >> t;

    for (int no = 0; no < t; no++) {
        int n, k;
        cin >> n >> k;

        priority_queue<int> que;
        que.push(n);
        int cnt = 0;
        while (!que.empty() && cnt < k) {
            int seg = que.top(); que.pop();
            cnt++;

            int seg1 = (seg - 1) / 2,
                seg2 = seg / 2;

            if (cnt == k) {
                cout << "Case #" << no + 1 << ": " << max(seg1, seg2)
                     << " " << min(seg1, seg2) << endl;
            } else {
                if (seg1 > 0) que.push(seg1); 
                if (seg2 > 0) que.push(seg2);
            }
        }
    }

    return 0;
}
