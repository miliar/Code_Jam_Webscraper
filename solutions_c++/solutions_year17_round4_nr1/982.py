#include <Problem.h>

#define CURRENT_PROBLEM



#ifdef CURRENT_PROBLEM


struct TestCase
{
    int N = 0;
    int P = 0;
    std::vector<int> G;
};

typedef int Result;

class r2_2017_A : public Google::Problem<TestCase, Result>
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
        int N = tc.N;
        int P = tc.P;
        std::vector<int> G(P, 0);
        for (int i = 0; i < N; ++i)
            G[tc.G[i]] += 1;
        
        int res = 0;

        // 0.
        res += G[0];
        N -= G[0];
        G[0] = 0;
        if (N == 0)
            return res;

        // P >= 2
        for (int i = 1; 2 * i <= P && N > 0; ++i)
        {
            
            if (i == P - i)
            {
                int c = G[i] / 2;
                res += c;
                N -= 2 * c;
                G[i] -= 2 * c;
                continue;
            }

            int c = 0;
            if (G[i] < G[P - i])
            {
                c = G[i];
                G[P - i] -= G[i];
                G[i] = 0;
            }
            else
            {
                c = G[P - i];
                G[i] -= G[P - i];
                G[P - i] = 0;
            }
            N -= 2 * c;
            res += c;
        }

        if (N == 0)
            return res;

        // P >= 3 (1, 1, 1), (1, 1, 2)
        while (G[1] >= 2)
        {
            G[1] -= 2;
            if (G[P - 2] > 0)
            {
                G[P - 2] -= 1;
                res += 1;
                N -= 3;
            }
            else
            {
                G[1] += 2;
                break;
            }
        }

        // (2, 2, 2)
        if (P == 3)
        {
            int c = G[2] / 3;
            res += c;
            N -= 3 * c;
        }

        // P == 4 (1, 1, 1, 1)
        if (P == 4)
        {
            //(2, 3, 3)
            int c = G[3] / 2;
            if (G[2] >= c)
            {
                G[2] -= c;
                G[3] -= 2 * c;
                res += c;
                N -= 3 * c;
            }


            //(1, 1, 1, 1)
            c = G[1] / 4;
            res += c;
            N -= 4 * c;

            // (3, 3, 3, 3)
            c = G[3] / 4;
            res += c;
            N -= 4 * c;
        }

        // leftovers
        if (N > 0)
            res += 1;

        return res;
    }
};


void solveCurrentProblem()
{
    // A-test
    // A-small-attempt0
    // A-large
    //Google::solve<r2_2017_A>("2017/A-test.in", "2017/A-test.out");
    //Google::solve<r2_2017_A>("2017/A-small-attempt2.in", "2017/A-small-attempt2.out");
    Google::solve<r2_2017_A>("2017/A-large.in", "2017/A-large.out");
}


template<>
inline void Google::readTestCase(TestCase& tc, std::istream& is)
{
    is >> tc.N;
    is >> tc.P;
    tc.G.reserve(tc.N);
    for (int i = 0; i < tc.N; ++i)
    {
        int g = 0;
        is >> g;
        tc.G.push_back(g % tc.P);
    }
}


#endif // CURRENT_PROBLEM
