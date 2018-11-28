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

#define E_PI 3.1415926535897932384626433832795028841971693993751058209749445923078164062

struct Pancake
{
    double R;
    double H;
};

//double getBest(vector<Pancake> P, int K)
//{
//    std::next_permutation()
//}

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

        int N, K;
        input >> N >> K;
        vector<Pancake> P(N);
        for (auto& p : P) input >> p.R >> p.H;

#if 1
        sort(P.begin(), P.end(), [](const Pancake& a, const Pancake& b)
        {
            double sA = 2.0 * a.R * a.H;
            double sB = 2.0 * b.R * b.H;
            return sA > sB;
            //if (a.R > b.R) return true;
            //if (a.R < b.R) return false;
            //return a.H > b.H;
        });
        
        vector<Pancake> P2;
        for (int i = 0; i < K - 1; i++) P2.push_back(P[0]), P.erase(P.begin());

        double maxR = 0;
        for (int i = 0; i < K - 1; i++) maxR = max(maxR, P2[i].R);
        sort(P.begin(), P.end(), [=](const Pancake& a, const Pancake& b)
        {
            double tA = 2.0 * a.R * a.H + max(0, a.R * a.R - maxR * maxR);
            double tB = 2.0 * b.R * b.H + max(0, b.R * b.R - maxR * maxR);
            return tA > tB;
            //if (tA > tB) return true;
            //if (tA < tB) return false;
            //double sA = 2.0 * a.R * a.H;
            //double sB = 2.0 * b.R * b.H;
            //return sA >= sB;
        });

        P2.push_back(P[0]), P.erase(P.begin());

        maxR = 0;
        for (int i = 0; i < K; i++) maxR = max(maxR, P2[i].R);

        double sum = maxR * maxR;
        for (auto& p : P2) sum += 2.0 * p.R * p.H;
#endif

        ostringstream answer;
        answer << fixed << setprecision(16);

        answer << sum * E_PI;
        //answer << getBest(P, K);

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
