
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <queue>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <utility>

using namespace std;

typedef struct Interval {
    int l;
    int r;
    int size;
} Interval;

class MyComp {
public:
    bool operator() (Interval& l, Interval r) {
        if (l.size < r.size) {
            return true;
        } else if (l.size == r.size) {
            if (l.l < r.l) {
                return true;
            }
        } else {
            return false;
        }
    }
};

pair<int, int> solve(int n, int k) {
    MyComp comp;
    priority_queue<Interval, vector<Interval>, MyComp> pq(comp);

    vector<int> stalls(n+2);
    stalls[0] = 1;
    stalls[n+1] = 1;

    Interval it;
    it.l = 1;
    it.r = n;
    it.size = n;
    pq.push(it);

    for (int i = 0; i < k; i++) {
        Interval it = pq.top();
        pq.pop();
        int pos = (it.r + it.l) / 2;
        stalls[pos] = 1;
        if (it.size == 1) {
            if (i == k-1) {
                int l = pos - it.l;
                int r = it.r - pos;

                return make_pair(max(l, r), min(l, r));
            }
            continue;
        } else if (it.size == 2) {
            Interval itNew;
            itNew.l = it.r;
            itNew.r = it.r;
            itNew.size = 1;
            pq.push(itNew);
        } else {
            Interval itNew;
            itNew.l = it.l;
            itNew.r = pos-1;
            itNew.size = (pos-1) - it.l + 1;
            pq.push(itNew);

            Interval itNewTwo;
            itNewTwo.l = pos+1;
            itNewTwo.r = it.r;
            itNewTwo.size = itNewTwo.r - itNewTwo.l + 1;
            pq.push(itNewTwo);
        }

        if (i == k-1) {
            int l = pos - it.l;
            int r = it.r - pos;
            return make_pair(max(l, r), min(l, r));
        }
    }

};

int main() {

    int t;
    int n, k;

    scanf("%d", &t);
    for (int i = 1; i <= t; i++) {
        scanf("%d %d", &n, &k);
        pair<int, int> ans = solve(n, k);
        cout << "Case #" << i << ": " << ans.first << " " << ans.second << endl;
    }

}
