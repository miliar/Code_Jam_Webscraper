#include <memory>
#include <string>
#include <list>
#include <vector>
#include <set>
#include <map>
#include <queue>
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
#define ul unsigned long

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
		istr >> N >> K;
	}
	
	// to solve the test case and output the value to ostr
	std::string solveTestCase()
	{
		stringstream ss;

		unsigned long min, max;
		if (K == N)
		{
			min = max = 0;
		}
		/*else if (K > N / 2)
		{
			min = 0;
			max = 0;
		}*/
		else
		{
			std::priority_queue<ul> spaces;
			
			spaces.push(N);
			while (K--)
			{
				ul curSpace = spaces.top();
				//cout << "CurVal "<<curSpace << endl;
				spaces.pop();
				min = (curSpace-1) / 2;
				max = curSpace / 2;
				spaces.push(min);
				spaces.push(max);
			//	cout << "insert " << min << " and " << max << endl;
			}
		}


		ss << max << " " << min;
		return ss.str();
	}


	unsigned long K, N;

};



int main(int argc, char* argv[])
{
	std::ios_base::sync_with_stdio(false);

	std::string inputFile("C:\\Users\\David\\Downloads\\C-small-2-attempt0.in");
	std::string outputFile("C:\\GoogleJam\\C.out");

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

	int a;
	cin >> a;
	return 0;
}