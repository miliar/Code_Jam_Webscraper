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
//#include "..\\..\\Libraries\\BigInteger\\BigIntegerLibrary.hh" // from http://mattmccutchen.net/bigint/
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
		int N, R, O, Y, G, B, V;
		input >> N >> R >> O >> Y >> G >> B >> V;

		ostringstream str;
		str << fixed << setprecision(16);

		bool impossible = false;
		if (R > Y + B || Y > R + B || B > R + Y) impossible = true;

		if (!impossible)
		{
			char last = ' ';
			char first = ' ';
			for (int i = 0; i < N; i++)
			{
				if (last == 'R')
				{
					if (Y > B || Y == B && first == 'Y') Y--, last = 'Y';
					else B--, last = 'B';
				}
				else if (last == 'Y')
				{
					if (R > B || R == B && first == 'R') R--, last = 'R';
					else B--, last = 'B';
				}
				else if (last == 'B')
				{
					if (R > Y || R == Y && first == 'R') R--, last = 'R';
					else Y--, last = 'Y';
				}
				else
				{
					if (R >= Y && R >= B) R--, last = 'R';
					else if (Y >= R && Y >= B) Y--, last = 'Y';
					else B--, last = 'B';
				}
				str << last;
				if (first == ' ') first = last;
			}
		}

		ostringstream answer;
		if (impossible) answer << "IMPOSSIBLE";
		else answer << str.str();
		auto s = str.str();

		int nR = 0, nY = 0, nB = 0;
		for (int i = 0; i < s.size(); i++)
		{
			if (s[i] == s[(i + 1) % s.size()])
			{
				BadMessage("ERROR AT " << i);
				DebugBreak();
			}
			if (s[i] == 'R') nR++;
			if (s[i] == 'Y') nY++;
			if (s[i] == 'B') nB++;
		}

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
