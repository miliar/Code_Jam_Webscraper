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

    struct TPancake {
        TReal r, h;

        TReal side() const {
            return 2 * M_PI * r * h;
        }
    };

    std::vector<TPancake> p;

    explicit TSolver(std::istream& in) {
        in >> n >> k;
        p.resize(n);
        for (int i = 0; i < n; ++i) {
            in >> p[i].r >> p[i].h;
        }
    }

    TReal ans = 0.0;

    void Solve() {
        while ((int)p.size() >= k) {
            std::sort(WHOLE(p), [](const TPancake& a, const TPancake& b) {
                return a.r < b.r;
            });

            TReal here = M_PI * p.back().r * p.back().r + p.back().side();
            p.pop_back();

            std::sort(WHOLE(p), [](const TPancake& a, const TPancake& b) {
                return a.side() > b.side();
            });

            for (int i = 0; i + 1 < k; ++i) {
                here += p[i].side();
            }

            ans = std::max(ans, here);
        }
    }

    void PrintAnswer(std::ostream& out) const {
        out.precision(8);
        out << std::fixed << ans;
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
