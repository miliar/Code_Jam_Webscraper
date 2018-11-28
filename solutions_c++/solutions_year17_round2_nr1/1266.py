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

uint	D, N;
uint	K[1001], S[1001];

void read_task(std::fstream & input, std::fstream & output)
{
	input >> D >> N;
	for(int i = 0; i < N; i++)
	{
		input >> K[i] >> S[i];
	}
}

void solve_task(std::fstream & input, std::fstream & output)
{
	double T = 0;
	for(int i = 0; i < N; i++)
	{
		T = std::max(T, ((double)(D - K[i])) / ((double)S[i]));
	}
	T = ((double)D) / T;

	char str[256];
	sprintf(str, "%-20.6f", T);
	output << str;
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
