#include <cstdint>
#include <cstring>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
#include <math.h>
#include <bitset>

using namespace std;

/*-------------------------------------------------------------------------
Typedefs
-------------------------------------------------------- -----------------*/

typedef int8_t s8;
typedef uint8_t u8;
typedef int16_t s16;
typedef uint16_t u16;
typedef int32_t s32;
typedef uint32_t u32;
typedef int64_t s64;
typedef uint64_t u64;
typedef float f32;
typedef double d64;

/*--------------------------------------------------------------------------------------------------------------------
Helper functions
--------------------------------------------------------------------------------------------------------------------*/

template<typename T>
void read(T& value) { cin >> value; cin.get(); }

template <>
void read(std::string& s) { getline(cin, s); }

/*--------------------------------------------------------------------------------------------------------------------
I/O Helper functions
--------------------------------------------------------------------------------------------------------------------*/

void redirectInput(const std::string& fileName)
{
	static ifstream fi(fileName, std::ios_base::in);
	std::cin.rdbuf(fi.rdbuf());
}

void redirectOutput(const std::string& fileName)
{
	static ofstream fo(fileName, std::ios_base::out);
	std::cout.rdbuf(fo.rdbuf());
}

string caseToString(s32 i)
{
	ostringstream oss;
	oss << "Case #" << (i + 1) << ": ";
	return oss.str();
}

/*--------------------------------------------------------------------------------------------------------------------
Solver functions
--------------------------------------------------------------------------------------------------------------------*/

struct Pair
{
	u32 max;
	u32 min;
};

void step(u64 s, u64& max, u64& min)
{
	u64 div = s / 2;
	u64 mod = s % 2;
	max = min = div;
	if (!mod && min) min--;
}

void solver(u64 s, u64 k, u64& max, u64& min)
{
	queue<u64> maxQ, minQ;
	maxQ.push(s);
	max = min = 0;
	while (k)
	{
		u64 next;
		if (maxQ.size())
		{
			if (minQ.size() && minQ.front() >= maxQ.front())
			{
				next = minQ.front();
				minQ.pop();
			}
			else
			{
				next = maxQ.front();
				maxQ.pop();
			}
		}
		else
		{
			next = minQ.front();
			minQ.pop();
		}
		step(next, max, min);

		maxQ.push(max);
		if (max != min) 
		{
				minQ.push(min);
		}
		else
		{
			maxQ.push(min);
		}
		k--;
	}
}

int main()
{
	redirectInput("in.txt");
	redirectOutput("out.txt");

	// read case count
	u32 caseCount;
	read(caseCount);

	u64 s, k;
	u64 max, min;

	for (u32 i = 0; i < caseCount; i++)
	{
		read(s);
		read(k);
		solver(s, k, max, min);
		cout << caseToString(i) << max << " " << min << endl;
	}

	return caseCount;
}