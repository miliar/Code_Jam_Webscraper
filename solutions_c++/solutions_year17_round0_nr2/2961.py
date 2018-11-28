#include <stdio.h>
#include <tchar.h>
#include <iostream>
#include <fstream>
#include <string>
#include <typeinfo>

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

void makeTidy(string& n);

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
		for (int i = 1; i <= T; ++i)
		{
			auto n = r.get<string>();
			makeTidy(n);
			outFile << "Case #" << i << ": " << n << endl;
		}
	}
	catch (const std::exception& e)
	{
		std::cout << "exception [" << typeid(e).name() << "] " << (e.what() ? e.what() : "no description") << std::endl;
		return -4;
	}
	return 0;
}

void makeTidy(string& n)
{
	if (n.size() <= 1) return;
	auto previous = n[0];
	int index = 1;
	while (index < n.size())
	{
		auto current = n[index];
		if (current < previous) break;
		previous = current;
		++index;
	}
	if (index == n.size()) return; // nothing to adjust
	for (auto i = index + 1; i < n.size(); ++i)
	{
		n[i] = '9';
	}
	do
	{
		if (n[index] >= n[index - 1]) return;
		n[index] = '9';
		--n[--index];
	} while (index > 0);
	if (n[0] != '0') return;
	n.erase(n.begin());
}