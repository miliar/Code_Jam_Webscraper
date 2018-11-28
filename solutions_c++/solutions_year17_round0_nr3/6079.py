#include <iostream>
#include <set>
#include <utility>
using namespace std;

struct comparator {

    bool operator() (const pair<int, int>& lhs, const pair<int, int>& rhs) const {
        int lDiff = lhs.second - lhs.first;
        int rDiff = rhs.second - rhs.first;
        if (lDiff > rDiff) return true;
        if (rDiff > lDiff) return false;
        if (lhs.first < rhs.first) return true;
        return false;
    }
};

void ubaci(set<pair<int, int> , comparator> &s, int fi, int se) {
    if (fi <= se)
        s.insert(make_pair(fi, se));
}


int main() {

    int t; cin >> t;
    int cnt = 0;
    set<pair<int, int>, comparator> s;

    while(t--) {
        cnt++;

        int n; cin >> n;
        int k; cin >> k;
        s.clear();
        s.insert(make_pair(1, n));

        
        for (int i = 0; i < k - 1; i++) {

            pair<int, int> nxt = *s.begin();
            s.erase(s.begin());

            int pol = (nxt.second - nxt.first) / 2;
            ubaci(s, nxt.first, nxt.first + pol - 1);
            ubaci(s, nxt.first + pol + 1, nxt.second);
        }

        pair<int, int> last = *s.begin();
        int diff = (last.second - last.first);
        int mini = diff / 2;
        int maxi = diff / 2 + (diff % 2? 1 : 0);


        printf("Case #%d: %d %d\n", cnt, maxi, mini);


    }
    return 0;
}
