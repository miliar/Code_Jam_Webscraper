#include <iostream>
#include <stdio.h>
#include <limits.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <queue>

typedef long long ll;
using namespace std;

int t,n, k;

struct item {
    int min;
    int max;
    int pos;
};

class Cmp{
public:
    bool operator()(const item &a, const item &b) const
    {
        if (a.min == b.min) {
            if (a.max == b.max) {
                return a.pos < b.pos;
            } else {
                return a.max < b.max;
            }
        } else {
            return a.min < b.min;
        }
    }
};


item devide(int l, int r) {
    item t;
    if (l == r) {
        t.pos = l;
        t.min = 0;
        t.max = 0;
        return t;
    }
    if (l+1 == r) {
        t.pos = l;
        t.min = 0;
        t.max = 1;
        return t;
    }
    t.pos = (l+r)/2;
    t.min = t.pos - l;
    t.max = r - t.pos;
    return t;
}

item solve(int n, int k) {
    priority_queue<item, vector<item>, Cmp> q;
    item top;
    q.push(devide(1, n));
    for (int i = 1; i <= k; i++) {
        top = q.top(); q.pop();
        int l = top.pos - top.min;
        int r = top.pos + top.max;
        q.push(devide(l, top.pos-1));
        q.push(devide(top.pos+1, r));
    }
    return top;
}

int main() {
	freopen("C-small-2-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);

    cin >> t;

    for (int tt = 1; tt <= t; tt++) {
        cin >> n >> k;

        item i = solve(n, k);
        cout << "Case #" << tt << ": " << i.max << " " << i.min << endl;
    }


    return 0;
}
