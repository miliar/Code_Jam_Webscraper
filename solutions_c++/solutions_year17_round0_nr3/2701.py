#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;

typedef long long ll;

struct stall {

    ll w, c;

    stall(ll width, ll quantity) {

        w = width;
        c = quantity;
    }

    ll min() {
        return w - w / 2 - 1;
    }

    ll max() {
        return w / 2;
    }

    vector<stall> split() {

        vector<stall> res;
        res.push_back(stall(min(), c));
        res.push_back(stall(max(), c));

        return res;
    }
};

struct stallCmp {

    bool operator()(stall a, stall b) {

        return a.w > b.w;
    }
};

struct bathroom {

    set<stall, stallCmp> s;

    bathroom(stall st) {

        s.insert(st);
    }

    stall nextStalls() {

        stall res = *s.begin();
        s.erase(s.begin());

        vector<stall> split = res.split();
        for (int i = 0; i < split.size(); ++i)
            if (split[i].w > 0)
                addStalls(split[i]);

        return res;
    }

    void addStalls(stall x) {

        set<stall>::iterator f = s.find(x);

        if (f != s.end()) {

            stall tmp = *f;
            s.erase(f);
            tmp.c += x.c;
            s.insert(tmp);
        }
        else s.insert(x);
    }
};

int main() {

    int t;
    ll n, k;

    scanf("%d", &t);

    for (int caseno = 1; caseno <= t; ++caseno) {

        scanf("%lld%lld", &n, &k);

        bathroom b = bathroom(stall(n, 1));
        stall curStall(0, 0);

        do {

            curStall = b.nextStalls();
            k -= curStall.c;

        } while (k > 0);

        printf("Case #%d: %lld %lld\n", caseno, curStall.max(), curStall.min());
    }
}
