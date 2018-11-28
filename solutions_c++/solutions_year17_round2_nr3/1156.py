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
		int N, Q;
		input >> N >> Q;
		long long E[102];
		int S[102];
		long long D[102][102];
		int U[102];
		int V[102];
		for (int i = 0; i < N; i++) input >> E[i] >> S[i];
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < N; j++)
			{
				input >> D[i][j];
			}
		}
		for (int i = 0; i < Q; i++)
		{
			input >> U[i] >> V[i];
		}

		// small dataset reduction
		struct city
		{
			double speed;
			double endurance;
			double distance;
		};
		vector<city> cities(N - 1);
		for (int i = 0; i < N - 1; i++)
		{
			cities[i].endurance = E[i];
			cities[i].speed = S[i];
			cities[i].distance = D[i][i + 1];
		}

		vector<double> minTime(N, 1e300);
		minTime[0] = 0;
		for (int i = 0; i < N - 1; i++)
		{
			long long dist = cities[i].distance;
			int j = 1;
			while (dist <= cities[i].endurance && i + j < N)
			{
				minTime[i + j] = min(minTime[i + j], minTime[i] + dist / cities[i].speed);
				if(i + j < N-1) dist += cities[i + j].distance;
				j++;
			}
		}

		ostringstream answer;
		answer << fixed << setprecision(16);

		answer << minTime[N - 1];

		answer << 0;

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
