#include <Problem.h>
#include <algorithm>

struct TestCase
{
    size_t K = 0;
    std::string s;
};

struct Result
{
    bool possible = false;
    size_t min_flips = 0;
};

class q_2017_A : public Google::Problem<TestCase, Result>
{
public:
    void operator() () override
    {
        for (const auto& tc : m_inputs)
            m_results.push_back(solveTestCase(tc));
    }

private:
    Result solveTestCase(const TestCase& tc)
    {
        Result r;
        r.possible = true;
        auto s = tc.s;
        for (size_t i = 0; i < s.size(); ++i)
        {
            if (s[i] == '+')
                continue;
            if (s.size() - i < tc.K)
            {
                r.possible = false;
                break;
            }
            std::transform(s.begin() + i, s.begin() + i + tc.K, s.begin() + i, [](const char& ch) { return (ch == '-') ? '+' : '-'; });
            r.min_flips += 1;
        }
        return r;
    }
};

template<>
inline void Google::readTestCase(TestCase& tc, std::istream& is)
{
    is >> tc.s;
    is >> tc.K;
}

template<>
inline void Google::writeResult(std::ostream& os, const Result& r)
{
    if (!r.possible)
        os << "IMPOSSIBLE";
    else
        os << r.min_flips;
}
