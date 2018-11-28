////////////////////////////////////////////////////////////////
//                                                            //
//  Google Code Jam Template                                  //
//  by MooseBoys                                              //
//                                                            //
////////////////////////////////////////////////////////////////

////////////////////////////////////////////////
//                                            //
//  Generic Code                              //
//                                            //
////////////////////////////////////////////////

////////////////////////////////
//  Standard Includes         //
////////////////////////////////

#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <list>
#include <string>
#include <sstream>
#include <algorithm>
#include <cassert>
#include <map>
#include <functional>
#include <random>
#include <set>

////////////////////////////////
//  Non-Standard Includes     //
////////////////////////////////

#include <Windows.h>
#include "..\\..\\Libraries\\BigInteger\\BigIntegerLibrary.hh" // from http://mattmccutchen.net/bigint/
//#include "boost/math/common_factor.hpp" // from http://www.boost.org/


////////////////////////////////
//  Typedefs and Macros       //
////////////////////////////////

typedef long long           LL;
typedef unsigned long long  ULL;


////////////////////////////////
//  Debug Helpers             //
////////////////////////////////

// colored console messages
#define GoodMessage(message) {setColor(GOOD);std::cout<<message<<std::endl;setColor(NORMAL);}
#define BadMessage(message) {setColor(BAD);std::cout<<message<<std::endl;setColor(NORMAL);}
#define ImportantMessage(message) {setColor(IMPORTANT);std::cout<<message<<std::endl;setColor(NORMAL);}
enum consoleColor { NORMAL, GOOD, BAD, IMPORTANT };
inline void setColor(consoleColor c)
{
    WORD wAttributes = 0x07;
    if (c == GOOD) wAttributes = 0x0A;
    if (c == BAD) wAttributes = 0x0C;
    if (c == IMPORTANT) wAttributes = 0xF9;
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), wAttributes);
}


////////////////////////////////
//  Common Functions          //
////////////////////////////////

// find and open a problem input
int loadProblemFile(std::ifstream &inputFile, std::string &inputFileName)
{
    for (char cProblem = 'A'; cProblem <= 'Z'; cProblem++)
    {
        inputFileName = std::string(1, cProblem) + "-test";
        inputFile.open(inputFileName + ".in", std::ifstream::in);
        if (inputFile.is_open()) return 0;
        inputFileName = std::string(1, cProblem) + "-large";
        inputFile.open(inputFileName + ".in", std::ifstream::in);
        if (inputFile.is_open()) return 0;
        for (char cAttempt = '9'; cAttempt >= '0'; cAttempt--)
        {
            inputFileName = std::string(1, cProblem) + "-small-attempt" + cAttempt;
            inputFile.open(inputFileName + ".in", std::ifstream::in);
            if (inputFile.is_open()) return 0;
        }
    }
    return -1;
}

// load and create problem input and output streams
int getProblemIO(std::ifstream &input, std::ofstream &output)
{
    std::string fileName;
    if (loadProblemFile(input, fileName)) { BadMessage("could not find any input files to load"); return -1; }
    else { GoodMessage("successfully loaded input file \"" << fileName << ".in\""); }
    output.open(fileName + ".out", std::ofstream::out);
    if (output.is_open()) { GoodMessage("successfully created output file \"" << fileName << ".out\""); }
    else { BadMessage("could not create output file \"" << fileName << ".out\""); return -1; }
    return 0;
}


////////////////////////////////////////////////
//                                            //
//  Problem-Specific Code                     //
//                                            //
////////////////////////////////////////////////

using namespace std;

// problem entrypoint
int CodeJamMain()
{
    ifstream input;
    ofstream output;

    if (getProblemIO(input, output)) return -1;
    cout << fixed << setprecision(16);
    output << fixed << setprecision(16);

    int T;
    input >> T;
    for (int caseNum = 0; caseNum < T; caseNum++)
    {
        int N, P;
        input >> N >> P;
        vector<long long> R(N);
        for (auto& r : R) input >> r;
        vector<vector<long long>> Q;
        for (int i = 0; i < N; i++)
        {
            vector<long long> QQ(P);
            for (auto& qq : QQ) input >> qq;
            Q.push_back(QQ);
        }

        for (auto& p : Q) sort(p.begin(), p.end());
        vector<vector<set<long long>>> allowedServings(N);
        for (int i = 0; i < N; i++)
        {
            allowedServings[i].resize(P);
            for (int j = 0; j < P; j++)
            {
                for (long long m = (Q[i][j] * 10) / (R[i] * 11) - 1; Q[i][j] * 10 >= R[i] * m * 9; m++)
                {
                    if(Q[i][j] * 10 <= R[i] * m * 11) allowedServings[i][j].insert(m);
                }
            }
        }
        long long sum = 0;
        bool used[52][52];
        int use[52];
        memset(&used[0][0], 0, sizeof(used));
        for (int j = 0; j < P; j++)
        {
            for (const auto& m : allowedServings[0][j])
            {
                memset(&use[0], 0, sizeof(use));
                bool found = false || N == 1;
                for (int i = 1; i < N; i++)
                {
                    for (int k = 0; k < P; k++)
                    {
                        if (used[i][k]) continue;
                        auto m2 = allowedServings[i][k].find(m);
                        if (m2 != allowedServings[i][k].end())
                        {
                            found = true;
                            use[i] = k;
                            break;
                        }
                    }
                    if (!found) break;
                }
                if (found)
                {
                    sum++;
                    for (int k = 1; k < N; k++) used[k][use[k]] = true;
                    break;
                }
            }
        }

        ostringstream answer;

        answer << sum;

        output << "Case #" << caseNum + 1 << ": ";
        output << answer.str() << endl;
        GoodMessage("Case #" << caseNum + 1 << ": " << answer.str());
    }

    return 0;
}

////////////////////////////////////////////////
//                                            //
//  Generic Entrypoint                        //
//                                            //
////////////////////////////////////////////////

int main(int argc, char* argv[])
{
    int ret = CodeJamMain();
    if (ret == 0) { GoodMessage(">>>> SUCCESS <<<<"); }
    else { BadMessage(">>>> FAILURE <<<<"); }
    system("pause");
    return ret;
}
