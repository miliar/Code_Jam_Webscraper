#include <bits/stdc++.h>
using namespace std;

typedef long long int bint;
typedef pair<bint, bint> bpair;

bint l(bint n) {
    assert (n > 0);
    return (n - 1) / 2;
}

bint r(bint n) {
    return (n - 1) - l(n);
}

bpair shrink(bpair range) {
    assert (range.first <= range.second &&
            range.second - range.first <= 2);

    bint ls = l(range.first);
    bint gt = r(range.second);
    return bpair(ls, gt);
}

bint num_holes(bint s, bint n) {
    assert (s >= 0 && n >= 0);

    typedef map<bpair, bint> mem_t;
    static mem_t mem;

    bint result;
    if (s == 0 || s > n) {
        result = 0;
    }
    else if (s == n) {
        result = 1;
    }
    else {
        mem_t::iterator iter = mem.find(bpair(s, n));
        if (iter != mem.end()) {
            result = iter->second;
        }
        else {
            result = num_holes(s, l(n)) + num_holes(s, r(n));
            mem[bpair(s, n)] = result;
        }
    }

    return result;
}

bint num_holes_gt(bint s, bint n) {
    assert (s > 0 && n >= 0);

    bint t, result = 0;
    bpair range(n, n);
    for (;;) {
        for (t = range.second; t >= range.first && t > s; --t) {
            result += num_holes(t, n);
        }

        if (t <= s) {
            return result;
        }

        range = shrink(range);
    }
}

bint hole_start(bint s, bint n, bint j) {
    assert (s > 0 && n >= 0 && j >= 0);

    bint result;
    if (s == n) {
        result = 0;
    }
    else {
        bint num_l_holes = num_holes(s, l(n));
        if (j < num_l_holes) {
            result = hole_start(s, l(n), j);
        }
        else {
            result = l(n) + 1 + hole_start(s, r(n), j - num_l_holes);
        }
    }

    return result;
}

bpair hole_info(bint n, bint i) {
    assert (1 <= i && i <= n);

    bint done = 0, old_done;
    bint s, old_s;
    bint hole_size, hole_rank;
    bpair range(n, n);

    for (;;) {
        for (s = range.second; s >= range.first && s > 0; --s) {
            old_s = s;
            old_done = done;
            done += num_holes(s, n);

            if (done >= i) {
                hole_size = old_s;
                hole_rank = i - old_done - 1;
                return make_pair(hole_size, hole_rank);
            }
        }
        range = shrink(range);
    }
}

void man_pos(bint n, bint i) {
    assert (1 <= i && i <= n);

    bpair hole = hole_info(n, i);
    bint hole_size = hole.first;
    bint hole_rank = hole.second;

    bint pos = hole_start(hole_size, n, hole_rank) + l(hole_size) + 1;
    bint a = pos - hole_start(hole_size, n, hole_rank) - 1;
    bint b = hole_start(hole_size, n, hole_rank) + hole_size - pos;
    cout << max(a, b) << " " << min(a, b) << endl;
}

void Solve(int testNum) {
    bint n, k, step = 1;
    cin >> n >> k;
    printf("Case #%d: ", testNum);
    man_pos(n, k);
}

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

    int t;
    scanf("%d", &t);
    for(int i = 0; i < t; i++) {
        Solve(i+1);
    }
}
