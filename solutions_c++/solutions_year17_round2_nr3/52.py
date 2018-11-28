/* This is template part for Google CodeJam contest
 * created by Shapovalov Nikita, 2016
 */

#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>

namespace CodeJamUtility {

    class TestCaseUtil
    {
        std::clock_t start_test_time;

        int test_id_;
        int precision_;

        std::stringstream ss;

    public:
        TestCaseUtil(int test_id, int precision = 10) :
            start_test_time(std::clock()),
            test_id_(test_id),
            precision_(precision),
            ss()
        {
            std::cerr << "Processing test #" << std::setw(4) << test_id << ": ";
            ss << std::fixed << std::setprecision(precision_);
        }

        TestCaseUtil(const TestCaseUtil &) = delete;

        TestCaseUtil &operator=(const TestCaseUtil &) = delete;

        ~TestCaseUtil()
        {
            std::cerr << "Ok. Time elapsed: " << std::setw(5) <<
                (std::clock() - start_test_time) / (1. * CLOCKS_PER_SEC) << " secs" << std::endl;
            std::cout << "Case #" << test_id_ << ": " << ss.str() << "\n";
        }

        template< class T >
        friend TestCaseUtil &operator<<(TestCaseUtil &, const T &obj);

    };

    template< class T >
    TestCaseUtil &
    operator<<(TestCaseUtil &t, const T &obj)
    {
        t.ss << obj;
        return t;
    }
}

#define EXECUTE_FUNCTION(NAME) \
    process(CodeJamUtility::TestCaseUtil & NAME)

#define CODEJAM_RUN_NEW_TEST(ID, NAME) \
    {\
        CodeJamUtility::TestCaseUtil NAME(ID);\
        process(NAME);\
    }

#define CODEJAM_RUN_ALL_TESTS(NAME)\
int main() \
{\
    std::ios_base::sync_with_stdio(false); \
    int testNumber##NAME;\
    std::cin >> testNumber##NAME;\
    for (int counter##NAME = 1; counter##NAME <= testNumber##NAME; ++counter##NAME) {\
        CODEJAM_RUN_NEW_TEST(counter##NAME, NAME);\
    }\
    return 0;\
}

#include <bits/stdc++.h>

using namespace std;

/* End of template part */

#define ve vector
#define pa pair
#define tu tuple

typedef ve< int > vi;
typedef long double ld;
typedef int64_t ll;

void
EXECUTE_FUNCTION(out)
{
    int n, q;
    cin >> n >> q;
    vi s(n), e(n);
    ve< ve< ll > > d(n, ve< ll >(n, 0));
    for (int i = 0; i < n; ++i) {
        cin >> e[i] >> s[i];
    }
    for (int i = 0; i < n; ++i) {
        for (ll &x: d[i]) {
            cin >> x;
        }
    }
    for (int i = 0; i < n; ++i) {
        d[i][i] = 0;
    }
    // floyd
    for (int k = 0; k < n; ++k) {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (d[i][k] != -1 && d[k][j] != -1) {
                    ll nd = d[i][k] + d[k][j];
                    if (d[i][j] == -1 || d[i][j] > nd) {
                        d[i][j] = nd;
                    }
                }
            }
        }
    }
    for (int _ = 0; _ < q; ++_) {
        int u, v;
        cin >> u >> v;
        --u, --v;
        ve< ld > dist(n, -1);
        vi used(n, 0);
        dist[u] = 0;
        while (!used[v]) {
            int id = -1;
            for (int i = 0; i < n; ++i) {
                if (!used[i] && dist[i] > -0.5 && (id == -1 || dist[id] > dist[i])) {
                    id = i;
                }
            }
            if (id == -1) break;
            used[id] = 1;
            for (int to = 0; to < n; ++to) {
                if (d[id][to] == -1 || d[id][to] > e[id]) continue;
                ld nd = dist[id] + (d[id][to] * ld(1.) / s[id]);
                if (dist[to] == -1 || dist[to] > nd) {
                    dist[to] = nd;
                }
            }
        }
        out << dist[v];
        if (_ != q - 1) {
            out << ' ';
        }
    }
}

CODEJAM_RUN_ALL_TESTS(Qual_2015_)
