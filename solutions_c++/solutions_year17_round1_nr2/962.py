// License {{{
// Copyright © 2016 Fedor Alekseev <feodor.alexeev@gmail.com>
// This work is free. You can redistribute it and/or modify it under the
// terms of the Do What The Fuck You Want To Public License, Version 2,
// as published by Sam Hocevar. See http://www.wtfpl.net/ for more details.
// }}}

#include <bits/stdc++.h>

#ifdef moskupols
    #define debug(...) fprintf(stderr, __VA_ARGS__)
#else
    #define debug(...) 42
#endif

#define timestamp(x) debug("["#x"]: %.3f\n", (double)clock() / CLOCKS_PER_SEC)

#define hot(x) (x)
#define sweet(value) (value)
#define faceless

#define WHOLE(v) (v).begin(),(v).end()
#define RWHOLE(v) (v).rbegin(),(v).rend()
#define UNIQUE(v) (v).erase(unique(WHOLE(v)),(v).end())

typedef long long int64;
typedef unsigned long long uint64;
typedef long double TReal;

template<class TWrapped>
class TMultiSolver {
public:
    template<typename... Args>
    explicit TMultiSolver(int testCase, Args&&... args)
        : Wrapped(std::forward<Args>(args)...)
        , TestCase(testCase)
    {
    }

    void Solve() {
        Wrapped.Solve();
    }

    void PrintAnswer(std::ostream& out) const {
        out << "Case #" << TestCase << ": ";

        std::ostringstream oss;
        Wrapped.PrintAnswer(oss);
        if (oss.str().back() != '\n') {
            oss << '\n';
        }

        out << oss.str();
    }

    TWrapped Wrapped;
    int TestCase;
};

class TSolver {
public:
    int n, p;
    std::vector<int> req;
    std::vector<std::vector<std::vector<int>>> ranges;

    static std::vector<int> MakeRange(int req, int x) {
        // debug("%d %d: ", req, x);
        std::vector<int> res;

        auto ok = [&](int s) {
            return s > 0 && req * s * 9 <= 10 * x && req * s * 11 >= 10 * x;
        };

        if (ok(x / req)) {
            res.push_back(x / req);
        }

        for (int i = x / req + 1; ok(i); ++i) res.push_back(i);
        for (int i = x / req - 1; ok(i); --i) res.push_back(i);

        std::sort(WHOLE(res));
        // for (auto q : res) debug("%d ", q);
        // debug("\n");
        return res;
    }

    explicit TSolver(std::istream& in) {
        in >> n >> p;
        req.resize(n);
        for (int i = 0; i < n; ++i) in >> req[i];
        ranges.resize(n);
        for (int i = 0; i < n; ++i) {
            auto& ran = ranges[i];
            ran.resize(p);
            for (int j = 0; j < p; ++j) {
                int x;
                in >> x;
                ran[j] = MakeRange(req[i], x);
            }
        }
    }

    int ans = 0;

    void Solve() {
        if (n == 1) {
            for (const auto& r : ranges[0]) {
                ans += !r.empty();
            }
            return;
        }
        assert(n == 2);

        bool ok[10][10];
        for (int i = 0; i < p; ++i) {
            for (int j = 0; j < p; ++j) {
                std::vector<int> tmp;
                std::set_intersection(
                    WHOLE(ranges[0][i]),
                    WHOLE(ranges[1][j]),
                    std::back_inserter(tmp)
                );
                ok[i][j] = !tmp.empty();
            }
        }

        std::vector<int> perm(p);
        for (int i = 0; i < p; ++i) perm[i] = i;
        do {
            int here = 0;
            for (int i = 0; i < p; ++i)
                if (ok[i][perm[i]]) ++here;
            ans = std::max(ans, here);
        } while (std::next_permutation(WHOLE(perm)));
    }

    void PrintAnswer(std::ostream& out) const {
        out << ans;
    }
};

int main() {
    std::ios_base::sync_with_stdio(false);

    int t;
    std::cin >> t;
    for (int i = 1; i <= t; ++i) {
        auto solver = std::make_shared<TMultiSolver<TSolver>>(i, std::cin);
        solver->Solve();
        solver->PrintAnswer(std::cout);
        debug("%d ", i);
        timestamp(multi);
    }

    timestamp(end);
    return 0;
}
