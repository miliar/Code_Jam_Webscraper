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

pair<long long, long long> f(long long n, long long k)
{
    if (k == 1) return make_pair((n + 1) / 2, (n + 2) / 2);
    if (n % 2 == 1) return f(n / 2, k / 2);
    if (k % 2 == 0) return f(n / 2, k / 2);
    return f(n / 2 - 1, k / 2);
}

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
        long long N;
        input >> N;
        long long K;
        input >> K;

        ostringstream answer;
        // 1
        // xxx => 1,1
        // 2
        // xxox => 1,2
        // xxxx => 1,1
        // 3
        // xoxox => 2,2
        // xxxox => 1,1
        // xxxxx => 1,1
        // 4
        // xoxoox => 2,3
        // xoxxox => 1,2
        // xxxxox => 1,1
        // xxxxxx => 1,1
        // 5
        // xooxoox => 3,3
        // xxoxoox => 1,2
        // xxoxxox => 1,2
        // xxxxxox => 1,1
        // xxxxxxx => 1,1
        // 6
        // xooxooox => 3,4
        // xooxoxox => 2,2
        // xxoxoxox => 1,2
        // xxxxoxox => 1,1
        // xxxxxxox => 1,1
        // xxxxxxxx => 1,1
        // 7
        // xoooxooox => 4,4
        // xoxoxooox => 2,2
        // xoxoxoxox => 2,2
        // xxxoxoxox => 1,1
        // xxxxxoxox => 1,1
        // xxxxxxxox => 1,1
        // xxxxxxxxx => 1,1
        // 8
        // xoooxoooox => 4,5
        // xoooxoxoox => 2,3
        // xoxoxoxoox => 2,2
        // xoxoxoxxox => 1,2
        // xxxoxoxxox => 1,1
        // xxxxxoxxox => 1,1
        // xxxxxxxxox => 1,1
        // xxxxxxxxxx => 1,1
        // 9
        // xooooxoooox => 5,5
        // xoxooxoooox => 2,3
        // xoxooxoxoox => 2,3
        // xoxxoxoxoox => 1,2
        // xoxxoxoxxox => 1,2
        // xxxxoxoxxox => 1,1
        // xxxxxxoxxox => 1,1
        // xxxxxxxxxox => 1,1
        // xxxxxxxxxxx => 1,1
        // 10
        // xooooxooooox => 5,6
        // xooooxooxoox => 3,3
        // xoxooxooxoox => 2,3
        // xoxxoxooxoox => 1,2
        // xoxxoxxoxoox => 1,2
        // xoxxoxxoxxox => 1,2
        // xxxxoxxoxxox => 1,1
        // xxxxxxxoxxox => 1,1
        // xxxxxxxxxxox => 1,1
        // xxxxxxxxxxxx => 1,1
        // 11
        // xoooooxooooox => 6,6
        // xooxooxooooox => 3,3
        // xooxooxooxoox => 3,3
        // xxoxooxooxoox => 1,2
        // xxoxxoxooxoox => 1,2
        // xxoxxoxxoxoox => 1,2
        // xxoxxoxxoxxox => 1,2
        // xxxxxoxxoxxox => 1,1
        // xxxxxxxxoxxox => 1,1
        // xxxxxxxxxxxox => 1,1
        // xxxxxxxxxxxxx => 1,1

        // Patterns:
        // min_1 = 1,1,2,2,3,3,4,4...
        // min_2 = x,1,1,1,1,2,2,2,2,3...
        // min_3 = x,x,1,1,1,1,2,2,2,2,3...

        // recursion
        // 11 just duplicates the 5's
        // 10 does 5 and 4
        // 9 does 4's
        // 8 does 4 and 3
        // etc.
        // so 11(n) => n=1 ? 5,5 : 5(n/2) => 2(n/4)
        // 10(n) => n=1 ? 5,6 : n%2? 4(n/2) : 5(n/2)???

        //pair<long long, long long> v[10]; 
        //for(int i = 0; i < 10; i++) v[i] = f(11, i + 1);

        auto ans = f(N, K);
        answer << ans.second - 1 << " " << ans.first - 1;

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
