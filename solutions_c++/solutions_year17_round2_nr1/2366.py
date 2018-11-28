#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <list>
#include <algorithm>
#include <iterator>
#include <iomanip>

using namespace std;

typedef unsigned int uint;
typedef unsigned long ulong;
typedef unsigned long long ulonglong;


void solution()
{
	uint D, N;

	cin >> D >> N;

	double max = 0;
	for (uint i = 0; i < N; i++)
	{
		uint tempK, tempS;
		cin >> tempK >> tempS;

		double arrival = ((double)(D - tempK)) / (double)tempS;

		if (arrival > max)
			max = arrival;
	}

	cout << fixed << setprecision(6);
	cout << ((double)D) / max << endl;
}


int main(int argc, char ** argv)
{
	uint cases;

	ifstream in;
	ofstream out;

	streambuf *cinbuf = cin.rdbuf(); //save old buf
	streambuf *coutbuf = cout.rdbuf(); //save old buf

	if (argc == 2 || argc == 3)
	{
		in.open(argv[1]);
		cin.rdbuf(in.rdbuf()); //redirect cin to input file
	}

	if (argc == 3)
	{
		out.open(argv[2]);
		cout.rdbuf(out.rdbuf()); //redirect cout to output file
	}

	cin >> cases;

	for (uint i = 1; i <= cases; i++)
	{
		cerr << "Case #" << i << ": ";
		cout << "Case #" << i << ": ";
		solution();
		cerr << "Done" << endl;
	}


	// redirect cout to cerr
	cout.rdbuf(cerr.rdbuf());

	cout << "Done" << endl;

	// keep window open when run through vs
	cin.rdbuf(cinbuf);   //reset to standard input again
	std::cout << "Press ENTER to continue...";
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

	return 0;
}
