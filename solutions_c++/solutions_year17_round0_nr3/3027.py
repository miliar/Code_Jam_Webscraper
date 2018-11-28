#include <fstream>
#include <iostream>
#include <vector>
#include <list>
#include <algorithm>
using namespace std;

typedef unsigned long long u_long;

struct stalls
{
	u_long N;
	u_long K;
};

void BathroomStalls(int argc, char** argv)
{
	ifstream in(argv[1]);
	ofstream out(argv[2]);

	unsigned int cases;
	in >> cases;
	vector<stalls> input;

	for (size_t i = 0; i < cases; ++i)
	{
		input.push_back(stalls());
		in >> input[i].N;
		in >> input[i].K;
	}
	in.close();

	for (size_t i = 0; i < cases; i++)
	{
		u_long n = input[i].N;
		u_long k = input[i].K;

		u_long div = 1;
		while (k / div > 0)
			div *= 2;
		
		div /= 2;

		u_long right = (n - (k - div)) / (2 * div);
		u_long left = (n - k) / (2 * div);

		out << "Case #" << i+1 << ": " << right << " " << left << endl;

	}

	out.close();
}