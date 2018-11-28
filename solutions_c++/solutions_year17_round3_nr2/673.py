#include <Problem.h>

#define CURRENT_PROBLEM



#ifdef CURRENT_PROBLEM


struct TestCase
{
    std::map<std::pair<size_t, size_t>, size_t> a; // timeslot -> 0-Cameron or 1-Jamie
};

typedef size_t Result;
const int M = 1440;
const int B = 720;

class r1_2017_3B : public Google::Problem<TestCase, Result>
{
public:
    void operator() () override
    {
        size_t i = 0;
        for (const auto& tc : m_inputs)
        {
            m_results.push_back(solveTestCase(tc));
            std::cout << ++i << std::endl;
        }
    }

private:
    Result solveTestCase(const TestCase& tc)
    {
        // edge cases
        if (tc.a.size() < 2)
            return 2;

        size_t res = 0;
        size_t A[2] = { 0, 0 }; // total activity time
        std::multiset<int> S[2]; // negatives; special time slots
        size_t Ts[2] = { 0, 0 }; // total special time

        for (auto it = tc.a.begin(); it != tc.a.end(); ++it)
        {
            // TODO
            A[it->second] += it->first.second - it->first.first;

            auto nxt = it;
            ++nxt;
            if (nxt == tc.a.end())
                nxt = tc.a.begin();

            if (it->second != nxt->second)
            {
                ++res;
                continue;
            }
            else
            {
                int Ti = 0;
                if (nxt->first.first <= it->first.first)
                {
                    Ti = nxt->first.first + M - it->first.second;
                }
                else
                {
                    Ti = nxt->first.first - it->first.second;
                }
                if (Ti > 0)
                {
                    Ts[it->second] += Ti;
                    S[it->second].insert(-1 * Ti);
                }
            }
        }

        for (size_t i = 0; i < 2; ++i)
        {
            int Ti = A[i] + Ts[i];
            if (Ti > B)
            {
                // start reducing
                for (auto it = S[i].begin(); it != S[i].end(); ++it)
                {
                    Ti += *it;
                    res += 2; // 2 more switches
                    if (Ti <= B)
                        break; // enough switching
                }
            }
        }

        return res;
    }
};


void solveCurrentProblem()
{
    // B-test
    // B-small-attempt0
    // B-large
    Google::solve<r1_2017_3B>("2017_r1C/B-large.in", "2017_r1C/B-large.out");
}


template<>
inline void Google::readTestCase(TestCase& tc, std::istream& is)
{
    size_t A[2];
    is >> A[0];
    is >> A[1];
    for (size_t i = 0; i < A[0]; ++i)
    {
        size_t tb;
        size_t te;
        is >> tb;
        is >> te;
        tc.a.emplace(std::make_pair(tb, te), 0);
    }
    for (size_t i = 0; i < A[1]; ++i)
    {
        size_t tb;
        size_t te;
        is >> tb;
        is >> te;
        tc.a.emplace(std::make_pair(tb, te), 1);
    }
}



#endif // CURRENT_PROBLEM
