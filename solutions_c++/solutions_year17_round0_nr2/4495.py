#include <memory>
#include <string>
#include <list>
#include <vector>
#include <set>
#include <map>
#include <fstream>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <math.h>  
#include <cmath>  
#include <bitset>

#include "bigint-2010.04.30/BigInteger.hh"

using namespace std;

#define all(a) (a).begin(), (a).end()
#define FOR(i, a, b) for (long i(a), _b(b); i < _b; ++i)
const double pi = 2 * acos(0.0);
// greatest common divisor
template<class T> T gcd(T a, T b) { return b == 0 ? a : gcd(b, a % b); }
// square
template<class T> T sqr(T a) { return (a)* (a); }

/*
struct cmpParty
{
	bool operator()(const party& a, const party &b)
	{
		return a.second > b.second;
	}
};*/


BigInteger absBigInt(const BigInteger &bg)
{
	if (bg < 0)
		return bg*BigInteger(-1);
	return bg;
}


class TestCaseSolver
{
public:
	TestCaseSolver() {}

	~TestCaseSolver() {
	}

	// to read/init the test case
	void readTestCase(std::istream &istr)
	{
		istr >> N;
	}

	bool isTidy(const string &s)
	{
		
	}
	
	// to solve the test case and output the value to ostr
	std::string solveTestCase()
	{
		stringstream ss;

		string tidyN = N;
		int s = N.size();
		int pos = N.size() - 1;
		int prev = N[pos];
		--pos;
		while (pos >= 0)
		{
			int cur = tidyN[pos];
			if (cur > prev)
			{
				tidyN[pos] -= 1;
				--cur;
				FOR(j, 1, s - pos )
				{
					tidyN[pos + j] = '9';
				}
			}
			prev = cur;
			--pos;
		}
		
		bool eraseO = true;
		for (char c : tidyN)
		{
			if (c != '0' || !eraseO)
			{
				eraseO = false;
				ss << c;
			}
		}
		return ss.str();
	}


	string N;

};



int main(int argc, char* argv[])
{
	std::ios_base::sync_with_stdio(false);

	std::string inputFile("C:\\Users\\David\\Downloads\\B-large.in");
	std::string outputFile("C:\\GoogleJam\\B.out");

	ofstream out;
	ifstream in;

	//in.open(argv[1]);
	//out.open(argv[2]);
	in.open(inputFile);
	out.open(outputFile);

	unsigned int nbTestCases;
	in >> nbTestCases;

	for (unsigned int curTest = 1; curTest <= nbTestCases; ++curTest)
	{
		TestCaseSolver testcaseSolver;

		testcaseSolver.readTestCase(in);
		std::string answer = testcaseSolver.solveTestCase();
		out << "Case #" << curTest << ": " << answer << '\n';
		cout << "Case #" << curTest << ": " << answer << endl;

	}
	out << flush;

	return 0;
}