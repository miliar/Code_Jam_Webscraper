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

bool IsTidy(u64 n)
{
	u64 max = 9;
	u64 k;
	while (n > 9)
	{
		k = n / 10;
		u64 mod = n - k * 10;
		if (mod > max) return false;
		max = mod;
		n = k;
	}
	return n <= max;
}

u64 GetTidy(u64 n)
{
	u64 max = 9;
	u64 k;
	u64 i = 0;
	vector<u64> v;
	while (n > 9)
	{
		
		k = n / 10;
		u64 mod = n - k * 10;
		v.push_back(mod);
		n = k;
	}
	v.push_back(n);
	if (v.size() == 1)
		return v[0];

	for (i = 1; i < v.size(); i++)
	{
		if (v[i] > v[i - 1])
		{
			if (v[i]) 
				v[i]--;
			else
				v[i] = 9;

			for (u32 j = i-1; j > 0; j--)
			{
				v[j] = 9;
			}
			v[0] = 9;
		}
	}

	u64 res = 0;
	u64 m = 1;
	for (i = 0; i < v.size(); i++)
	{
		res += v[i] * m;
		m *= 10;
	}
	return res;
}

int main()
{
	redirectInput("in.txt");
	redirectOutput("out.txt");

	// read case count
	u32 caseCount;
	read(caseCount);

	u64 n;
	for (u32 i = 0; i < caseCount; i++)
	{
		read(n);
		cout << caseToString(i) << GetTidy(n) << endl;
	}

	return caseCount;
}