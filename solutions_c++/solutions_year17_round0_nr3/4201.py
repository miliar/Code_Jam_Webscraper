#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

struct Space {
    int index;
    int length;

    bool operator< (const Space& r) const {
        if (length == r.length) {
            return index < r.index;
        }

        return length < r.length;
    }
};

pair<int, int> solve(int N, int K) {
    pair<int, int> ans;
    set<Space> s;
    s.insert({0, N});

    for (int k = 1; k <= K; ++k) {
        Space space = *(s.rbegin());
        s.erase(space);

        Space s1, s2;
        if (space.length % 2 == 1) {
            s1.index = space.index;
            s1.length = space.length / 2;
            s2.index = space.index + space.length / 2 + 1;
            s2.length = space.length / 2;
        }
        else {
            s1.index = space.index;
            s1.length = space.length / 2 - 1;
            s2.index = space.index + space.length / 2;
            s2.length = space.length / 2;
        }

        if (k == K) {
            ans.first = s2.length;
            ans.second = s1.length;
        }

        s.insert(s1);
        s.insert(s2);
    }

    return ans;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        int N, K;
        cin >> N >> K;
        auto ans = solve(N, K);
        cout << "Case #" << t << ": " << ans.first << " " << ans.second << endl;
    }
    return 0;
}
