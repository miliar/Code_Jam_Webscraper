#include <stdio.h>
#include <tchar.h>
#include <iostream>
#include <fstream>
#include <string>
#include <typeinfo>
#include <map>
#include <vector>
#include <functional>

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

struct result
{
	int64_t max;
	int64_t min;
};

result solve(int64_t n, int64_t k);

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
			auto n = r.get<int64_t>();
			auto k = r.get<int64_t>();
			auto r = solve(n, k);
			outFile << "Case #" << i << ": " << r.max << ' ' << r.min << endl;
		}
	}
	catch (const std::exception& e)
	{
		std::cout << "exception [" << typeid(e).name() << "] " << (e.what() ? e.what() : "no description") << std::endl;
		return -4;
	}
	return 0;
}

using chunk_map = map<int64_t, int64_t, greater<int64_t>>;

result solve(int64_t n, int64_t k)
{
	chunk_map chunks;
	chunks.emplace(n, 1);
	int64_t p = 2;
	while (p < k + 1)
	{
		chunk_map chunks_new;
		for (auto& ch : chunks)
		{
			auto left = (ch.first - 1) / 2;
			auto right = ch.first - 1 - left;
			if (right == 0) break;
			chunks_new[right] += ch.second;
			if (left > 0) chunks_new[left] += ch.second;
		}
		if (chunks_new.size() == 0) return { 0,0 };
		chunks.swap(chunks_new);
		p *= 2;
	}
	k -= p / 2 - 1;
	for (auto& ch : chunks)
	{
		if (ch.second < k)
		{
			k -= ch.second;
			continue;
		}
		auto left = (ch.first - 1) / 2;
		auto right = ch.first - 1 - left;
		return { right, left };
	}
}
