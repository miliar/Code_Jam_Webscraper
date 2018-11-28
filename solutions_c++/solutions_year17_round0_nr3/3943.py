#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <algorithm>
#include <cmath>
#include <map>
#include <queue>
#include <ctime>
#include <unordered_map>
using namespace std;

clock_t begin_time, end_time;
void printtime() {
    end_time = clock();
    double elapsed_secs = double(end_time - begin_time) / CLOCKS_PER_SEC;
    cerr << "\nTime elapsed: " << elapsed_secs << endl;
}

struct Entry {
    int mn, mx, index;

    bool operator<(const Entry &e) const {
        if(mn == e.mn) {
            if(mx == e.mx)
                return index < e.index;
            else
                return mx > e.mx;
        }
        else
            return mn > e.mn;
    }
};

void print(vector<bool> &v) {
    for(auto x: v) {
        if(x)
            cout << "#";
        else
            cout << ".";
    }
    cout << endl;
}

void solve() {
    int k, n;
    cin >> n >> k;
    // min(l, r) -> max(l, r) -> index
    set<Entry> s;
    s.insert({ (n-1)/2, n/2,(n-1)/2});

    vector<bool> used (n+2, false);
    used[0] = used[n + 1] = true;

    Entry t;
    for(int i=0;i<k;i++) {
        t = *s.begin(); s.erase(t);
        used[t.index + 1] = true;
        //print(used);
        //cout << t.index << "_";
        if(t.mn == t.mx && t.mn == 0) continue;
        int left_segment = t.mn;
        Entry L = {(left_segment-1) / 2, left_segment / 2, t.index - left_segment / 2 - 1};

        int right_segment = t.mx;
        Entry R = {(right_segment-1) / 2, right_segment / 2, t.index + (right_segment-1) / 2 + 1};
        s.insert(L);
        s.insert(R);
    }
    cout << t.mx << " " << t.mn << endl;
}

int main() {
    begin_time = clock();

    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int tests;
    scanf("%d", &tests);
    for(int i=0;i<tests;i++) {
        printf("Case #%d: ", i + 1);
        solve();
    }

    printtime();
    return 0;
}