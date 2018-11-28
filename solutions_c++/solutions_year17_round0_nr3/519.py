#include <windows.h>
#include <tchar.h>
#include <stdio.h>
#include <conio.h>
#include <map>
#include <list>
#include <vector>
#include <fstream>
#include <algorithm>
#include <string>
#include <stdint.h>
using namespace std;

#define DIE(format, ...) do{ wprintf(L"DIE: "format, ##__VA_ARGS__); DebugBreak(); }while(0);

typedef int sint32;
typedef long long sint64;
typedef sint64 sint;
typedef unsigned uint32;
typedef unsigned long long uint64;
typedef uint64 uint;

typedef std::map<uint, uint> I2C;
I2C		i2c;
uint	N, K;

void read_task(std::fstream & input, std::fstream & output)
{
	input >> N >> K;
}

void solve_task(std::fstream & input, std::fstream & output)
{
	uint	L, L1, L2, C, cnt;

	i2c.clear();
	i2c[N] = 1;
	cnt = K;

	for(;;)
	{
		L = i2c.rbegin()->first;
		C = i2c.rbegin()->second;
		i2c.erase(--i2c.end());

		if(L >= 1)
		{
			L1 = (L-1)/2;
			L2 = L - 1 - L1;
		}
		else
		{
			DIE(L"no space!!!");
		}

		if(cnt <= C)
		{
			break;
		}
		else
		{
			i2c[L1] += C;
			i2c[L2] += C;
			cnt -= C;
		}
	}
	output << L2 << " " << L1;
}

int main(int argc, _TCHAR* argv[])
{
	int cTask, iTask;
	std::fstream input, output;

	input.open("input.txt" , std::ios_base::in);
	output.open("output.txt" , std::ios_base::out);
	
	input >> cTask;
	for(iTask = 0; iTask < cTask; iTask++)
	{
		read_task(input, output);
		output << "Case #" << iTask + 1 << ": ";
		solve_task(input, output);
		output << std::endl;
	}

	input.close();
	output.close();
	wprintf(L"DONE\n");
	getch();
	return 0;
}
