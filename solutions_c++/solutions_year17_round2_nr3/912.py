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

typedef long long i64;
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

const i64 INF = 1e16;

class TSolver {
public:
    int n;
    int e[105];
    int s[105];
    i64 d[105][105];

    int q;
    int U[105];
    int V[105];

    explicit TSolver(std::istream& in) {
        in >> n >> q;
        for (int i = 0; i < n; ++i) {
            in >> e[i] >> s[i];
        }
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                in >> d[i][j];
            }
        }
        for (int i = 0; i < q; ++i) {
            in >> U[i] >> V[i];
        }
    }

    i64 dClosure[105][105];
    void MakeDClosure() {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                dClosure[i][j] = (d[i][j] == -1 ? INF : d[i][j]);
            }
        }
        for (int k = 0; k < n; ++k) {
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < n; ++j) {
                    dClosure[i][j] = std::min(dClosure[i][j], dClosure[i][k] + dClosure[k][j]);
                }
            }
        }
    }

    TReal edges[105][105];
    void MakeEdges() {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                auto dc = dClosure[i][j];
                if (dc <= e[i]) {
                    edges[i][j] = TReal(dc) / s[i];
                } else {
                    edges[i][j] = INF;
                }
            }
            edges[i][i] = 0;
        }
    }

    void MakeRanges() {
        for (int k = 0; k < n; ++k)
            for (int i = 0; i < n; ++i)
                for (int j = 0; j < n; ++j)
                    edges[i][j] = std::min(edges[i][j], edges[i][k] + edges[k][j]);
    }

    void Solve() {
        MakeDClosure();
        MakeEdges();
        MakeRanges();
    }

    void PrintAnswer(std::ostream& out) const {
        out.precision(6);
        for (int i = 0; i < q; ++i) {
            if (i) out << ' ';
            out << std::fixed << edges[U[i]-1][V[i]-1];
        }
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
