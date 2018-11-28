#include <Problem.h>
#include <algorithm>


class q_2017_B : public Google::Problem<std::string, std::string>
{
public:
    void operator() () override
    {
        for (const auto& tc : m_inputs)
            m_results.push_back(solveTestCase(tc));
    }

private:
    std::string solveTestCase(const std::string& tc)
    {
        size_t curr_index = 0;
        // find the character that 'breaks' the tidiness
        while (curr_index < tc.size() - 1 && tc[curr_index] <= tc[curr_index + 1])
            ++curr_index;
        if (curr_index == tc.size() - 1)
            return tc;

        // find the first character to modify
        while (curr_index > 0)
        {
            if (tc[curr_index - 1] == tc[curr_index])
                --curr_index;
            else
                break;
        }

        // decrement the preceding characters for a minimum, and then append with '9's
        std::string result = tc.substr(0, curr_index);
        if (tc[curr_index] != '1')
            result += tc[curr_index] - 1;
        for (size_t j = curr_index + 1; j < tc.size(); ++j)
            result += '9';

        return result;
    }
};
