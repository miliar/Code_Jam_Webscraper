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
    static const size_t MaxN = 1005;

    std::bitset<MaxN> state;
    int n, k;
    int ans = 0;

    explicit TSolver(std::istream& in) {
        std::string s;
        in >> s >> k;
        n = s.size();
        for (size_t i = 0; i < s.size(); ++i) {
            state[i] = s[i] == '-';
        }
    }

    int DoSolve() {
        if (state.none()) {
            return 0;
        }
        if (k > n && state.any()) {
            return -1;
        }
        for (int i = 0; i + k <= n; ++i) {
            // debug("%s\n", state.to_string().c_str());
            if (state.test(i)) {
                ++ans;
                for (int j = i; j < i + k; ++j)
                    state.flip(j);
            }
        }
        return state.none() ? ans : -1;
    }

    void Solve() {
        ans = DoSolve();
    }

    void PrintAnswer(std::ostream& out) const {
        if (ans == -1) {
            out << "IMPOSSIBLE";
        } else {
            out << ans;
        }
    }
};

int main() {
    std::ios_base::sync_with_stdio(false);

    int t;
    std::cin >> t;
    for (int i = 1; i <= t; ++i) {
        using S = TMultiSolver<TSolver>;
        using P = std::unique_ptr<S>;
        auto solver = P(new S(i, std::cin));
        solver->Solve();
        solver->PrintAnswer(std::cout);
        debug("%d ", i);
        timestamp(multi);
    }

    timestamp(end);
    return 0;
}
