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
    int n, k;
    TReal u;
    TReal p[55];

    explicit TSolver(std::istream& in) {
        in >> n >> k >> u;
        for (int i = 0; i < n; ++i) {
            in >> p[i];
        }
    }

    TReal score(TReal bound) const {
        TReal here[55];
        TReal left = u;
        for (int i = 0; i < n; ++i) {
            left -= std::max<TReal>(0., bound - p[i]);
            here[i] = std::max(bound, p[i]);
        }
        if (left < 0.0) {
            return -1.;
        }
        return std::accumulate(here, here + n, 1.0L, std::multiplies<TReal>());
    }

    bool ok(TReal bound) const {
        return score(bound) >= 0.0;
    }

    TReal bound = -1;
    void Solve() {
        TReal l = *std::min_element(p, p + n);
        TReal r = 1.0;
        for (int i = 0; i < 300; ++i) {
            TReal mid = (l + r) / 2.;
            if (ok(mid)) {
                l = mid;
            } else {
                r = mid;
            }
        }
        bound = l;
    }

    void PrintAnswer(std::ostream& out) const {
        out.precision(8);
        out << std::fixed << score(bound);
    }
};

int main() {
    std::ios_base::sync_with_stdio(false);

    int t;
    std::cin >> t;
    for (int i = 1; i <= t; ++i) {
        auto solver = std::make_unique<TMultiSolver<TSolver>>(i, std::cin);
        solver->Solve();
        solver->PrintAnswer(std::cout);
        debug("%d ", i);
        timestamp(multi);
    }

    timestamp(end);
    return 0;
}
