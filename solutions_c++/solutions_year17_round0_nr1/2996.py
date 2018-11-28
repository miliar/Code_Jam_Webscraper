#include <iostream>
#include <fstream>
#include <string>
#include <typeinfo>
#include <vector>
#include <cmath>
#include <boost/math/special_functions/sign.hpp>

class stream_reader
{
public:
	stream_reader(std::istream& s) : s_(s) {}
	template <typename T> T get()
	{
		T v;
		s_ >> v;
		if (s_.fail())
		{
			throw std::exception("Failed to read from a stream");
		}
		return v;
	}
private:
	std::istream& s_;
};


using namespace std;

void PrintUsage(const char* exeName)
{
	cout << "Usage: " << exeName << " infile [outfile]" << endl;
}

int solve(string& cakes, int k);

int main(int argc, char* argv[])
{
	if (argc < 2)
	{
		PrintUsage(argv[0]);
		return -1;
	}
	string inName = argv[1];

	string outName = argc > 2 ? argv[2] : inName + ".out";

	ifstream inFile(inName);
	if (!inFile.is_open())
	{
		cout << "Bad input file: " << inName.c_str() << endl;
		return -2;
	}

	ofstream outFile(outName);
	if (!outFile.is_open())
	{
		cout << "Bad output file: " << outName.c_str() << endl;
		return -3;
	}

	try
	{
		stream_reader r(inFile);
		auto T = r.get<int>();
		cout << "Number of cases: " << T;
		for (int k = 1; k <= T; ++k)
		{
			auto cakes = r.get<string>();
			auto size = r.get<int>();
			auto flips = solve(cakes, size);
			outFile << "Case #" << k << ": ";
			if (flips < 0)
			{
				outFile << "IMPOSSIBLE";
			}
			else
			{
				outFile << flips;
			}
			outFile << endl;
		}
	}
	catch (const std::exception& e)
	{
		std::cout << "exception [" << typeid(e).name() << "] " << (e.what() ? e.what() : "no description") << std::endl;
		return -4;
	}
	return 0;
}

int solve(string& cakes, int k)
{
	int flips = 0;
	int i = 0;
	for (; i <= ((int)cakes.size()) - k; ++i)
	{
		if (cakes[i] == '+') continue;
		// do flip
		cakes[i] = '+';
		int j = i + 1;
		for (int count = 1; count < k; ++count, ++j)
		{
			if (cakes[j] == '+')
			{
				cakes[j] = '-';
			}
			else
			{
				cakes[j] = '+';
			}
		}
		++flips;
	}
	for (; i < cakes.size(); ++i)
	{
		if (cakes[i] != '+') return -1; //impossible
	}
	return flips;
}
