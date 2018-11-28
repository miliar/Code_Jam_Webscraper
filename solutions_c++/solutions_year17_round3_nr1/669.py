#pragma once

#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <memory>
#include <algorithm>

namespace Google
{
    template<typename P>
    void solve(const char* inputPath, const char* outputPath)
    {
        P p;
        p.readTestCases(inputPath);
        p.m_results.reserve(p.m_inputs.size()); //optional
        p();
        p.writeResults(outputPath);
    }

    void solveCurrentProblem();

    template<typename TC, typename R = int>
    class Problem
    {
    public:
        typedef std::vector<TC> TestCases;
        typedef std::vector<R> Results;
        typedef std::string FilePath;

        virtual void operator() () = 0;

    protected:
        Problem() {}

        TestCases m_inputs;
        Results m_results;

        void readTestCases(const FilePath& inputPath)
        {
            std::ifstream inFile(inputPath);
            //read the number of test cases
            size_t T = 0;
            inFile >> T;
            m_inputs.reserve(T);

            for (size_t i = 0; i < T; ++i)
            {
                m_inputs.push_back(TC());
                readTestCase(m_inputs.back(), inFile);
            }
        }

        void writeResults(const FilePath& outputPath)
        {
            std::ofstream outFile(outputPath);
            for (size_t i = 0; i < m_results.size(); ++i)
            {
                outFile << "Case #" << i + 1 << ": ";
                writeResult(outFile, m_results[i]);
                outFile << std::endl;
            }
        }

        template<typename P>
        friend void solve(const char* inputPath, const char* outputPath);
    };

    template<typename TC>
    inline void readTestCase(TC& tc, std::istream& is)
    {
        is >> tc;
    }

    template<typename R>
    inline void writeResult(std::ostream& os, const R& r)
    {
        os << r;
    }
}
