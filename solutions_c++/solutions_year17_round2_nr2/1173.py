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

class UNICORN
{
public:
	int		count;
	char	color;
};

UNICORN		U[3];
uint		N, R, O, Y, G, B, V;
std::string S;

bool sortfunc(const UNICORN & a, const UNICORN & b)
{
	return a.count < b.count;
}

void read_task(std::fstream & input, std::fstream & output)
{
	input >> N >> R >> O >> Y >> G >> B >> V;
	U[0].color = 'R';
	U[0].count = R;
	U[1].color = 'Y';
	U[1].count = Y;	
	U[2].color = 'B';
	U[2].count = B;
}

void solve_task(std::fstream & input, std::fstream & output)
{
	S.clear();
	S.reserve(N);
	
	std::sort(&U[0], &U[0] + 3, sortfunc);

	if(U[2].count > U[0].count + U[1].count)
	{
		output << "IMPOSSIBLE";
		return;
	}

	while(U[2].count > U[1].count || U[2].count > U[0].count)
	{
		if(U[1].count >= U[0].count)
		{
			U[1].count--;
			S += U[1].color;

			U[2].count--;
			S += U[2].color;
		}
		else
		{
			U[0].count--;
			S += U[0].color;

			U[2].count--;
			S += U[2].color;
		}
	}

	if(U[2].count == U[1].count && U[2].count == U[0].count)
	{
	}
	else
	{
		DIE(L"err!");
	}

	while(U[2].count > 0)
	{
		S += U[0].color;
		S += U[1].color;
		S += U[2].color;
		U[2].count--;
	}

	output << S;
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
