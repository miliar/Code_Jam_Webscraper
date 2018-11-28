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

int hd, ad, hk, ak, b, d;

struct TState {
    static int64 states[105 * 105 * 105 * 105];

    int64 hpD, attD, hpK, attK;

    int64& value() {
        return states[
            hpD * 105 * 105 * 105
            + attD * 105 * 105
            + hpK * 105
            + attK
        ];
    }

    TState Move(int id) const {
        if (id == 0) return {std::max(0LL, hpD - attK), attD, std::max(0LL, hpK - attD), attK};
        if (id == 1) return {std::max(0LL, hpD - attK), std::min(hpK, attD + b), hpK, attK};
        if (id == 2) return {std::max(0LL, hd - attK), attD, hpK, attK};
        assert(id == 3);
        int64 a = std::max(0LL, attK - d);
        return {std::max(0LL, hpD - a), attD, hpK, a};
    }
};

int64 TState::states[105 * 105 * 105 * 105];

class TSolver {
public:
    explicit TSolver(std::istream& in) {
        in >> hd >> ad >> hk >> ak >> b >> d;
    }

    int ans = -1;

    void Solve() {
        std::queue<TState> q;
        q.push(TState{hd, ad, hk, ak});
        memset(TState::states, -1, sizeof TState::states);
        q.front().value() = 0;
        while (!q.empty()) {
            auto v = q.front();
            q.pop();
            if (!v.hpK) {
                ans = v.value();
                return;
            }
            if (!v.hpD) continue;
            for (int i = 0; i < 4; ++i) {
                auto u = v.Move(i);
                if (u.value() == -1) {
                    q.push(u);
                    u.value() = v.value() + 1;
                }
            }
        }
    }

    void PrintAnswer(std::ostream& out) const {
        if (ans != -1) out << ans; else out << "IMPOSSIBLE\n";
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
